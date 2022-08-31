'''
MIT License (MIT)
Copyright © 2022 Chiara Catizone, Giulia Venditti

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import pandas as pd
import re

doc = pd.read_csv('../datasets/dbf-esempi/Coperture_quaternarie_10K.csv')
working = doc[doc.DATA_AGGIO.str.contains('2', regex= True, na=False)]
working['DATA_AGGIO'] = working['DATA_AGGIO'].apply(lambda x : x[-4:])
print(working)

working.to_csv('../datasets/dbf-esempi/Coperture_quaternarie_10K.csv', encoding='utf-8')