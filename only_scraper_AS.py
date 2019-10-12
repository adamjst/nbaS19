# Import libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Adam Sawyer', 'From': 'ajsawyer@syr.edu'}
##Source
##https://urllib3.readthedocs.io/en/latest/user-guide.html

##Set three parameters for loop: league, year, and month
leagues = ['NBA','ABA','BAA']
years = []
months = ['june', 'may', 'april', 'march','february', 'january', 'december', 'november', 'october']
years.append(2019)
for i in range(73):
    years.append(years[i] - 1)


##Set the nested loop
def scrape():
    ##Set counter to determine progress
    counter = 0
    for league in leagues:
        for year in years:
            for month in months:
                try:

                ##Assign path, URL, and then apply Beautiful Soup
                    url = 'https://www.basketball-reference.com/leagues/{}_{}_games-{}.html'.format(league, year, month)

                    ##Acquire text from url
                    page_url = requests.get(url).text
                    #print(league, month, year, counter)
                    soup = BeautifulSoup(page_url, "html.parser")
                    #print(soup.prettify())

                    ##extract table
                    table = soup.find('table', {'class': 'suppress_glossary'})
                    ##convert to dataframe
                    df = pd.DataFrame(table)
                    #print(df)

                ## Assign as local html file written to specific league, month, and year. ##THIS WILL NEED TO BE ADJUSTED TO YOUR LOCAL PATH##
                    df.to_html(r"C:\Users\adamj\OneDrive\Documents\Writings\Work.w.Seth\pureHTML\{}_{}_{}.html".format(league, year, month), header=True)
                ##Show progress of code. 73 years, 3 leagues and nine months
                    counter += (100 / (73 * 3 * 9))
                except:
                    continue
scrape()