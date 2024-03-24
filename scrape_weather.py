"""
Description: Weather Processing App Group 9
Author: Lance Fuentes, Al Hochbaum, Christian Requerme
Section Number: FTO01
Date Created: 03/20/24
Credit:
Updates: Handling non float temp not working
"""
import requests
from lxml import html
from datetime import datetime
from pprint import pprint
#pip install python-dateutil
from dateutil.relativedelta import relativedelta

def format_payload_for_insert(list_data: list, location_payload: list, step: int) -> list[tuple]:
    '''
    Summary: 
    - Copies a data-structure of type list and converts it into a 
      dictionary

    ARGS:
    - A list structure containing key and values from a web-scrap that
      need to be reformatted into a dictionary data structure

    Return:
    - Returns a dictionary
    '''
    insert_args = []

    for index in range(0, len(list_data), step): 
        try:
            date = format_date(list_data[index])
            location = str(location_payload[0]).split(' ', maxsplit=1)[0]
            province = str(location_payload[1]).strip()
            max_temp = try_convert_to_float(list_data[index + 1])
            min_temp = try_convert_to_float(list_data[index + 2])
            mean_temp = try_convert_to_float(list_data[index + 3])

            if None in (date, location, province, max_temp, min_temp, mean_temp):
                continue

            insert_args.append((
                date,
                location,
                province,
                max_temp,
                min_temp,
                mean_temp))
        except IndexError:
            # Not enough elements in list_data
            break
        except Exception as e:
            print(f'Error: {e}')
            continue

    return insert_args

def try_convert_to_float(value: str) -> float:
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def format_date(unformatted_date: str) -> str:
    try:
        # Attempt to parse the date in various formats
        formatted_date = datetime.strptime(unformatted_date, '%B %d, %Y').strftime('%Y-%m-%d')
    except ValueError:
        try:
            formatted_date = datetime.strptime(unformatted_date, '%Y-%m-%d').strftime('%Y-%m-%d')
        except ValueError:
            formatted_date = ''
    return formatted_date


def main()-> None:
    """
    Summary:
    - The main executable body for this module
    """

    current_date = datetime.now()

    while True:
        month = current_date.month
        year  = current_date.year

        request = f'https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Year={year}&Month={month}#'
        response_body = requests.get(request, timeout=60)

        if response_body.status_code == 200 and response_body.__sizeof__() > 0:
            tree = html.fromstring(response_body.content)

            city_path     = '//main/div/p/text()'
            province_path = '//main/div/br/text()'
            location_payload = tree.xpath(f"{city_path} | {province_path}")

            date_path      = '//table/tbody/tr/th/abbr/@title'
            temperature_path = '//tr/td[position()<4]/text()'
            table_load = tree.xpath(f"{date_path} | {temperature_path}")

            # pprint(table_load)

            insert_values = format_payload_for_insert(table_load, location_payload, 4)

            pprint(insert_values)
        else:
            break
        current_date -= relativedelta(months=1)

if __name__ == '__main__':
    main()
    input('Press Enter to exit program...\n')
