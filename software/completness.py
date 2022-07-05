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