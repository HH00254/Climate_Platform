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
<<<<<<< HEAD
************* Module scrape_weather
scrape_weather.py:42:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:63:26: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:65:41: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:66:44: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:67:44: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:68:45: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:69:45: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:72:31: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:73:26: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:75:41: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:76:44: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:77:44: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:78:45: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:79:45: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:84:26: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:86:41: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:87:44: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:88:44: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:89:45: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:90:45: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:114:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:137:0: C0301: Line too long (106/100) (line-too-long)
scrape_weather.py:145:0: C0301: Line too long (115/100) (line-too-long)
scrape_weather.py:185:0: C0301: Line too long (164/100) (line-too-long)
scrape_weather.py:220:16: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:222:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:226:0: C0304: Final newline missing (missing-final-newline)
scrape_weather.py:17:0: E0401: Unable to import 'requests' (import-error)
scrape_weather.py:18:0: E0401: Unable to import 'lxml' (import-error)
scrape_weather.py:22:0: E0401: Unable to import 'dateutil.relativedelta' (import-error)
scrape_weather.py:40:40: C0121: Comparison 'location_element[0] == None' should be 'location_element[0] is None' (singleton-comparison)
scrape_weather.py:161:0: R0914: Too many local variables (16/15) (too-many-locals)
scrape_weather.py:19:0: C0411: standard import "datetime.datetime" should be placed before third party imports "requests", "lxml.html" (wrong-import-order)
scrape_weather.py:20:0: C0411: standard import "pprint.pprint" should be placed before third party imports "requests", "lxml.html" (wrong-import-order)
scrape_weather.py:21:0: C0411: standard import "calendar" should be placed before third party imports "requests", "lxml.html" (wrong-import-order)
scrape_weather.py:21:0: W0611: Unused import calendar (unused-import)
************* Module _scrape_weather
_scrape_weather.py:92:0: C0301: Line too long (164/100) (line-too-long)
_scrape_weather.py:126:0: C0304: Final newline missing (missing-final-newline)
_scrape_weather.py:12:0: E0401: Unable to import 'requests' (import-error)
_scrape_weather.py:13:0: E0401: Unable to import 'lxml' (import-error)
_scrape_weather.py:14:0: E0401: Unable to import 'dateutil.relativedelta' (import-error)
_scrape_weather.py:31:40: C0121: Comparison 'location_element[0] == None' should be 'location_element[0] is None' (singleton-comparison)
_scrape_weather.py:62:0: C0116: Missing function or method docstring (missing-function-docstring)
_scrape_weather.py:65:0: C0116: Missing function or method docstring (missing-function-docstring)
_scrape_weather.py:78:0: R0914: Too many local variables (16/15) (too-many-locals)
************* Module main
main.py:21:0: C0304: Final newline missing (missing-final-newline)
main.py:1:0: C0114: Missing module docstring (missing-module-docstring)
main.py:3:0: C0411: standard import "pprint.pprint" should be placed before first party imports "db_operations.DBOperations", "scrape_weather"  (wrong-import-order)
main.py:4:0: C0411: standard import "time.time" should be placed before first party imports "db_operations.DBOperations", "scrape_weather"  (wrong-import-order)
main.py:3:0: W0611: Unused pprint imported from pprint (unused-import)
main.py:4:0: W0611: Unused time imported from time (unused-import)
************* Module db_operations
db_operations.py:85:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
************* Module plot_operations
plot_operations.py:10:0: E0401: Unable to import 'matplotlib.pyplot' (import-error)
plot_operations.py:12:0: C0115: Missing class docstring (missing-class-docstring)
plot_operations.py:12:0: R0903: Too few public methods (0/2) (too-few-public-methods)
plot_operations.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
plot_operations.py:17:19: W0613: Unused argument 'self' (unused-argument)
plot_operations.py:17:25: W0613: Unused argument 'year_range' (unused-argument)
************* Module test
test.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module weather_processor
weather_processor.py:1:0: R0801: Similar lines in 2 files
==_scrape_weather:[62:82]
==scrape_weather:[131:173]
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
==_scrape_weather:[41:50]
==scrape_weather:[51:62]
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
==_scrape_weather:[29:38]
==scrape_weather:[37:48]
    for location_element in location_payload:
        if location_element[0] == '' or location_element[0] == None:
            location_element = 'NULL'

    insert_args = []
    index = 0
    while index < len(list_data):

        try: (duplicate-code)
