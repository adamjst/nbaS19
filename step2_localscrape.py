# Import libraries
import pandas as pd
import re
from bs4 import BeautifulSoup
from pathlib import Path

"""Scrape local html file and return in html and formatted csv"""

def step2_scrape(year_start, years_back, stage):
    """Scrape local html file for regular season data and return in html and csv in separate output folders"""
    counter = 0
    leagues = ['NBA', 'ABA', 'BAA']
    mths = ['october', 'november', 'december', 'january', 'february', 'march', 'april']
    yrs = []
    yrs.append(year_start)
    for i in range(years_back):
        yrs.append(yrs[i] - 1)
    for league in leagues:
        for yr in yrs:
            for mth in mths:
                ##Assign local path, URL

                if stage == 'Playoffs':
                    # Create relative path
                    step1_html = Path('data', 'html', '{}_{}_playoffs_step1.html'.format(league, yr), header=True)
                    step2_csv = Path('data', 'csv', '{}_{}_playoffs_step2.csv'.format(league, yr), header=True)

                else:
                    step1_html = Path('data', 'html', '{}_{}_{}_step1.html'.format(league, yr, mth), header=True)
                    step2_csv = Path('data', 'csv', '{}_{}_{}_step2.csv'.format(league, yr, mth), header=True)

                #print(yr, mth)

                #print(step1_html)
                counter += (100 / (74 * 3 * 9))
                page_url = open(step1_html)
                #Apply Beautiful Soup to determine columns of new table##
                soup = BeautifulSoup(page_url, "html.parser")

                #print(soup.prettify())
                    ##extract table
                table = soup.find('tbody')

                # if this month is empty or the page is wrong
                if not table:
                    continue

                ###TRIED STARTING ALIGNMENT OF COLUMNS HERE###
                cols = table.find_all('tr')[0]

                header = []
                for col in cols.find_all('th'):
                      header.append(col.get_text())
                print(header)


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
                round = ['regular'] * 250
                prog = re.compile('[a-zA-z].+')
                Year = []
                Month = []


                ## Find and extract relevant data point and then append under appropriate column. For Box Score, extract underlying hyperlink ##

                for row in table.find_all('tr'):
                    dat = row.find('th')
                    #print(dat)
                    if stage != 'Playoffs':
                        if dat.get_text() == 'Playoffs':
                            break
                        else:
                            pass
                    dat2 = dat.find('a')
                    date.append(dat2.get_text())
                    #print(date)
                    sta = row.find_all('td')[0]
                    start.append(sta.get_text())
                    #print(start)
                    vis = row.find_all('td')[1]
                    visitor.append(str(vis.get_text()))
                    #print(visitor)
                    pv = row.find_all('td')[2]
                    ptsv.append(pv.get_text())
                    #print(ptsv)
                    ho = row.find_all('td')[3]
                    home.append(str(ho.get_text()))
                    #print(home)
                    ph = row.find_all('td')[4]
                    ptsh.append(ph.get_text())
                    #print(ptsh)
                    #pg = row.find_all('td')[5]
                    #a = pg.find('a')
                    #print(a.attrs)
                    ##Based on my extraction code at step 1, I seem to have problems here at Step 2 when trying to
                    # extract the URL (href) of the BoxScore column. Maybe a regex to extract the third dictionary key?
                    #short_html = html.split('"')[0]
                    #print(short_html)
                    box.append(short_url)  ##Instead, I just put the url from the boxscore
                    #print(box)
                    over = row.find_all('td')[6]
                    ot.append(over.get_text())
                    at = row.find_all('td')[7]
                    attend.append(at.get_text())
                    #print(attend)
                    df = pd.DataFrame(list(zip(date, start, visitor, ptsv, home, ptsh, box, ot, attend, round, Year, Month)))
                    print(df)

                    #print(df)

                    ### STILL WORKING ON ALIGNING COLUMNS IN DATA FRAME##

                    # if prog.match(row['start']):
                    #      # if correct match, insert the match into the new column
                    #      visitor.append(str(sta.get_text()))
                    #      ptsv.append(pv.get_text())
                    #      home.append(str(ho.get_text()))
                    #      ptsh.append(ph.get_text())
                    #      start = []
                    # else:
                    #      # if no match, insert filler string into new column
                    #      pass

                    df.columns = ['date','start','visitor','visitor.pts','home','home.pts','boxscore', 'ot','attend', 'round', 'Year', 'Month']

                    ####STILL WORKING ON DATETIME SPLITTING####


                    # df['date'] = pd.to_datetime(df['date'])
                    # df['Year'] = df['date'].dt.year
                    # df['Month'] = df['date'].dt.month

                    ##Convert to datetime


                    df.to_csv((step2_csv), header=True)

step2_scrape(2019, 73, 'Regular')
step2_scrape(2019, 73, 'Playoffs')

