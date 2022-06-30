from dbfread import DBF
for row in DBF('../datasets/originals/Opere_Difesa_2020.dbf', encoding='utf-8'):
    print(row)
