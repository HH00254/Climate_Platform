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
db_operations.py:86:0: C0303: Trailing whitespace (trailing-whitespace)
db_operations.py:135:0: C0301: Line too long (107/100) (line-too-long)
db_operations.py:178:0: C0301: Line too long (198/100) (line-too-long)
db_operations.py:199:0: C0301: Line too long (196/100) (line-too-long)
db_operations.py:212:0: C0303: Trailing whitespace (trailing-whitespace)
db_operations.py:216:0: C0304: Final newline missing (missing-final-newline)
************* Module weather_processor
weather_processor.py:31:0: C0303: Trailing whitespace (trailing-whitespace)
weather_processor.py:82:113: C0303: Trailing whitespace (trailing-whitespace)
weather_processor.py:82:0: C0301: Line too long (113/100) (line-too-long)
weather_processor.py:84:0: C0301: Line too long (117/100) (line-too-long)
weather_processor.py:85:0: C0301: Line too long (127/100) (line-too-long)
weather_processor.py:92:0: C0303: Trailing whitespace (trailing-whitespace)
weather_processor.py:95:0: C0303: Trailing whitespace (trailing-whitespace)
weather_processor.py:125:0: C0303: Trailing whitespace (trailing-whitespace)
weather_processor.py:164:0: C0304: Final newline missing (missing-final-newline)
weather_processor.py:16:0: C0411: standard import "asyncio" should be placed before first party imports "db_operations.DBOperations", "scrape_weather.ScrapeWeather"  (wrong-import-order)
weather_processor.py:16:0: W0611: Unused import asyncio (unused-import)
weather_processor.py:19:0: W0611: Unused import _scrape_weather (unused-import)
************* Module _scrape_weather
_scrape_weather.py:186:0: C0304: Final newline missing (missing-final-newline)
_scrape_weather.py:11:0: E0401: Unable to import 'requests' (import-error)
_scrape_weather.py:12:0: E0401: Unable to import 'lxml' (import-error)
_scrape_weather.py:13:0: E0401: Unable to import 'dateutil.relativedelta' (import-error)
_scrape_weather.py:94:0: R0914: Too many local variables (16/15) (too-many-locals)
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
Your code has been rated at 8.09/10

