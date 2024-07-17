# Railway Selenium Automation Project
## Overview
This project is aimed at automating tests for the Railway application using Selenium WebDriver with Python. It includes automated tests for various functionalities like user registration, booking tickets, canceling tickets, and checking ticket prices.

## Prerequisites
Before running the tests, ensure you have the following installed:
- Python (3.x recommended)
- PyCharm or any Python IDE
- WebDriver for your preferred browser (Chrome, Firefox, etc.)
- Selenium WebDriver library (pip install selenium)
- Required browser drivers (ChromeDriver, GeckoDriver) available in PATH or explicitly set
## Project Structure
The project is structured as follows:
- data/: Contains test data in JSON format.
- enums/: Enums for various constants used in tests.
- models/: Defines data models like User.
- pages/: Page Object Model (POM) classes representing web pages.
- utils/: Utility classes for actions like Action handling WebDriver operations.
- Test scripts organized by functionality.

## Run test
 - python main.py --type=remote --browser=chrome
 - python main.py --type=remote --browser=firefox
 - python main.py --type=local --browser=chrome
 - python main.py --type=local --browser=firefox


