from typing import OrderedDict
from cv2 import split
from dbfread import DBF
import pandas as pd
import pprint

name = 'Coperture_quaternarie_10K'
idx = -1

df = pd.DataFrame()

for row in DBF('../datasets/originals/'+name+'.dbf', encoding='latin-1'):
    
    #qui aggiunge le colonne la prima volta che le vede come keys
    if idx == -1:
        df.columns = pd.DataFrame(columns=row.keys())
    idx+=1
    print(idx)

    for key, value in row.items():
        #AGGIUNGI COLONNE SE NON ESISTONO 
        if key not in df.columns:
            print('missing', key) 
            df.assign(col_name=key)
            df.loc[idx, key] = value

        else: 
            df.loc[idx, key] = value
        # print(key, value )

pprint.pprint(df)

df.to_csv('../datasets/dbf-esempi/'+name+'.csv', encoding='utf-8')



