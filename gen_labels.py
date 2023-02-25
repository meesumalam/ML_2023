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
    df = pd.read_fwf('waseemDataSet.txt', sep='\t', header=None, names=['Comment'])

    df_new = extract_labels(df)
    df_new.to_csv("WaseemDataWithLabels2.txt", sep='\t', index=False)
    #with open("WaseemDataWithLabels.txt", "w") as f:
    #    df_new = df_new.to_string(index=False)
    #    f.writelines(df_new)
