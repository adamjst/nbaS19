# Import libraries
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path

def regular_scrape():
    counter = 0
    leagues = ['NBA', 'ABA', 'BAA']
    mths = ['october', 'november', 'december', 'january', 'february', 'march']
    yrs = []
    yrs.append(2019)
    for i in range(73):
        yrs.append(yrs[i] - 1)
    for league in leagues:
        for yr in yrs:
            for mth in mths:
                ##Assign local path, URL
                # print(year, month)
                html_folder = Path(r'data\html\{}_{}_{}_scraped.html'.format(league, yr, mth), header=True)
                csv_folder = Path(r'data\{}_{}_{}.csv'.format(league, yr, mth), header=True)
                if csv_folder.exists ():
                    pass
                else:
                    continue

                outputs = Path(r'data\outputs\{}_{}_{}.csv'.format(league, yr, mth), header=True)
                #print(html_folder)
                counter += (100 / (74 * 3 * 9))
                page_url = open(csv_folder)
                #Apply Beautiful Soup to determine columns of new table##
                soup = BeautifulSoup(page_url, "html.parser")
                #print(soup.prettify())

                ## Create boxes for each data point for scraping ##
                date = []
                start = []
                visitor = []
                ptsv = []
                home = []
                ptsh = []
                box = []
                ot = [None] * 250
                attend = []
                short_url = r'https://www.basketball-reference.com/boxscores/'
                round = ['regular'] * 250


                ## Find and extract relevant data point and then append under appropriate column. For Box Score, extract underlying hyperlink ##

                for row in soup.find_all('tr'):
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
                    #print(a)
                    #if a.attrs is True:                    ###Based on my extraction code at step 1, I seem to have problems here at Step 2 when trying to extract the URL (href) of the BoxScore column.
                     #   pass
                    #else:
                        #continue
                    #html = list(a.attrs)[2]
                    #print(html)
                    #short_html = html.split('"')[0]
                    #print(short_html)
                    box.append(short_url)
                    #print(box)
                    at = row.find_all('td')[7]
                    attend.append(at.get_text())
                    #print(attend)
                    df = pd.DataFrame(list(zip(date, start, visitor, ptsv, home, ptsh, box, ot, attend, round)))

                    #print(df)
                    df.columns = ['date','start','visitor','visitor.pts','home','home.pts','boxscore','ot','attend', 'round']

                    df.to_csv((outputs), header=True)
                    df.to_html((html_folder), header=True)

def april_scrape():
    counter = 0
    leagues = ['NBA', 'ABA', 'BAA']
    mths = ['april']
    yrs = []
    yrs.append(2019)
    for i in range(73):
        yrs.append(yrs[i] - 1)
    for league in leagues:
        for yr in yrs:
            for mth in mths:
                ##Assign local path, URL
                # print(year, month)
                html_folder = Path(r'data\html\{}_{}_{}_scraped.html'.format(league, yr, mth), header=True)
                csv_folder = Path(r'data\{}_{}_{}.csv'.format(league, yr, mth), header=True)
                if csv_folder.exists ():
                    pass
                else:
                    continue

                outputs = Path(r'data\outputs\{}_{}_{}.csv'.format(league, yr, mth), header=True)
                #print(html_folder)
                counter += (100 / (74 * 3 * 9))
                page_url = open(csv_folder)
                #Apply Beautiful Soup to determine columns of new table##
                soup = BeautifulSoup(page_url, "html.parser")
                #print(soup.prettify())

                ## Create boxes for each data point for scraping ##
                date = []
                start = []
                visitor = []
                ptsv = []
                home = []
                ptsh = []
                box = []
                ot = [None] * 250
                attend = []
                short_url = r'https://www.basketball-reference.com/boxscores/'
                round = ['regular'] * 250


                ## Find and extract relevant data point and then append under appropriate column. For Box Score, extract underlying hyperlink ##

                for row in soup.find_all('tr'):
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
                    df.to_html((html_folder), header=True)


def playoff_local_scrape():
    counter = 0
    leagues = ['NBA', 'ABA', 'BAA']
    yrs = []
    yrs.append(2019)
    for i in range(73):
        yrs.append(yrs[i] - 1)
    for league in leagues:
        for yr in yrs:
                ##Assign local path, URL
                # print(year, month)
                html_folder = Path(r'data\html\{}_{}_scraped_playoffs.html'.format(league, yr), header=True)
                csv_folder = Path(r'data\{}_{}_playoffs.csv'.format(league, yr), header=True)
                if csv_folder.exists ():
                    pass
                else:
                    continue

                outputs = Path(r'data\outputs\{}_{}_playoffs.csv'.format(league, yr), header=True)
                #print(html_folder)
                counter += (100 / (74 * 3 * 9))
                page_url = open(csv_folder)
                #Apply Beautiful Soup to determine columns of new table##
                soup = BeautifulSoup(page_url, "html.parser")
                #print(soup.prettify())

                ## Create boxes for each data point for scraping ##
                date = []
                start = []
                visitor = []
                ptsv = []
                home = []
                ptsh = []
                box = []
                ot = [None] * 250
                attend = []
                short_url = r'https://www.basketball-reference.com/boxscores/'
                round = ['playoffs'] * 250


                ## Find and extract relevant data point and then append under appropriate column. For Box Score, extract underlying hyperlink ##

                for row in soup.find_all('tr'):
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
                    at = row.find_all('td')[7]
                    attend.append(at.get_text())
                    #print(attend)
                    df = pd.DataFrame(list(zip(date, start, visitor, ptsv, home, ptsh, box, ot, attend, round)))

                    #print(df)
                    df.columns = ['date','start','visitor','visitor.pts','home','home.pts','boxscore','ot','attend', 'round']

                    df.to_csv((outputs), header=True)
                    df.to_html((html_folder), header=True)

regular_scrape()
playoff_local_scrape()
april_scrape()