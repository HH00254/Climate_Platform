
"""
Description: Weather Processing App Group 9
Author: Lance Fuentes, Al Hochbaum, Christian Requerme
Section Number: FTO01
Date Created: 03/20/24
Credit:
Updates:
"""
from datetime import datetime
from pprint import pprint
import requests
from lxml import html
from dateutil.relativedelta import relativedelta
from db_operations import DBOperations

db_operations = DBOperations('weather_data.sqlite')

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
    index = 0
    while index < len(list_data):

        try:
            if checking_for_date(list_data, index, step):
                insert_args.append((
                    format_date(list_data[index]),
                    str(location_payload[0]).split(' ', maxsplit=1)[0],
                    str(location_payload[1]).strip(),
                    float(list_data[index + 1]),
                    float(list_data[index + 2]),
                    float(list_data[index + 3])))
            else:
                # Not enough elements in list_data
                index =  index - step + 1
        except TypeError as e:
            print(f'Error: {e}')
        except ValueError as e:
            print(f'Error: {e}')
        except IndexError as e:
            print(f'Error: {e}')
        finally:
            # Continue Incrementation
            index += step

    return insert_args

def format_date(unformatted_date: str) -> str:
    return datetime.strptime(unformatted_date, '%B %d, %Y').strftime('%Y-%m-%d')

def checking_for_date(data_collection, index, step) -> bool:
    error_flag = False

    if len(data_collection) == index + step:
        error_flag = True
    elif index + step < len(data_collection):
        if(str(data_collection[index]).split(' ', maxsplit=1)[0].strip() ==
           str(data_collection[index + step]).split(' ', maxsplit=1)[0].strip()):
            error_flag = True

    return error_flag


def main()-> None:
    """
    Summary:
    - The main executable body for this module
    """
    current_date   = datetime.now()
    previous_data  = None
    data_flag = True

    while data_flag:

        month = current_date.month
        year  = current_date.year

        request = f'https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Year={year}&Month={month}#'
        response_body = requests.get(request, timeout=60)

        if response_body.status_code == 200 and response_body.content:
            tree = html.fromstring(response_body.content)

            city_path     = '//main/div/p/text()'
            province_path = '//main/div/br/text()'
            location_payload = tree.xpath(f"{city_path} | {province_path}")

            date_path      = '//table/tbody/tr[position()< last() -3]/th/abbr/@title'
            temperature_path = '//tr[position()< last() -3]/td[position()<4]/text()'
            table_load = tree.xpath(f"{date_path} | {temperature_path}")

            # Check if the current data is not empty and is the same as the previous non-empty data
            if table_load and table_load == previous_data:
                data_flag = False

            elif table_load:
                previous_data = table_load
                insert_values = format_payload_for_insert(table_load, location_payload, 4)

                pprint(insert_values)

            for entry in insert_values:
                db_operations.save_data(entry)
        else:
            data_flag = False

        # Decrementing the time frame.
        current_date -= relativedelta(months=1)

if __name__ == '__main__':
    main()
    input('Press Enter to exit program...\n')