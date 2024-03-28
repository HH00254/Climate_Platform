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
scrape_weather.py:131:0: C0301: Line too long (106/100) (line-too-long)
scrape_weather.py:139:0: C0301: Line too long (115/100) (line-too-long)
scrape_weather.py:179:0: C0301: Line too long (164/100) (line-too-long)
scrape_weather.py:220:0: C0304: Final newline missing (missing-final-newline)
scrape_weather.py:11:0: E0401: Unable to import 'requests' (import-error)
scrape_weather.py:12:0: E0401: Unable to import 'lxml' (import-error)
scrape_weather.py:16:0: E0401: Unable to import 'dateutil.relativedelta' (import-error)
scrape_weather.py:34:40: C0121: Comparison 'location_element[0] == None' should be 'location_element[0] is None' (singleton-comparison)
scrape_weather.py:155:0: R0914: Too many local variables (16/15) (too-many-locals)
scrape_weather.py:13:0: C0411: standard import "datetime.datetime" should be placed before third party imports "requests", "lxml.html" (wrong-import-order)
scrape_weather.py:14:0: C0411: standard import "pprint.pprint" should be placed before third party imports "requests", "lxml.html" (wrong-import-order)
scrape_weather.py:15:0: C0411: standard import "calendar" should be placed before third party imports "requests", "lxml.html" (wrong-import-order)
scrape_weather.py:15:0: W0611: Unused import calendar (unused-import)
************* Module _scrape_weather
_scrape_weather.py:93:0: C0301: Line too long (164/100) (line-too-long)
_scrape_weather.py:127:0: C0304: Final newline missing (missing-final-newline)
_scrape_weather.py:10:0: E0401: Unable to import 'requests' (import-error)
_scrape_weather.py:11:0: E0401: Unable to import 'lxml' (import-error)
_scrape_weather.py:15:0: E0401: Unable to import 'dateutil.relativedelta' (import-error)
_scrape_weather.py:32:40: C0121: Comparison 'location_element[0] == None' should be 'location_element[0] is None' (singleton-comparison)
_scrape_weather.py:63:0: C0116: Missing function or method docstring (missing-function-docstring)
_scrape_weather.py:66:0: C0116: Missing function or method docstring (missing-function-docstring)
_scrape_weather.py:79:0: R0914: Too many local variables (16/15) (too-many-locals)
_scrape_weather.py:12:0: C0411: standard import "datetime.datetime" should be placed before third party imports "requests", "lxml.html" (wrong-import-order)
_scrape_weather.py:13:0: C0411: standard import "pprint.pprint" should be placed before third party imports "requests", "lxml.html" (wrong-import-order)
_scrape_weather.py:14:0: C0411: standard import "calendar" should be placed before third party imports "requests", "lxml.html" (wrong-import-order)
_scrape_weather.py:14:0: W0611: Unused import calendar (unused-import)
************* Module main
main.py:29:0: C0304: Final newline missing (missing-final-newline)
main.py:15:0: C0116: Missing function or method docstring (missing-function-docstring)
main.py:12:0: C0411: standard import "pprint.pprint" should be placed before first party imports "db_operations.DBOperations", "scrape_weather"  (wrong-import-order)
main.py:13:0: C0411: standard import "time.time" should be placed before first party imports "db_operations.DBOperations", "scrape_weather"  (wrong-import-order)
************* Module db_operations
db_operations.py:85:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
db_operations.py:119:15: W0718: Catching too general exception Exception (broad-exception-caught)
************* Module plot_operations
plot_operations.py:8:0: C0304: Final newline missing (missing-final-newline)
plot_operations.py:8:0: C0304: Final newline missing (missing-final-newline)
************* Module test
test.py:5:0: C0304: Final newline missing (missing-final-newline)
test.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module weather_processor
weather_processor.py:1:0: R0801: Similar lines in 2 files
==_scrape_weather:[63:83]
==scrape_weather:[125:167]
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
    """ (duplicate-code)
weather_processor.py:1:0: R0801: Similar lines in 2 files
==_scrape_weather:[42:51]
==scrape_weather:[45:56]
                    str(location_payload[0]).split(' ', maxsplit=1)[0],
                    str(location_payload[1]).strip(),
                    float(list_data[index + 1]),
                    float(list_data[index + 2]),
                    float(list_data[index + 3])))
            else:
                # Not enough elements in list_data
                index =  index - step + 1
        except TypeError as e: (duplicate-code)
weather_processor.py:1:0: R0801: Similar lines in 2 files
==_scrape_weather:[30:39]
==scrape_weather:[31:42]
    for location_element in location_payload:

        if location_element[0] == '' or location_element[0] == None:
            location_element = 'NULL'

    insert_args = []
    index = 0
    while index < len(list_data):

        try:
 (duplicate-code)
weather_processor.py:1:0: R0801: Similar lines in 2 files
==_scrape_weather:[98:107]
==scrape_weather:[188:196]
            city_path     = '//main/div/p/text()'
            province_path = '//main/div/br/text()'
            location_payload = tree.xpath(f"{city_path} | {province_path}")

            date_path      = '//table/tbody/tr[position()< last() -3]/th/abbr/@title'
            temperature_path = '//tr[position()< last() -3]/td[position()<4]/text()'
            table_load = tree.xpath(f"{date_path} | {temperature_path}")

            # Check if the current data is not empty and is the same as the previous non-empty data (duplicate-code)

-----------------------------------
Your code has been rated at 7.25/10

