# Import libraries
import requests
from pathlib import Path


"""Scrape regular season and playoff game summary data from basketball reference and convert it to a raw html output."""


headers = {'User-Agent': 'Adam Sawyer', 'From': 'ajsawyer@syr.edu'}
##Source
##https://urllib3.readthedocs.io/en/latest/user-guide.html



##Set the nested loop
def step1_scrape(year_start, years_back, stage):
    """Scrape regular season game summary data and save it to a local folder in raw html form."""
    ##Set three parameters for loop: league, year, and month
    leagues = ['NBA', 'ABA', 'BAA']
    years = []
    #May and June accounted for under playoffs.
    months = ['october', 'november', 'december', 'january', 'february', 'march', 'april']
    years.append(year_start)
    for i in range(years_back):
        years.append(years[i] - 1)
    for league in leagues:
        for year in years:
            for month in months:
                ##Differentiates inputs by playoffs compared to regular season
                if stage == 'playoffs':
                    # Create relative path
                    step1_html = Path('data', 'html', '{}_{}_playoffs_step1.html'.format(league, year), header=True)
                    url = 'https://www.basketball-reference.com/playoffs/{}_{}_games.html'.format(league, year)


                else:
                    step1_html = Path('data', 'html', '{}_{}_{}_step1.html'.format(league, year, month), header=True)
                    url = 'https://www.basketball-reference.com/leagues/{}_{}_games-{}.html'.format(league, year, month)

                ##Acquire text from url
                page_url = requests.get(url).text.encode('utf-8')
                str_html = str(page_url)
                open( step1_html, 'w').write( str_html )
                print(league, year, month)

#Run function for both regular season and playoffs
step1_scrape(2019, 73, 'regular')
step1_scrape(2019, 73, 'playoffs')


