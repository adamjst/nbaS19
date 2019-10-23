import pandas as pd
import glob

"""Concatenate dataframes from all months, all years, all leagues. Return one centralized dataframe"""
def df_concatenate():
    """Convert csvs to dataframes and then concatenate before returning csv"""
    ## Set relative path for csv concatenation.
    path = ('data/outputs')
    all_files = glob.glob(path + '/*.csv')
    total =[]

    ## Loop through files and append to giant dataframe

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        total.append(df)

    #total.drop_duplicates(keep=False, inplace=True)
    total = pd.concat(total, axis=0, ignore_index=True)
    print(total.columns)

    total.to_csv("data/total_data.csv", header=True)
    print(total)
df_concatenate()