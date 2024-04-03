[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LvdQZzDp)
This is an example file for you to include in your project.
You must have a title, a project description and a pylint section in this file. There are also other sections you should consider to have. *Make it professional.*

# Weather Processing App

## Project Description
```
Course: ADEV-3005 Programming in Python
Instructor:
Section Number:
Author:
Date Created:
Credit: 
Updates:
```
Expand the Project Introduction to include a detailed description of what the project does, its purpose, and who it's for. Highlight any unique features or challenges addressed by the project.

## Optional sections to include

**Installation**: Provide step-by-step instructions on how to install and set up the project. Include any prerequisites, such as Python version or external libraries, and how to install them.

**Usage**: Explain how to use the application, including command-line arguments, configuration files, and examples of common use cases. Screenshots or GIFs can be very helpful here.

**Technologies Used**: List the programming languages, frameworks, libraries, and any other technologies used in the project. This is helpful for understanding the project's technical stack and for users looking to learn from your code.

**Features**: Outline the key features of your application. This section can highlight what makes your project stand out.

**Acknowledgments**: A section to give thanks to individuals, organizations, or resources that contributed to the success of the project. This can include sources of inspiration, financial support, or technical guidance.

**Contact Information**: Provide details on how to reach the authors or maintainers for further questions or discussions about the project.

**Frequently Asked Questions (FAQs)**: Address common questions about the project. This can save time for both the project team and users.

**Known Issues and Limitations**: Document any known bugs or limitations in the current version of the project. This transparency can help manage user expectations and encourage contributions to resolve these issues.

**Future Work**: Briefly describe any planned enhancements or features for future releases. This shows that the project is active and continually improving.


