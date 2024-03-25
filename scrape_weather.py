
"""

Description: Weather Processing App Group 9

Author: Lance Fuentes, Al Hochbaum, Christian Requerme

Section Number: FTO01

Date Created: 03/20/24

Credit:

Updates:

"""
import requests
from lxml import html
from datetime import datetime
from pprint import pprint
import calendar
import re

def format_payload_for_insert(list_data: list, location_payload: list, step: int) -> list[tuple]:

    '''

    Summary:

    - Copys a data-structure of type list and converts it into a

      dictionary

 

    ARGS:

    - A list stucture containing key and values from a web-scrap that

      need to be reformated into a dictionary data structure

    Return:

    - Returns a dictionary

    '''
    for location_element in location_payload:

        if location_element[0] == '' or location_element[0] == None:
            location_element = 'NULL'

    insert_args = []

    for index in range(0, len(list_data), step):
        try:
            insert_args.append((
                format_date(list_data[index]),
                str(location_payload[0]).split(' ', maxsplit=1)[0],
                str(location_payload[1]).strip(),
                float(sanitize_string(list_data[index + 1])),
                float(sanitize_string(list_data[index + 2])),
                float(sanitize_string(list_data[index + 3]))))

        except TypeError as e:
            print(f'Error: {e}')

        except ValueError as e:
            print(f'Error: {e}')

    return insert_args

 

def format_date(unformatted_date: str) -> str:
    return datetime.strptime(unformatted_date, '%B %d, %Y').strftime('%Y-%d-%m')

def sanitize_string(input_string):
    # Use regular expression to find digits in the input string
    sanitized_string = re.sub(r"[+,-,''][0-9]\.[0-9]", '', input_string).strip()

    return sanitized_string

def get_days_in_month(year, month) -> int:
    # Get the number of days in the specified month
    return calendar.monthrange(year, month)[1]

def main()-> None:
    """
    Summary:

    - The main executable body for this module

    """
    month = datetime.now().month
    year  = datetime.now().year
    last_year = year + 1
    decrement_value = 1
    table_load = []

    for index in range(year):
        if year != last_year:
            while month != 0:
                
                request = f'https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year={year}&Month={month}#'
                month = month - 1
                
                response_body = requests.get(request, timeout=60)

                if response_body.status_code == 200 and response_body.__sizeof__() > 0:
                    tree = html.fromstring(response_body.content)

                    city_path     = '//main/div/p/text()'
                    province_path = '//main/div/br/text()'
                    location_payload = tree.xpath(f"{city_path} | {province_path}")

                    number_of_days = get_days_in_month(year, month)

                    for inner_index in range(number_of_days):
                        
                        date_path       = f'//table/tbody/tr[{inner_index}]/th/abbr/@title'
                        tempature_path  = f'//tr[{inner_index}]/td[position()<4]/text()'
                    
                        table_load.append(tree.xpath(f"{date_path} | {tempature_path}"))

                    # insert_values = format_payload_for_insert(table_load, location_payload, 4)
                    
                    pprint(table_load)

            month = 12
            decrement_value = decrement_value + index
            last_year = year
            year = year - decrement_value
        else:
            break

if __name__ == '__main__':

    main()

    input('Press Enter to exit program...\n')