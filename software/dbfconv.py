'''
MIT License (MIT)
Copyright © 2022 Chiara Catizone, Giulia Venditti

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
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