weather_processor.py:1:0: R0801: Similar lines in 2 files
==_scrape_weather:[97:106]
==scrape_weather:[195:203]
                city_path     = '//main/div/p/text()'
                province_path = '//main/div/br/text()'
                location_payload = tree.xpath(f"{city_path} | {province_path}")

                date_path      = '//table/tbody/tr[position()< last() -3]/th/abbr/@title'
                temperature_path = '//tr[position()< last() -3]/td[position()<4]/text()'
                table_load = tree.xpath(f"{date_path} | {temperature_path}")
 (duplicate-code)

-----------------------------------
<<<<<<< HEAD
Your code has been rated at 6.48/10
=======
************* Module db_operations
db_operations.py:86:0: C0303: Trailing whitespace (trailing-whitespace)
db_operations.py:135:0: C0301: Line too long (107/100) (line-too-long)
db_operations.py:178:0: C0301: Line too long (198/100) (line-too-long)
db_operations.py:199:0: C0301: Line too long (196/100) (line-too-long)
db_operations.py:212:0: C0303: Trailing whitespace (trailing-whitespace)
db_operations.py:216:0: C0304: Final newline missing (missing-final-newline)
************* Module weather_processor
weather_processor.py:25:0: C0303: Trailing whitespace (trailing-whitespace)
weather_processor.py:76:113: C0303: Trailing whitespace (trailing-whitespace)
weather_processor.py:76:0: C0301: Line too long (113/100) (line-too-long)
weather_processor.py:78:0: C0301: Line too long (117/100) (line-too-long)
weather_processor.py:79:0: C0301: Line too long (127/100) (line-too-long)
weather_processor.py:86:0: C0303: Trailing whitespace (trailing-whitespace)
weather_processor.py:89:0: C0303: Trailing whitespace (trailing-whitespace)
weather_processor.py:153:0: C0304: Final newline missing (missing-final-newline)
************* Module scrape_weather
scrape_weather.py:35:43: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:38:146: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:54:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:66:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:68:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:82:0: C0301: Line too long (114/100) (line-too-long)
scrape_weather.py:84:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:157:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:184:35: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:193:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:206:45: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:212:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:246:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:250:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:261:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:283:0: C0304: Final newline missing (missing-final-newline)
scrape_weather.py:11:0: E0401: Unable to import 'lxml' (import-error)
scrape_weather.py:12:0: E0401: Unable to import 'dateutil.relativedelta' (import-error)
scrape_weather.py:13:0: E0401: Unable to import 'requests' (import-error)
scrape_weather.py:218:4: R0914: Too many local variables (16/15) (too-many-locals)
scrape_weather.py:15:0: C0411: standard import "math" should be placed before third party imports "lxml.html", "dateutil.relativedelta.relativedelta", "requests" and first party import "prod_util.ProdUtil"  (wrong-import-order)
scrape_weather.py:15:0: W0611: Unused import math (unused-import)
************* Module dbcm
dbcm.py:81:0: C0304: Final newline missing (missing-final-newline)
************* Module plot_operations
plot_operations.py:36:0: C0301: Line too long (101/100) (line-too-long)
plot_operations.py:38:0: C0301: Line too long (115/100) (line-too-long)
plot_operations.py:40:0: C0301: Line too long (124/100) (line-too-long)
plot_operations.py:41:0: C0301: Line too long (115/100) (line-too-long)
plot_operations.py:51:0: C0301: Line too long (103/100) (line-too-long)
plot_operations.py:62:0: C0301: Line too long (116/100) (line-too-long)
plot_operations.py:73:0: C0301: Line too long (120/100) (line-too-long)
plot_operations.py:82:0: C0301: Line too long (109/100) (line-too-long)
plot_operations.py:91:0: C0301: Line too long (101/100) (line-too-long)
plot_operations.py:93:0: C0304: Final newline missing (missing-final-newline)
plot_operations.py:11:0: E0401: Unable to import 'matplotlib.pyplot' (import-error)
************* Module prod_util
prod_util.py:43:0: C0301: Line too long (155/100) (line-too-long)
prod_util.py:50:0: C0303: Trailing whitespace (trailing-whitespace)
prod_util.py:54:0: C0301: Line too long (115/100) (line-too-long)
prod_util.py:69:0: C0305: Trailing newlines (trailing-newlines)

-----------------------------------
Your code has been rated at 8.19/10
>>>>>>> 1a34288dbee26ff68c9996da2b45bad0589e4f24
=======
Your code has been rated at 6.29/10
>>>>>>> 0759e1a58ab7fd61e887daeb2a19c2adce892925

