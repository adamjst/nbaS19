import pandas as pd
from pathlib import Path
import re

"""Two step process of assessing whether correct string/number value is in each column before transferring correct entries into new column"""
def df_alignment():
    """align data into proper columns based on regex"""
    ## Set relative path
    path = Path('data', 'total_data.csv', header=True)
    print(path)
    ## Read in csv
    df = pd.read_csv(path, index_col=None, header=0)

    ####VISITOR Column Alignment.###

    for index, row in df.iterrows():
        # Compile regex pattern to match with character string
        prog = re.compile('[a-zA-z].+')

        # access column using match of column name
        if prog.match(row['visitor']):
            #if correct match, insert the match into the new column
            df.at[index, 'vis2'] = (str(prog.match(row['visitor']).group(0)))
        else:
            #if no match, insert filler string into new column
            df.at[index, 'vis2'] = ('Fill')

    for index, row in df.iterrows():
        # Compile regex pattern to match with character filler
        prog = re.compile('Fill')

        # access new column using match of character filler
        if prog.match(row['vis2']):
            #if correct match, insert the team name from the 'start' column into new visitor column
            df.at[index, 'vis2'] = df.at[index, 'start']
        else:
            #if no match, team name is already there, so ignore and keep going
            pass

    ####HOME Column Alignment###

    for index, row in df.iterrows():
        # Compile regex pattern to match with character string
        prog = re.compile('[a-zA-z].+')

        # Access column using match of column name
        if prog.match(row['home']):
            # if correct match, insert the match into the new column
            df.at[index, 'home2'] = (str(prog.match(row['home']).group(0)))
        else:
            #if no match, insert filler string into new column
            df.at[index, 'home2'] = ('Fill')

    for index, row in df.iterrows():
        # Compile regex pattern to match with character filler
        prog = re.compile('Fill')

        # access new column using match of character filler
        if prog.match(row['home2']):
            #if correct match, insert the team name mistakenly in the 'visitor.pts' column into new home column
            df.at[index, 'home2'] = df.at[index, 'visitor.pts']
        else:
            #if no match, team name is already there, so ignore and keep going
            pass

    ####Visitor Points Column Alignment.###
    for index, row in df.iterrows():
        # Compile regex pattern to match with numerical value
        num = re.compile('[0-9]+')

        # Access column using match of column name
        if num.match(row['visitor.pts']):
            # if correct match of numerical values, insert the match into the new column
            df.at[index, 'vis.pts2'] = num.match(row['visitor.pts']).group(0)
        else:
            #if no match, insert filler string into new column
            df.at[index, 'vis.pts2'] = ('Fill')

    for index, row in df.iterrows():
        # Compile regex pattern to match with character filler
        num = re.compile('Fill')

        # access new column using match of character filler
        if num.match(row['vis.pts2']):
            #if correct match, insert the points total mistakenly in the 'visitor' column into new vis. pts column
            df.at[index, 'vis.pts2'] = df.at[index, 'visitor']
        else:
            #if no match, points value is already there, so ignore and keep going
            pass

    ####HOME Points Column Alignment.###
    for index, row in df.iterrows():
        # Compile regex pattern to match with numerical value
        num = re.compile('[0-9]+')

        # Access column using match of column name
        if num.match(row['home.pts']):
            # if correct match of numerical values, insert the match into the new column
            df.at[index, 'home.pts2'] = num.match(row['home.pts']).group(0)
        else:
            #if no match, insert filler string into new column
            df.at[index, 'home.pts2'] = ('Fill')

    for index, row in df.iterrows():
        # Compile regex pattern to match with character filler

        num = re.compile('Fill')

        # Access column using match of column name
        if num.match(row['home.pts2']):
            #if correct match, insert the points total mistakenly in the 'home' column into new home.pts column
            df.at[index, 'home.pts2'] = df.at[index, 'home']
        else:
            #if no match, points value is already there, so ignore and keep going
            pass

    #send to csv
    df.to_csv(path, header=True)


df_alignment()