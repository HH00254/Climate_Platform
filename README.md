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
scrape_weather.py:130:0: C0301: Line too long (106/100) (line-too-long)
scrape_weather.py:138:0: C0301: Line too long (115/100) (line-too-long)
scrape_weather.py:178:0: C0301: Line too long (164/100) (line-too-long)
scrape_weather.py:219:0: C0304: Final newline missing (missing-final-newline)
scrape_weather.py:14:0: E0401: Unable to import 'requests' (import-error)
scrape_weather.py:15:0: E0401: Unable to import 'lxml' (import-error)
scrape_weather.py:16:0: E0401: Unable to import 'dateutil.relativedelta' (import-error)
scrape_weather.py:33:40: C0121: Comparison 'location_element[0] == None' should be 'location_element[0] is None' (singleton-comparison)
scrape_weather.py:154:0: R0914: Too many local variables (16/15) (too-many-locals)
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
main.py:41:0: W0311: Bad indentation. Found 10 spaces, expected 12 (bad-indentation)
main.py:42:0: W0311: Bad indentation. Found 10 spaces, expected 12 (bad-indentation)
main.py:47:0: C0304: Final newline missing (missing-final-newline)
************* Module db_operations
db_operations.py:72:0: C0301: Line too long (153/100) (line-too-long)
db_operations.py:89:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
************* Module plot_operations
plot_operations.py:8:0: C0304: Final newline missing (missing-final-newline)
plot_operations.py:8:0: C0304: Final newline missing (missing-final-newline)
************* Module test
test.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module weather_processor
weather_processor.py:1:0: R0801: Similar lines in 2 files
==_scrape_weather:[62:82]
==scrape_weather:[124:166]
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
==scrape_weather:[44:55]
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
==scrape_weather:[30:41]
    for location_element in location_payload:
        if location_element[0] == '' or location_element[0] == None:
            location_element = 'NULL'

    insert_args = []
    index = 0
    while index < len(list_data):

        try: (duplicate-code)
weather_processor.py:1:0: R0801: Similar lines in 2 files
==_scrape_weather:[97:106]
==scrape_weather:[187:195]
                city_path     = '//main/div/p/text()'
                province_path = '//main/div/br/text()'
                location_payload = tree.xpath(f"{city_path} | {province_path}")

                date_path      = '//table/tbody/tr[position()< last() -3]/th/abbr/@title'
                temperature_path = '//tr[position()< last() -3]/td[position()<4]/text()'
                table_load = tree.xpath(f"{date_path} | {temperature_path}")
 (duplicate-code)

-----------------------------------
Your code has been rated at 7.75/10