### Pylint Result
************* Module scrape_weather
scrape_weather.py:27:0: C0301: Line too long (123/100) (line-too-long)
scrape_weather.py:36:146: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:51:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:53:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:65:0: C0301: Line too long (114/100) (line-too-long)
scrape_weather.py:68:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:71:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:72:0: C0301: Line too long (140/100) (line-too-long)
scrape_weather.py:134:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:157:0: C0301: Line too long (111/100) (line-too-long)
scrape_weather.py:190:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:205:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:215:0: C0304: Final newline missing (missing-final-newline)
scrape_weather.py:11:0: E0401: Unable to import 'lxml' (import-error)
scrape_weather.py:12:0: E0401: Unable to import 'dateutil.relativedelta' (import-error)
scrape_weather.py:13:0: E0401: Unable to import 'requests' (import-error)
scrape_weather.py:54:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
************* Module dbcm
dbcm.py:75:0: C0304: Final newline missing (missing-final-newline)
************* Module scrape
scrape.py:18:0: C0301: Line too long (123/100) (line-too-long)
scrape.py:27:146: C0303: Trailing whitespace (trailing-whitespace)
scrape.py:42:0: C0303: Trailing whitespace (trailing-whitespace)
scrape.py:44:0: C0303: Trailing whitespace (trailing-whitespace)
scrape.py:56:0: C0301: Line too long (114/100) (line-too-long)
scrape.py:59:0: C0303: Trailing whitespace (trailing-whitespace)
scrape.py:62:0: C0303: Trailing whitespace (trailing-whitespace)
scrape.py:63:0: C0301: Line too long (140/100) (line-too-long)
scrape.py:125:0: C0303: Trailing whitespace (trailing-whitespace)
scrape.py:148:0: C0301: Line too long (111/100) (line-too-long)
scrape.py:181:0: C0303: Trailing whitespace (trailing-whitespace)
scrape.py:195:0: C0303: Trailing whitespace (trailing-whitespace)
scrape.py:206:0: C0303: Trailing whitespace (trailing-whitespace)
scrape.py:1:0: C0114: Missing module docstring (missing-module-docstring)
scrape.py:2:0: E0401: Unable to import 'lxml' (import-error)
scrape.py:3:0: E0401: Unable to import 'dateutil.relativedelta' (import-error)
scrape.py:4:0: E0401: Unable to import 'requests' (import-error)
scrape.py:5:0: E0611: No name 'PdUtil' in module 'prod_util' (no-name-in-module)
scrape.py:45:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
************* Module main
main.py:24:0: C0301: Line too long (113/100) (line-too-long)
main.py:25:0: C0301: Line too long (124/100) (line-too-long)
main.py:35:0: C0303: Trailing whitespace (trailing-whitespace)
main.py:44:0: C0304: Final newline missing (missing-final-newline)
main.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module db_operations
db_operations.py:127:0: C0304: Final newline missing (missing-final-newline)
db_operations.py:84:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
db_operations.py:118:15: W0718: Catching too general exception Exception (broad-exception-caught)
************* Module plot_operations
plot_operations.py:11:0: C0304: Final newline missing (missing-final-newline)
plot_operations.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module prod_util
prod_util.py:37:0: C0303: Trailing whitespace (trailing-whitespace)
prod_util.py:56:0: C0305: Trailing newlines (trailing-newlines)
************* Module weather_processor
weather_processor.py:8:0: C0304: Final newline missing (missing-final-newline)
weather_processor.py:8:0: C0304: Final newline missing (missing-final-newline)
weather_processor.py:1:0: R0801: Similar lines in 2 files
==scrape:[113:205]
==scrape_weather:[122:215]
                                        location_payload[0],
                                        location_payload[1],
                                        list_data[index + 1],
                                        list_data[index + 2],
                                        list_data[index + 3]))

            finally:
                # Continue Incrementation
                index += step

        return insert_collection

    def get_xpath_page_values(self, trees) -> list:
        """
        Extract values from the parsed HTML trees.

        Args:
        - trees: List of parsed HTML trees.

        Returns:
        - list: List of tuples for insertion into the database.
        """
        insert_values = []

        for tree in trees:
            if tree.xpath('//td[position()<4]/text()'):
                city_path     = '//main/div/p/text()'
                province_path = '//main/div/br/text()'
                location_payload = tree.xpath(f"{city_path} | {province_path}")

                date_path        = '//table/tbody/tr[position()< last() -3]/th/abbr/@title'
                temperature_path = '//tr[position()< last() -3]/td[position()<4]/text()'
                table_load = tree.xpath(f"{date_path} | {temperature_path}")

                insert_values = self._format_payload_for_insert(table_load, location_payload, insert_values, 4)

        return insert_values

    def web_scrape_call(self, st_year: int, st_month = None) -> list:
        """
        Perform the web scraping call to retrieve weather data.

        Args:
        - st_year (int): The starting year for scraping.
        - st_month (int): The starting month for scraping. Defaults to None.

        Returns:
        - list: List of parsed HTML trees containing weather data.
        """
        month_counter    = 0
        month            = 0
        previous_data    = html.fromstring('<body><main><td>Null</td></main></body>')
        termination_flag = True
        call_attempt     = 0
        tree_pages = []

        if st_year is not None and st_month is not None:
            working_date = datetime(st_year, st_month, 1)
            month_range  = working_date.month

        else:
            working_date = self.date_instance
            month_range  = working_date.month

        while call_attempt < 12 and termination_flag and month_counter < month_range:
            month      = working_date.month
            year       = working_date.year

            request = self.web_address.format(self.station_id, year, month)
            response_body = requests.get(request, timeout=120)

            if (response_body.status_code == 200 and
                html.fromstring(response_body.content).xpath('//table/tbody')):
                tree = html.fromstring(response_body.content)

                if (tree.xpath('//td[position()<4]/text()') !=
                    previous_data.xpath('//td[position()<4]/text()')):
                    previous_data = tree
                    tree_pages.append(tree)

                    call_attempt     = 0
                    month_counter += 1

                else:
                    termination_flag = False

            else:
                call_attempt +=  1

            # Decrementing the time frame.
            working_date -= relativedelta(months=1)

        return tree_pages (duplicate-code)
