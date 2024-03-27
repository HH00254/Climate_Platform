
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
from dateutil.relativedelta import relativedelta


def _format_payload_for_insert(list_data: list, location_payload: list, step: int) -> list[tuple]:
    '''
    Summary:
    - Formats scraped data from the website

      dictionary
    ARGS:
    - A list stucture containing key and values from a web-scrap that
      need to be reformated into a dictionary data structure
    Return:
    - Returns a List of tuples

    '''
    for location_element in location_payload:

        if location_element[0] == '' or location_element[0] == None:
            location_element = 'NULL'
 
    insert_args = []
    index = 0
    while index < len(list_data):

        try:

            if _checking_for_date(list_data, index, step):
                insert_args.append((
                    _format_date(list_data[index]),
                    str(location_payload[0]).split(' ', maxsplit=1)[0],
                    str(location_payload[1]).strip(),
                    float(list_data[index + 1]),
                    float(list_data[index + 2]),
                    float(list_data[index + 3])))

            else:
                # Not enough elements in list_data
                index =  index - step + 1

        except TypeError as e:
            _system_log(e, 
                       (
                        list_data[index], 
                        location_payload[0], 
                        location_payload[1], 
                        list_data[index + 1], 
                        list_data[index + 2], 
                        list_data[index + 3]))

        except ValueError as e:          
            _system_log(e, 
                       (
                        list_data[index], 
                        location_payload[0], 
                        location_payload[1], 
                        list_data[index + 1], 
                        list_data[index + 2], 
                        list_data[index + 3]))


        except IndexError as e:
            _system_log(e, 
                       (
                        list_data[index], 
                        location_payload[0], 
                        location_payload[1], 
                        list_data[index + 1], 
                        list_data[index + 2], 
                        list_data[index + 3]))

        finally:
            # Continue Incrementation
            index += step

    return insert_args


def _system_log(exception: Exception, data_entre=None) -> None:
    """
    Summary:
    - Opens and writes error logs to a file
      when issues arise from web-scrapping

    Args:
    - Exception object from the event
    - A data object of the corrupted data.

    Return:
    - None
    """
    log_date = datetime.now().strftime('%Y-%m-%d')
    
    with open(f'web_scraping_{log_date}.txt', 'a+', encoding="utf-8") as file_stream_output:

        file_stream_output.write(f'\nError: {exception}\n')
        file_stream_output.write(f'Data Row Corruption:\n {data_entre}\n')


def _format_date(unformatted_date: str) -> str:
    """
    Summary:
    - Re-formates string date data

    Args:
    - An unformated date as a string

    Return:
    - A formated date
    """
    return datetime.strptime(unformatted_date, '%B %d, %Y').strftime('%Y-%m-%d')


def _checking_for_date(data_collection, index, step) -> bool:
    """
    Check if the date at the current index is the same as the date at index + step in the data collection.

    Args:
    - data_collection (list): A list containing the data collection.
    - index (int): The current index in the data collection.
    - step (int): The step size to check for the next date.

    Returns:
    - bool: True if the dates are the same or if the index + step is at the end of the collection, False otherwise.
    """
    error_flag = False

    if len(data_collection) == index + step:
        error_flag = True

    elif index + step < len(data_collection):

        if(str(data_collection[index]).split(' ', maxsplit=1)[0].strip() ==
           str(data_collection[index + step]).split(' ', maxsplit=1)[0].strip()):
            error_flag = True

    return error_flag


def web_scrape_call()-> list[tuple]:
    """
    Summary:
    - When invoked this method calls climate.weather.gc.ca
      to begin scraping the website for weather data.

    Args:
    - None

    Return:
    - A list object containing tuples, that act as a row to store 
      the scraped data for insertion into a DB.
    """
    insert_values  = []
    current_date   = datetime.now()
    previous_data  = html.fromstring('<body><main><td>Null</td></main></body>')
    call_attempt   = 0
    data_flag      = True

    while data_flag and call_attempt < 12:

        month = current_date.month
        year  = current_date.year

        request = f'https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Year={year}&Month={month}#'
        response_body = requests.get(request, timeout=120)

        if response_body.status_code == 200 and response_body.content:
            tree = html.fromstring(response_body.content)

            if (tree.xpath('//td[position()<4]/text()') !=
                previous_data.xpath('//td[position()<4]/text()')):
                previous_data = tree

                city_path     = '//main/div/p/text()'
                province_path = '//main/div/br/text()'
                location_payload = tree.xpath(f"{city_path} | {province_path}")

                date_path      = '//table/tbody/tr[position()< last() -3]/th/abbr/@title'
                temperature_path = '//tr[position()< last() -3]/td[position()<4]/text()'
                table_load = tree.xpath(f"{date_path} | {temperature_path}")

                insert_values.append(_format_payload_for_insert(table_load, location_payload, 4))
                call_attempt = 0

                pprint(insert_values)

            else:
                data_flag = False

        else:
            call_attempt +=  1

        # Decrementing the time frame.
        current_date -= relativedelta(months=1)

    return insert_values

if __name__ == '__main__':
    #for testing    
    wheather_data =  web_scrape_call()
    
    for weather_element in wheather_data:
        pprint(weather_element)

    input('Press Enter to exit program...\n')