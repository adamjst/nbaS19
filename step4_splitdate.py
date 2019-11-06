import pandas as pd
from pathlib import Path

"""Convert date column to datetime and then return year in new column"""
def df_splitdate():
    """Convert date column to datetime and then return year in new column"""
    ## Set relative path
    path = Path('data', 'total_data.csv', header=True)
    ## Read in csv
    df = pd.read_csv(path, index_col=None, header=0)

    ##Convert to datetime
    df['date'] = pd.to_datetime(df['date'])
    df['Year']= df['date'].dt.year
    df['Month'] = df['date'].dt.month

    #Drop unused columns
    df.drop("Unnamed: 0", axis=1, inplace=True)
    df.drop("Unnamed: 0.1", axis = 1, inplace=True)
    print(df.columns)
    #Write to csv
    df.to_csv(path, header=True)


df_splitdate()