weather_processor.py:1:0: R0801: Similar lines in 2 files
==scrape:[6:60]
==scrape_weather:[15:69]
class ScrapeWeather:
    """
    Summary:
    - A Weather scraper class that work on https://climate.weather.gc.ca
    """

    def __init__(self, date_instance = datetime.now(), station_id = 27174) -> None:
        """
        Initialize the ScrapeWeather class.

        Args:
        - date_instance (datetime): The date instance for which weather data is scraped. Defaults to current date and time.
        - station_id (int): The ID of the weather station. Defaults to 27174.

        Returns:
        None
        """
        self.date_instance  = date_instance
        self.station_id     = station_id
        self.web_address    = """
            https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID={}&timeframe=2&StartYear=1840&EndYear=2018&Year={}&Month={}#"""
        self.end_year       = self.get_data_end_point()

    def get_data_end_point(self, page_year = 1840) -> int:
        """
        Get the end year for data retrieval based on the current date.

        Args:
        - page_year (int): The starting year for data retrieval. Defaults to 1840.

        Returns:
        - int: The end year for data retrieval.
        """
        request = self.web_address.format(self.station_id, page_year, self.date_instance.month)
        response_body = requests.get(request, timeout=120)

        return self.get_xpath_year(html.fromstring(response_body.content))

    def get_xpath_year(self, tree_doc) -> int:
        """
        Extract the year from the webpage content.

        Args:
        - tree_doc: The parsed HTML tree of the webpage content.

        Returns:
        - int: The year extracted from the webpage.
        """
        try:
            year = (str(tree_doc.xpath('//*[@id="climateNav"]/div[3]/section/div[1]/form/fieldset/legend/text()'))
                                .split('(')[1].split(')')[0])
            return int(year)

        except TypeError as e: (duplicate-code)
weather_processor.py:1:0: R0801: Similar lines in 2 files
==scrape:[104:112]
==scrape_weather:[113:121]
                                        location_payload[0],
                                        location_payload[1],
                                        list_data[index + 1],
                                        list_data[index + 2],
                                        list_data[index + 3]))

            except IndexError as e:
                index =  index - step + 1 (duplicate-code)
weather_processor.py:1:0: R0801: Similar lines in 2 files
==scrape:[95:103]
==scrape_weather:[104:112]
                                        location_payload[0],
                                        location_payload[1],
                                        list_data[index + 1],
                                        list_data[index + 2],
                                        list_data[index + 3]))

            except ValueError as e:
                index =  index - step + 1 (duplicate-code)
weather_processor.py:1:0: R0801: Similar lines in 2 files
==scrape:[86:94]
==scrape_weather:[95:103]
                    str(location_payload[0]).split(' ', maxsplit=1)[0],
                    str(location_payload[1]).strip(),
                    float(list_data[index + 1]),
                    float(list_data[index + 2]),
                    float(list_data[index + 3]))))

            except TypeError as e:
                index =  index - step + 1 (duplicate-code)
weather_processor.py:1:0: R0801: Similar lines in 2 files
==scrape:[75:85]
==scrape_weather:[84:94]
        for location_element in location_payload:

            if location_element[0] == '' or location_element[0] is None:
                location_element = 'NULL'

        index = 0
        while index < len(list_data):

            try:
                insert_collection.append((( (duplicate-code)
weather_processor.py:1:0: R0801: Similar lines in 2 files
==scrape:[95:101]
==scrape_weather:[113:119]
                                        location_payload[0],
                                        location_payload[1],
                                        list_data[index + 1],
                                        list_data[index + 2],
                                        list_data[index + 3]))
 (duplicate-code)
weather_processor.py:1:0: R0801: Similar lines in 2 files
==scrape:[104:110]
==scrape_weather:[104:110]
                                        location_payload[0],
                                        location_payload[1],
                                        list_data[index + 1],
                                        list_data[index + 2],
                                        list_data[index + 3]))
 (duplicate-code)

-----------------------------------
Your code has been rated at 6.82/10

