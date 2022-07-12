from typing import OrderedDict
from cv2 import split
from dbfread import DBF
import pandas as pd
import pprint

name = 'PSAI_Aree_rischio_elevato_molto_elevato'
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


import pandas as pd
import os 

for item in os.listdir('../datasets/final_dataset/'):
    df = pd.read_csv('../datasets/final_dataset/'+item)
    print(item[:-4])

    df.to_json('../datasets/final_dataset/'+item[:-4]+'.json')
