# run: ipython cancer_pull.py
# update the file locations

import pandas as pd

def disaggregate(group):
    row = group.irow(0)
    # print out the index as it loops through for sanity
    if group.index.values[0] % 1000 == 0:
        print group.index.values[0], 'of', len(cancer)
    cols = list(row.index.values)[:15]
    return pd.DataFrame({k: [str(row[k])] * row['count'] for k in cols})

location = '/Users/ed/Downloads/'
cancer = pd.read_csv(location + 'cancer.txt', sep='\s+', header=None)

cols = [
    'menopaus',
    'agegrp',
    'density',
    'race',
    'Hispanic',
    'bmi',
    'agefirst',
    'nrelbc',
    'brstproc',
    'lastmamm',
    'surgmeno',
    'hrt',
    'invasive',
    'cancer',
    'training',
    'count',
]

cancer.columns = cols

grps = cancer.groupby(cols[:15], group_keys=False)
new_cancer = grps.apply(disaggregate)

new_cancer.to_csv(location + 'new_cancer.txt', index=False)
