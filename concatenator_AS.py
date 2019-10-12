import pandas as pd
import glob

def df_concatenate():
    ## Set path for csv concatenation. THIS WILL NEED TO BE SET TO LOCAL PATH ##
    path = r'C:\Users\adamj\OneDrive\Documents\Writings\Work.w.Seth\PureHTML'
    all_files = glob.glob(path + '/*.html')
    total = []

    ## Loop through files and append to giant dataframe

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        total.append(df)

    #total.drop_duplicates(keep=False, inplace=True)
    total = pd.concat(total, axis=0, ignore_index=True)

    ## Write to CSV. THIS WILL NEED TO BE SET TO LOCAL PATH ##

    total.to_csv(r"C:\Users\adamj\OneDrive\Documents\Writings\Work.w.Seth\total_data.csv", header=True)
    print(total)
