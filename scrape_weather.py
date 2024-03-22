"""
Description: Weather Processing App Group 9
Author: Lance Fuentes, Al Hochbaum, Christian Requerme
Section Number: FTO01
Date Created: 03/20/24
Credit:
Updates:
Test
Todo:   1. Create dictionaries for output.. 
                ex. daily_temps = {“Max”: 12.0, “Min”: 5.6, “Mean”: 7.1}
                    weather = {“2018-06-01”: daily_temps, “2018-06-02”: daily_temps}
        2. Scrape through up to current date and back in time until no data
        3. location
"""


from html.parser import HTMLParser
import urllib.request

class WeatherScraper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.td = False
        self.abbr = False
        self.p = False
        self.p_count = 0
        self.stop = False
        self.abbr_title = ""
        self.location = ""
        self.td_count = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'abbr':
            for attr in attrs:
                if attr[0] == 'title':
                    self.abbr_title = attr[1]
                    break
            self.abbr = True
        elif tag == 'td' and self.td_count < 3:
            self.td = True
        elif tag == 'p' and self.p_count < 2:
            self.p = True

    def handle_data(self, data):
        if self.td and self.td_count < 3 and any(char.isdigit() for char in self.abbr_title):
            print(self.abbr_title, data.strip())
        if self.p and self.p_count < 2:
            print(data)
            self.p_count += 1

    def handle_endtag(self, tag):
        if tag == 'abbr':
            self.abbr = False
        elif tag == 'td' and self.td:
            self.td = False
            self.td_count += 1
        elif tag == "tr":
            self.td_count = 0
            self.abbr_title = ''
        elif tag == 'p':
            self.p = False

# Create an instance of WeatherScraper
parser = WeatherScraper()

# Fetch the HTML content from the URL
url = "https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year=2007&Month=5#"
with urllib.request.urlopen(url) as response:
    html = str(response.read())

# Parse the HTML content
parser.feed(html)
