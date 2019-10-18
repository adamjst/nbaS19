import pandas as pd
import glob

def df_concatenate():
    ## Set relative path for csv concatenation.
    path = (r'data\outputs')
    all_files = glob.glob(path + '/*.csv')
    total =[]

    ## Loop through files and append to giant dataframe

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        total.append(df)

    #total.drop_duplicates(keep=False, inplace=True)
    total = pd.concat(total, axis=0, ignore_index=True)
    print(total.columns)

    total.to_csv(r"data\total_data.csv", header=True)
    print(total)
df_concatenate()