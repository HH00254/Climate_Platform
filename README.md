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
db_operations.py:139:0: C0301: Line too long (107/100) (line-too-long)
db_operations.py:165:32: C0303: Trailing whitespace (trailing-whitespace)
db_operations.py:241:0: C0304: Final newline missing (missing-final-newline)
************* Module weather_processor
weather_processor.py:163:0: C0304: Final newline missing (missing-final-newline)
************* Module scrape_weather
scrape_weather.py:34:43: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:37:146: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:81:0: C0301: Line too long (114/100) (line-too-long)
scrape_weather.py:183:35: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:205:45: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:283:0: C0304: Final newline missing (missing-final-newline)
scrape_weather.py:11:0: E0401: Unable to import 'lxml' (import-error)
scrape_weather.py:12:0: E0401: Unable to import 'dateutil.relativedelta' (import-error)
scrape_weather.py:13:0: E0401: Unable to import 'requests' (import-error)
scrape_weather.py:217:4: R0914: Too many local variables (16/15) (too-many-locals)
************* Module dbcm
dbcm.py:81:0: C0304: Final newline missing (missing-final-newline)
************* Module plot_operations
plot_operations.py:38:0: C0301: Line too long (154/100) (line-too-long)
plot_operations.py:43:0: C0301: Line too long (112/100) (line-too-long)
plot_operations.py:69:0: C0301: Line too long (102/100) (line-too-long)
plot_operations.py:81:0: C0301: Line too long (118/100) (line-too-long)
plot_operations.py:90:0: C0301: Line too long (113/100) (line-too-long)
plot_operations.py:99:0: C0301: Line too long (105/100) (line-too-long)
plot_operations.py:110:0: C0304: Final newline missing (missing-final-newline)
plot_operations.py:11:0: E0401: Unable to import 'matplotlib.pyplot' (import-error)
plot_operations.py:11:0: C0411: third party import "matplotlib.pyplot" should be placed before first party import "prod_util.ProdUtil"  (wrong-import-order)
************* Module prod_util
prod_util.py:57:0: C0301: Line too long (115/100) (line-too-long)

-----------------------------------
Your code has been rated at 8.95/10

