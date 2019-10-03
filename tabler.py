import pandas as pd
from scraper3 import *
import psycopg2
import random 
import pprint as pp
import re
#30 teams
teams = ['Atlanta Hawks', 'Boston Celtics','Brooklyn Nets','Charlotte Bobcats ',
'Chicago Bulls ','Cleveland Cavaliers ','Dallas Mavericks ','Denver Nuggets ',
'Detroit Pistons ','Golden State Warriors ','Houston Rockets ','Indiana Pacers ',
'Los Angeles Clippers ','Los Angeles Lakers ','Memphis Grizzlies ','Miami Heat ','Milwaukee Bucks ',
'Minnesota Timberwolves ','New Orleans Hornets ','New York Knicks ','Oklahoma City Thunder ',
'Orlando Magic ','Philadelphia Sixers ','Phoenix Suns ','Portland Trail Blazers ',
'Sacramento Kings ','San Antonio Spurs ','Toronto Raptors ','Utah Jazz ','Washington Wizards']

#teams with non-constant names:
	#Brooklyn Nets
	#Charlotte Hornets
	#New Orleans Pelicans
	#Oklahoma City Thunder

#playoffs start april 13, 2019. Consider only dates before that: 
# Oct 28 - April 12 regular season

score_df = pd.read_csv('team_score2019.csv', names = ['visitors','ptsv','home','ptsh'],
						skiprows = 34,delimiter = ',') #skip may,june
#print(score_df.head(1400))

score_df.drop(score_df.index[[115,145]]) # removes april 13 - 21
with open('2019data.csv','w') as f:
	#print(score_df.head(1400))
	score_df.to_csv(f,header=False,sep=',')

#	HOW TO RANDOMLY DRAW 3 TEAMS & THEIR MATCHES ?????

#tres = score_df.sample(n=3)
#print(tres)

#for n in range(3):
	#print (random.randint(0,30)) #14,20,26

#3 randomly selected teams
#print(teams[14]+teams[20]+teams[26]) #Memphis Grizzlies Oklahoma City Thunder San Antonio Spurs 
print(teams[14] in list(score_df['visitors']))

#print('Memphis Grizzlies' in list(score_df['visitors']))

#vis = list(score_df['visitors'])
#pp.pprint(vis)

#vis = score_df.set_index(['visitors'])
#hom = score_df.set_index(['home'])
#print(vis.loc['Miami Heat'])
#for i in teams: # which items of the teams list is locateable in the columns
	#print(i)
	#try:
		#print(vis.loc[i])
	#except:
		#continue

#score_df.loc[str((score_df['visitors'])==teams[14])] 
#or str((score_df['visitors'])==teams[20]) or
#str((score_df['visitors'])==teams[26])]

#matches1 = score_df.visitors.str.contains('Oklahoma City Thunder',case=False)
#print(score_df[matches])
#score1 = score_df[matches1].loc[(score_df[matches1].ptsv) > (score_df[matches1].ptsh)]
#print(score1)
#matches2 = score_df.visitors.str.contains('Minnesota Timberwolves',case=False)
#print(score_df[matches])
#score2 = score_df[matches2].loc[(score_df[matches2].ptsv) > (score_df[matches2].ptsh)]
#print(score2)
#matches3 = score_df.home.str.contains('Dallas Mavericks',case=False)
#score3 = score_df[matches3].loc[(score_df[matches3].ptsv) < (score_df[matches3].ptsh)]
#print(score3)

match1 = re.search('Grizzlies',score_df['visitors'])

