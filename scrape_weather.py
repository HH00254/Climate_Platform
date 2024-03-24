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
                float(list_data[index + 1]),
                float(list_data[index + 2]),
                float(list_data[index + 3])))

        except TypeError as e:
            print(f'Error: {e}')
            

    return insert_args

def format_date(unformatted_date: str) -> str:
    return datetime.strptime(unformatted_date, '%B %d, %Y').strftime('%Y-%d-%m')

def main()-> None:
    """
    Summary:
    - The main executable body for this module
    """
    day   = datetime.now().day
    month = datetime.now().month
    year  = datetime.now().year

    request = f'https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year={year}&Month={month}#'
    response_body = requests.get(request, timeout=60)

    if response_body.status_code == 200 and response_body.__sizeof__() > 0:
        tree = html.fromstring(response_body.content)

        city_path     = '//main/div/p/text()'
        province_path = '//main/div/br/text()'
        location_payload = tree.xpath(f"{city_path} | {province_path}")

        date_path      = f'//table/tbody/tr[position() < {day}]/th/abbr/@title'
        tempature_path = f'//tr[position() < {day}]/td[position()<4]/text()'
        table_load = tree.xpath(f"{date_path} | {tempature_path}")

        # pprint(table_load)

        insert_values = format_payload_for_insert(table_load, location_payload, 4)

        pprint(insert_values)

if __name__ == '__main__':
    main()
    input('Press Enter to exit program...\n')