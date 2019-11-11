# Import libraries
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path

"""Scrape local html file and return in html and formatted csv"""

def regular_scrape(year_start, years_back):
    """Scrape local html file for regular season data and return in html and csv in separate output folders"""
    counter = 0
    leagues = ['NBA', 'ABA', 'BAA']
    mths = ['october', 'november', 'december', 'january', 'february', 'march']
    yrs = []
    yrs.append(year_start)
    for i in range(years_back):
        yrs.append(yrs[i] - 1)
    for league in leagues:
        for yr in yrs:
            for mth in mths:
                ##Assign local path, URL
                print(yr, mth)
                html_folder = Path('data', 'html', '{}_{}_{}.html'.format(league, yr, mth), header=True)

                outputs = Path('data', 'outputs', '{}_{}_{}_processed.csv'.format(league, yr, mth), header=True)
                #print(html_folder)
                counter += (100 / (74 * 3 * 9))
                page_url = open(html_folder)
                #Apply Beautiful Soup to determine columns of new table##
                soup = BeautifulSoup(page_url, "html.parser")

                #print(soup.prettify())
                    ##extract table
                table = soup.find('tbody')

                # if this month is empty or the page is wrong
                if not table:
                    continue


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


                ## Find and extract relevant data point and then append under appropriate column. For Box Score, extract underlying hyperlink ##

                for row in table.find_all('tr'):
                    dat = row.find('th')
                    #print(dat)
                    if dat.get_text() == 'Playoffs':
                        break
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
                    df = pd.DataFrame(list(zip(date, start, visitor, ptsv, home, ptsh, box, ot, attend, round)))

                    #print(df)
                    df.columns = ['date','start','visitor','visitor.pts','home','home.pts','boxscore','ot','attend', 'round']

                    df.to_csv((outputs), header=True)
                #print(yr, mth)

def april_scrape(year_start, years_back):
    """Scrape local html file for April (a mixed-regular season/playoff month) and return in html and formatted csv"""
    counter = 0
    leagues = ['NBA', 'ABA', 'BAA']
    mths = ['april']
    yrs = []
    yrs.append(year_start)
    for i in range(years_back):
        yrs.append(yrs[i] - 1)
    for league in leagues:
        for yr in yrs:
            for mth in mths:
                ##Assign local path, URL
                # print(year, month)
                html_folder = Path('data', 'html', '{}_{}_{}.html'.format(league, yr, mth), header=True)

                outputs = Path('data', 'outputs', '{}_{}_{}_processed.csv'.format(league, yr, mth), header=True)
                #print(html_folder)
                counter += (100 / (74 * 3 * 9))
                page_url = open(html_folder)
                #Apply Beautiful Soup to determine columns of new table##
                soup = BeautifulSoup(page_url, "html.parser")
                #print(soup.prettify())

                table = soup.find('tbody')

                # if this month is empty or the page is wrong
                if not table:
                    continue



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
                short_url ='https://www.basketball-reference.com/boxscores/'
                round = ['regular'] * 250


                ## Find and extract relevant data point and then append under appropriate column. For Box Score, extract underlying hyperlink ##

                for row in table.find_all('tr'):
                    dat = row.find('th')
                    #print(dat)
                    if dat.get_text() == 'Playoffs':
                        break
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
                    #print(a)
                    #if a.attrs is True:
                     #   pass
                    #else:
                        #continue
                    #html = list(a.attrs)[2]
                    #print(html)
                    #short_html = html.split('"')[0]
                    #print(short_html)
                    box.append(short_url)
                    #print(box)
                    over = row.find_all('td')[6]
                    ot.append(over.get_text())
                    at = row.find_all('td')[7]
                    attend.append(at.get_text())
                    #print(attend)
                    df = pd.DataFrame(list(zip(date, start, visitor, ptsv, home, ptsh, box, ot, attend, round)))

                    #print(df)
                    df.columns = ['date','start','visitor','visitor.pts','home','home.pts','boxscore','ot','attend', 'round']

##source: https://medium.com/@rtjeannier/pandas-101-cont-9d061cb73bfc
## Assign to CSV written to specific month and year.
                    # print(df)
                    df.to_csv((outputs), header=True)


def playoff_local_scrape(year_start, years_back):
    """Scrape local html file for playoff data and return in html and formatted csv"""
    counter = 0
    leagues = ['NBA', 'ABA', 'BAA']
    yrs = []
    yrs.append(year_start)
    for i in range(years_back):
        yrs.append(yrs[i] - 1)
    for league in leagues:
        for yr in yrs:
                ##Assign local path, URL
                # print(year, month)
                html_folder = Path('data', 'html', '{}_{}_playoffs.html'.format(league, yr), header=True)

                outputs = Path('data', 'outputs', '{}_{}_playoffs_processed.csv'.format(league, yr), header=True)
                #print(html_folder)
                counter += (100 / (74 * 3 * 9))
                page_url = open(html_folder)
                #Apply Beautiful Soup to determine columns of new table##
                soup = BeautifulSoup(page_url, "html.parser")
                #print(soup.prettify())

                table = soup.find('tbody')

                # if this month is empty or the page is wrong
                if not table:
                    continue



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
                round = ['playoffs'] * 250


                ## Find and extract relevant data point and then append under appropriate column. For Box Score, extract underlying hyperlink ##

                for row in table.find_all('tr'):
                    dat = row.find('th')
                    #print(dat)
                    if dat.get_text() == 'Playoffs':
                        break
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
                    pg = row.find_all('td')[5]
                    a = pg.find('a')
                    box.append(short_url + a.attrs['href'])
                    #print(a)
                    #if a.attrs is True:
                     #   pass
                    #else:
                        #continue
                    #html = list(a.attrs)[2]
                    #print(html)
                    #short_html = html.split('"')[0]
                    #print(short_html)
                    #box.append(short_url)
                    #print(box)
                    over = row.find_all('td')[6]
                    ot.append(over.get_text())
                    #print(ot)
                    at = row.find_all('td')[7]
                    attend.append(at.get_text())
                    #print(attend)
                    df = pd.DataFrame(list(zip(date, start, visitor, ptsv, home, ptsh, box, ot, attend, round)))

                    #print(df)
                    df.columns = ['date','start','visitor','visitor.pts','home','home.pts','boxscore','ot','attend', 'round']

                    df.to_csv((outputs), header=True)

regular_scrape(2019, 3)
playoff_local_scrape(2019, 3)
april_scrape(2019, 3)
