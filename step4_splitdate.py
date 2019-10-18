import pandas as pd
from pathlib import Path

def df_splitdate():
    ## Set relative path
    path = Path(r'data\total_data.csv', header=True)
    ## Read in csv
    df = pd.read_csv(path, index_col=None, header=0)
    ##Convert to datetime
    df['date'] = pd.to_datetime(df['date'])
    df['Year']= df['date'].dt.year

    print(df['Year'])

    #Drop unused columns
    df.drop("Unnamed: 0", axis=1, inplace=True)
    df.drop("Unnamed: 0.1", axis = 1, inplace=True)
    print(df.columns)
    #Write to csv
    df.to_csv(r"data\total_data.csv", header=True)

df_splitdate()
