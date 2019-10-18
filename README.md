bootdist.py

  - uploads the pickled data and calculates some statistic. 
  - Ran 10 distribtuions and calculated the std/max to maximize unique values since most were similar in magnitude. A boxplot of 6 averages for each axis (dimension of the array) was plotted using matplotlib.

step1_webscrape
    - Applies beautifulsoup to basketball reference and saves to local file
    
step2_localscrape
    -Converts csvs with raw html to spreadsheet
    
step3_concatenator
    -Creates one giant table from all spreadsheets
    
step4_splitdate
    -Separates year from date
    
total_data.csv
    -all regular season to playoff games from 1946-2019
    
data.zip
    -disaggregated data divided by regular season/playoffs and filetype
    
tabler.py

  - this script attempts to perform some linear transitivity calculations. We only consider regular season so the all the dates before 4/13.
  - disclaimers: some nba teams change over the years, only a few. For reference: https://www.allaboutbasketball.us/nba/relocated-nba-teams.html
  - Much of what I've written so far does not work. I've tried to randomly select three teams for comparison by first generating 3 random numbers in the range(0,29). These 3 numbers are the indices for the three teams. My problem is not being able to index a column (i.e. scoredf['visitors']). For some teams, I was able to call  "  scoredf['Miami Heat']. " but an attempt to index the column with another index based on a list of nba teams doens't work. Try running some of what I've commented out to get an idea.
    
    
 *Links to what I've looked up are commented in the scripts for your reference
