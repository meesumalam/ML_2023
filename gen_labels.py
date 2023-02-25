import pandas as pd
import numpy as np


def extract_labels(df):
    
    label_list = []

    for comment in list(df['Comment'].str.lower()):
        if 'racism' in comment or 'racis' in comment or 'racist' in comment:
            label_list.append('racism')
        elif 'sex' in comment:
            label_list.append('sexism')
        else:
            label_list.append('None')
    # add script to remove it
    return pd.DataFrame(
        {
            'text': df['Comment'],
            'label': label_list
         
        }
    )

if __name__ == "__main__":
    df = pd.read_df = pd.read_fwf('waseemDataSet.txt', sep='\t', header=None, names=['Comment'])

    df_3 = extract_labels(df)

    with open("WaseemDataWithLabels.csv", "w") as f:
        f.writelines(df_3)
