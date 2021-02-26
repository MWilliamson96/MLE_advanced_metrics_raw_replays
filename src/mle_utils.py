import requests
from pathlib import Path
import pandas as pd

def read_multiindex_csv_to_df(path, header_lines=[0,1]):
    '''
    signature: read_multiindex_csv_to_df(path, header_lines=[0,1])
    
    reads csv with multiple column names for each column into a pandas dataframe
    
    parameters:
    -path: REQUIRED, string or pathlib.path object pointing to the csv file
    
    -header_lines: OPTIONAL, the lines of the csv to be used as column names. by default set to [0,1] (the first two lines of data)
    '''
    df = pd.read_csv(str(path), header=header_lines)
    col_names = list(df.columns)
    tmp_fill = ''
    for i in range(0, len(col_names)):
        current = col_names[i]
        if not current[0].startswith('Unnamed'):
            tmp_fill = current[0]
        else:
            col_names[i] = (tmp_fill, current[1])
    new_cols = pd.MultiIndex.from_tuples(col_names)
    df.columns = new_cols
    return df