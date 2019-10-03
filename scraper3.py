import pandas as pd
from bs4 import BeautifulSoup
import requests

import pprint as pp

years=[]
years.append(2019)
for i in range(72):
	years.append(years[i]-1)

months = ['june','may','april','march','february','january','december','november','october']

#https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059
#https://srome.github.io/Parsing-HTML-Tables-in-Python-with-BeautifulSoup-and-pandas/
#https://medium.com/analytics-vidhya/web-scraping-wiki-tables-using-beautifulsoup-and-python-6b9ea26d8722

#april is playoff season, the outlier from other months....<tr data-row = "78"

def scrape():
	for year in years:
		for month in months:
			try:

				print(year,month)
				url = 'https://www.basketball-reference.com/leagues/NBA_{}_games-{}.html'.format(year,month)

				page_url = requests.get(url).text
				soup = BeautifulSoup(page_url,'lxml')
				#print(soup.prettify())

				table = soup.find('table',{'class':'suppress_glossary'})
				#print(table)

				cols = table.find_all('tr')[0]
				#print(cols)

				header=[]
				for col in cols.find_all('th'):
					header.append(col.get_text())
				header[6] = 'Box Score'
				header[7] = 'OT'

				#print(header) #['Date', 'Start (ET)', 'Visitor/Neutral', 'PTS', 'Home/Neutral', 'PTS', 'Box Score', 'OT', 'Attend.', 'Notes']
				content = table.find('tbody')
				#print(content.prettify())

				date=[]
				start=[]
				visitor=[]
				ptsv=[]
				home=[]
				ptsh=[]
				box = [None] * 110
				ot = [None] * 110
				attend =[]
				notes = [None] * 110
				
				for row in content.find_all('tr'):
					try:
						dat = row.find('th')
						date.append(dat.get_text())
						sta = row.find('td')
						start.append(sta.get_text())
						vis = row.find_all('td')[1]
						visitor.append(str(vis.get_text()))
						pv = row.find_all('td')[2]
						ptsv.append(pv.get_text())
						ho = row.find_all('td')[3]
						home.append(str(ho.get_text()))
						ph = row.find_all('td')[4]
						ptsh.append(ph.get_text())
						at = row.find_all('td')[7]
						attend.append(at.get_text())
					except:
						continue

				#print(len(date)==len(start)==len(visitor)==len(ptsv)==len(home)==len(ptsh)==len(attend)) #True,110

				df = pd.DataFrame(list(zip(date,start,visitor,ptsv,home,ptsh,box,ot,attend,notes)),columns = header)
				print(df)

				df2 = pd.DataFrame(list(zip(visitor,ptsv,home,ptsh)))
				
				#with open('nbadat{}.csv'.format(year),'a') as f: # all data
					#df2.to_csv(f,header=False,sep=',')

				with open('team_score{}.csv'.format(year),'a') as f: # team names and points only
					df2.to_csv(f,header=False,sep=',')

			except:
				continue
#scrape()


