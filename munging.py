import pandas as pd
from tqdm import tqdm

def removingOthers():
    df = pd.read_csv('data.csv')

    cols = [0, 1, 2, 3, 5, 6]
    df.drop(df.columns[cols], axis=1, inplace=True)
    df.to_csv('urls.csv')

def stripping():
    f = open('urls.csv')
    file = f.read()
    f.close()

    updated = []
    file = file.split('\n')
    for line in tqdm(file):
        line = line.split(',')[-1]
        line = line.split('/')[-1]
        updated.append(line)

    file = open('ids', 'w')
    file.write('\n'.join(updated))
