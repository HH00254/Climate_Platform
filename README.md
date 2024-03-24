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
scrape_weather.py:34:48: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:48:0: C0303: Trailing whitespace (trailing-whitespace)
scrape_weather.py:64:0: C0301: Line too long (166/100) (line-too-long)
scrape_weather.py:86:0: C0304: Final newline missing (missing-final-newline)
scrape_weather.py:9:0: E0401: Unable to import 'requests' (import-error)
scrape_weather.py:10:0: E0401: Unable to import 'lxml' (import-error)
scrape_weather.py:29:40: C0121: Comparison 'location_element[0] == None' should be 'location_element[0] is None' (singleton-comparison)
scrape_weather.py:52:0: C0116: Missing function or method docstring (missing-function-docstring)
scrape_weather.py:11:0: C0411: standard import "datetime.datetime" should be placed before third party imports "requests", "lxml.html" (wrong-import-order)
scrape_weather.py:12:0: C0411: standard import "pprint.pprint" should be placed before third party imports "requests", "lxml.html" (wrong-import-order)
************* Module db_operations
db_operations.py:16:0: C0304: Final newline missing (missing-final-newline)
db_operations.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
db_operations.py:15:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module plot_operations
plot_operations.py:8:0: C0304: Final newline missing (missing-final-newline)
plot_operations.py:8:0: C0304: Final newline missing (missing-final-newline)
************* Module weather_processor
weather_processor.py:8:0: C0304: Final newline missing (missing-final-newline)
weather_processor.py:8:0: C0304: Final newline missing (missing-final-newline)

-----------------------------------
Your code has been rated at 3.75/10

