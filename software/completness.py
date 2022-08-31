'''
MIT License (MIT)
Copyright © 2022 Chiara Catizone, Giulia Venditti

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

def compl(source_data):
    import csv
    with open(source_data, 'r', encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [dict(x) for x in reader]

    conteggio = 0
    cont_value = 0
    for row in data:
        for value in row:
            cont_value += 1
            if row[value] == ' ' or row[value] == '':
                conteggio += 1
    if conteggio == 0:
        print('Completezza: 100%')
        return
    else:
        completezza_pop = (conteggio / cont_value) * 100
        percentuale_completezza_pop = 100 - completezza_pop
        print("Completezza:", round(percentuale_completezza_pop, 2), "%")
    print('Valori totali:', cont_value)
    print('Valori nulli:', conteggio)
    return

compl('datasets/dbf-esempi/RUOM_Aree_Costiere_Marine_ITR081FRMRERPOINT_2019.csv')
compl('datasets/dbf-esempi/RUOM_Reticolo_Principale_ITR081FRMRERPOINT_2019.csv')