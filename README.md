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
************* Module db_operations
db_operations.py:20:9: E0001: Parsing failed: 'invalid decimal literal (db_operations, line 20)' (syntax-error)
************* Module weather_processor
weather_processor.py:54:24: E0001: Parsing failed: 'unterminated string literal (detected at line 54) (weather_processor, line 54)' (syntax-error)
************* Module scrape_weather
scrape_weather.py:163:9: E0001: Parsing failed: 'invalid decimal literal (scrape_weather, line 163)' (syntax-error)
************* Module dbcm
dbcm.py:18:9: E0001: Parsing failed: 'invalid decimal literal (dbcm, line 18)' (syntax-error)
************* Module plot_operations
plot_operations.py:81:9: E0001: Parsing failed: 'unterminated triple-quoted string literal (detected at line 115) (plot_operations, line 81)' (syntax-error)
************* Module _main
_main.py:10:0: E0001: Cannot import 'db_operations' due to 'invalid decimal literal (db_operations, line 20)' (syntax-error)
************* Module _scrape_weather
_scrape_weather.py:92:0: C0301: Line too long (164/100) (line-too-long)
_scrape_weather.py:126:0: C0304: Final newline missing (missing-final-newline)
_scrape_weather.py:12:0: E0401: Unable to import 'requests' (import-error)
_scrape_weather.py:13:0: E0401: Unable to import 'lxml' (import-error)
_scrape_weather.py:14:0: E0401: Unable to import 'dateutil.relativedelta' (import-error)
_scrape_weather.py:15:0: E0001: Cannot import 'db_operations' due to 'invalid decimal literal (db_operations, line 20)' (syntax-error)
_scrape_weather.py:31:40: C0121: Comparison 'location_element[0] == None' should be 'location_element[0] is None' (singleton-comparison)
_scrape_weather.py:62:0: C0116: Missing function or method docstring (missing-function-docstring)
_scrape_weather.py:65:0: C0116: Missing function or method docstring (missing-function-docstring)
_scrape_weather.py:78:0: R0914: Too many local variables (16/15) (too-many-locals)
************* Module test
test.py:1:0: C0114: Missing module docstring (missing-module-docstring)
test.py:1:0: E0001: Cannot import 'db_operations' due to 'invalid decimal literal (db_operations, line 20)' (syntax-error)
************* Module main
main.py:21:0: C0304: Final newline missing (missing-final-newline)
main.py:1:0: C0114: Missing module docstring (missing-module-docstring)
main.py:1:0: E0001: Cannot import 'db_operations' due to 'invalid decimal literal (db_operations, line 20)' (syntax-error)
main.py:2:0: E0001: Cannot import 'scrape_weather' due to 'invalid decimal literal (scrape_weather, line 163)' (syntax-error)
main.py:3:0: C0411: standard import "pprint.pprint" should be placed before first party imports "db_operations.DBOperations", "scrape_weather"  (wrong-import-order)
main.py:4:0: C0411: standard import "time.time" should be placed before first party imports "db_operations.DBOperations", "scrape_weather"  (wrong-import-order)
main.py:3:0: W0611: Unused pprint imported from pprint (unused-import)
main.py:4:0: W0611: Unused time imported from time (unused-import)
************* Module prod_util
prod_util.py:43:0: C0301: Line too long (155/100) (line-too-long)
prod_util.py:50:0: C0303: Trailing whitespace (trailing-whitespace)
prod_util.py:54:0: C0301: Line too long (115/100) (line-too-long)
prod_util.py:69:0: C0305: Trailing newlines (trailing-newlines)

-----------------------------------
Your code has been rated at 2.26/10

