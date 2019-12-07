# Import libraries
import pandas as pd
import re
from bs4 import BeautifulSoup
from pathlib import Path

"""Scrape local html file and return in html and formatted csv"""


def step2_scrape(league, year_start, years_back, stage):
    """Scrape local html file for regular season data and return in html and csv in separate output folders"""
    mths = ['october', 'november', 'december', 'january', 'february', 'march', 'april']
    yrs = []
    yrs.append(year_start)
    for i in range(years_back):
        yrs.append(yrs[i] - 1)
    for yr in yrs:
        for mth in mths:
            ##Assign local path, URL
            print(league, yr, mth)
            if stage == 'Playoffs':
                # Create relative path
                step1_html = Path('data', 'html', '{}_{}_playoffs_step1.html'.format(league, yr), header=True)
                step2_csv = Path('data', 'csv', '{}_{}_playoffs_step2.csv'.format(league, yr), header=True)

            else:
                step1_html = Path('data', 'html', '{}_{}_{}_step1.html'.format(league, yr, mth), header=True)
                step2_csv = Path('data', 'csv', '{}_{}_{}_step2.csv'.format(league, yr, mth), header=True)

            # open local-saved html file
            page_url = open(step1_html)

            # Apply Beautiful Soup to determine columns of new table##
            soup = BeautifulSoup(page_url, "html.parser")

            # extract header and table body
            first_row = soup.find('thead')

            # Check to ensure the page is not empty
            if first_row is None:
                continue
            # Find table text
            table = soup.find('tbody')

            # Find/save header text
            head = first_row.find('tr')
            cols = head.find_all('th')
            header = []
            for col in cols:
                header.append(col.get_text())
            # print(header)
            # print(len(header))

            ## Create boxes for each data point for scraping ##
            date = []
            start = []
            visitor = []
            ptsv = []
            home = []
            ptsh = []
            box = []
            ot = []
            attend = []
            short_url = 'https://www.basketball-reference.com/boxscores/'
            round = [stage] * 250

            ## Find and extract relevant data point and then append under appropriate column. For Box Score, extract underlying hyperlink ##
            for row in table.find_all('tr'):
                dat = row.find('th')
                # print(dat)
                if stage != 'Playoffs':
                    if dat.get_text() == 'Playoffs':
                        break
                    else:
                        pass
                dat2 = dat.find('a')
                date.append(dat2.get_text())
                # print(date)
                sta = row.find_all('td')[0]
                start.append(sta.get_text())
                # print(start)
                vis = row.find_all('td')[1]
                visitor.append(str(vis.get_text()))
                # print(visitor)
                pv = row.find_all('td')[2]
                ptsv.append(pv.get_text())
                # print(ptsv)
                ho = row.find_all('td')[3]
                home.append(str(ho.get_text()))
                # print(home)
                ph = row.find_all('td')[4]
                ptsh.append(ph.get_text())
                box.append(short_url)  ##Instead, I just put the url from the boxscore
                # print(box)
                over = row.find_all('td')[6]
                ot.append(over.get_text())
                at = row.find_all('td')[7]
                attend.append(at.get_text())

                if len(header) == 10:
                    df = pd.DataFrame(list(zip(date, start, visitor, ptsv, home, ptsh, box, ot, attend, round)),
                                      columns=header)
                else:
                    df = pd.DataFrame(list(zip(date, start, visitor, ptsv, home, ptsh, box, ot, attend)),
                                      columns=header)
                # print(df)

                # Split_date
                df['Date'] = pd.to_datetime(df['Date'])
                df['Year'] = df['Date'].dt.year
                df['Month'] = df['Date'].dt.month

                # prevent writing of file if empty
                if len(df.columns) == 0:
                    continue

                # write file
                df.to_csv((step2_csv), header=True)


# Run for each league during league's years of operation
step2_scrape('NBA', 2019, 71, 'Regular')
step2_scrape('ABA', 1976, 10, 'Regular')
step2_scrape('BAA', 1949, 4, 'Regular')
step2_scrape('NBA', 2019, 71, 'Playoffs')
step2_scrape('ABA', 1976, 10, 'Playoffs')
step2_scrape('BAA', 1949, 4, 'Playoffs')
