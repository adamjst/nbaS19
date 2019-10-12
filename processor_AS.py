# Import libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests

leagues = ['NBA', 'ABA', 'BAA']

mths = ['june', 'may', 'april', 'march','february', 'january', 'december', 'november', 'october']
yrs = []
yrs.append(2019)
for i in range(1):
    yrs.append(yrs[i] - 1)

def local_scrape():
    counter = 0
    for league in leagues:
        for yr in yrs:
            for mth in mths:
                try:
                    ##Assign local path, URL
                    # print(year, month)
                    url = 'C://Users/adamj/OneDrive/Documents/Writings/Work.w.Seth/pureHTML/{}_{}_{}.html'.format(league, yr, mth)
                    print(url)
                    counter += (100 / (74 * 3 * 9))
                    page_url = open(url)

                    #Apply Beautiful Soup to determine columns of new table##
                    soup = BeautifulSoup(page_url, "html.parser")
                    #print(soup.prettify())


                    content = soup.find_all('th')[6]
                    print(content)

                    ## Create boxes for each data point for scraping ##

                    date = []
                    start = []
                    visitor = []
                    ptsv = []
                    home = []
                    ptsh = []
                    box = []
                    ot = [None] * 110
                    attend = []
                    notes = [None] * 110
                    short_url = r'https://www.basketball-reference.com/leagues/{}_{}_games-{}.html'.format(league, yr, mth)


                ## Find and extract relevant data point and then append under appropriate column. For Box Score, extract underlying hyperlink ##

                    for row in content.find_all('tr'):
                        try:
                            dat = row.find('th')
                            date.append(dat.get_text())
                            print(date)

                            #dates = date.datetime.strptime(str, '%s,%b %d, %Y')  WORKING ON CONVERTING TO DATETIME
                            #date = date.strftime('%Y')
                            sta = row.find('td')
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
                            #print(pg.attrs)                   ###STRUGGLING TO EXTRACT URL
                            #print(a)
                            box.append(short_url)
                            print(box)
                            at = row.find_all('td')[7]
                            attend.append(at.get_text())
                            #print(attend)
                            df = pd.DataFrame(list(zip(date, start, visitor, ptsv, home, ptsh, box, ot, attend, notes)))
                            ## Assign to CSV written to specific month and year. ##THIS WILL NEED TO BE ADJUSTED TO YOUR LOCAL PATH##
                            # print(df)
                            df.to_csv(r"C:\Users\adamj\OneDrive\Documents\Writings\Work.w.Seth\Clean\clean_{}_{}_{}.csv".format(league, yr, mth), header=True)
                            #print(str(counter)+ '% completed')
                        except:
                            continue
                except:
                    continue
local_scrape()
