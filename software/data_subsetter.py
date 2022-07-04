import pandas as pd
import re

doc = pd.read_csv('../datasets/dbf-esempi/Coperture_quaternarie_10K.csv')
working = doc[doc.DATA_AGGIO.str.contains('2', regex= True, na=False)]
working['DATA_AGGIO'] = working['DATA_AGGIO'].apply(lambda x : x[-4:])
print(working)

working.to_csv('../datasets/dbf-esempi/Coperture_quaternarie_10K.csv', encoding='utf-8')