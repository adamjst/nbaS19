# Import libraries
import requests
import pandas as pd
from pathlib import Path
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Adam Sawyer', 'From': 'ajsawyer@syr.edu'}
##Source
##https://urllib3.readthedocs.io/en/latest/user-guide.html



##Set the nested loop
def rs_scrape():
    ##Set counter to determine progress
    counter = 0
    ##Set three parameters for loop: league, year, and month
    leagues = ['NBA', 'ABA', 'BAA']
    years = []
    #April,May, and June are excluded. April scaper accounts for April. May and June accounted for under playoffs.
    months = ['october', 'november', 'december', 'january', 'february', 'march']
    years.append(2019)
    for i in range(73):
        years.append(years[i] - 1)
    for league in leagues:
        for year in years:
            for month in months:
                # Create relative path
                html_folder = Path(r'data\html\{}_{}_{}.html'.format(league, year, month), header=True)
                csv_folder = Path(r'data\{}_{}_{}.csv'.format(league, year, month), header=True)

                ##Assign path, URL, and then apply Beautiful Soup
                url = 'https://www.basketball-reference.com/leagues/{}_{}_games-{}.html'.format(league, year, month)

                    ##Acquire text from url
                page_url = requests.get(url).text
                    #print(league, month, year, counter)
                soup = BeautifulSoup(page_url, "html.parser")
                #print(soup.prettify())

                    ##extract table
                table = soup.find('tbody')

                df = pd.DataFrame(table)
                df2 = df.iloc[1::2]

                if df2.empty is True:
                    continue

                print(df)

                ## Assign as local html file written to specific league, month, and year.
                df2.to_csv(csv_folder)
                df2.to_html(html_folder)


##Set the nested loop
def playoff_scrape():
    ##Set counter to determine progress
    counter = 0
    ##Set three parameters for loop: league, year, and month
    leagues = ['NBA', 'ABA', 'BAA']
    years = []
    years.append(2019)
    for i in range(73):
        years.append(years[i] - 1)
    for league in leagues:
        for year in years:
                # Create relative path
                html_folder = Path(r'data\html\{}_{}_playoffs.html'.format(league, year), header=True)
                csv_folder = Path(r'data\{}_{}_playoffs.csv'.format(league, year), header=True)

                ##Assign path, URL, and then apply Beautiful Soup
                url = 'https://www.basketball-reference.com/playoffs/{}_{}_games.html'.format(league, year)

                    ##Acquire text from url
                page_url = requests.get(url).text
                    #print(league, month, year, counter)
                soup = BeautifulSoup(page_url, "html.parser")
                #print(soup.prettify())

                    ##extract table
                table = soup.find('tbody')

                ##convert to dataframe
                df = pd.DataFrame(table)
                df2 = df.iloc[1::2]

                if df2.empty is True:
                    continue

                #print(df)

                ## Assign as local html file written to specific league, month, and year. ##THIS WILL NEED TO BE ADJUSTED TO YOUR LOCAL PATH##
                df2.to_csv(csv_folder)
                df2.to_html(html_folder)




rs_scrape()
playoff_scrape()

