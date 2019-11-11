# Import libraries
import requests
from pathlib import Path
from bs4 import BeautifulSoup

"""Scrape regular season and playoff game summary data from basketball reference and convert it to a raw html output."""


headers = {'User-Agent': 'Adam Sawyer', 'From': 'ajsawyer@syr.edu'}
##Source
##https://urllib3.readthedocs.io/en/latest/user-guide.html



##Set the nested loop
def rs_scrape(year_start, years_back):
    """Scrape regular season game summary data and save it to a local folder in raw html form."""
    ##Set three parameters for loop: league, year, and month
    leagues = ['NBA', 'ABA', 'BAA']
    years = []
    #April,May, and June are excluded. April scaper accounts for April. May and June accounted for under playoffs.
    months = ['october', 'november', 'december', 'january', 'february', 'march', 'april']
    years.append(year_start)
    for i in range(years_back):
        years.append(years[i] - 1)
    for league in leagues:
        for year in years:
            for month in months:
                # Create relative path
                html_folder = Path('data', 'html', '{}_{}_{}.html'.format(league, year, month), header=True)

                ##Assign path, URL, and then apply Beautiful Soup
                url = 'https://www.basketball-reference.com/leagues/{}_{}_games-{}.html'.format(league, year, month)
                    ##Acquire text from url
                page_url = requests.get(url).text.encode('utf-8')
                str_html = str(page_url)
                open( html_folder, 'w').write( str_html )


##Set the nested loop
def playoff_scrape(year_start, years_back):
    """Scrape regular season game summary data and save it to a local folder in raw html form."""

    ##Set three parameters for loop: league, year, and month
    leagues = ['NBA', 'ABA', 'BAA']
    years = []
    years.append(year_start)
    for i in range(years_back):
        years.append(years[i] - 1)
    for league in leagues:
        for year in years:
                # Create relative path
                html_folder = Path('data', 'html', '{}_{}_playoffs.html'.format(league, year), header=True)

                ##Assign path, URL, and then apply Beautiful Soup
                url = 'https://www.basketball-reference.com/playoffs/{}_{}_games.html'.format(league, year)
                page_url = requests.get(url).text.encode('utf-8')
                str_html = str(page_url)
                open( html_folder, 'w').write( str_html )

                print (league, year)#page_url.to_html(html_folder)ba
rs_scrape(2019, 73)
playoff_scrape(2019, 73)


