import pandas as pd
from regex import D

def municipality(data):
    mun = []
    for x in data:
        if '::' in x:
            x = x.split('::')
            x = x[0]
            x = x.lower()
            x = x.title()
            mun.append(x)

        elif x.isupper() == True:
            x = x.lower()
            x = x.title()
            mun.append(x)

        else:
            value = x
            data = pd.read_csv('datasets/original_dataset/r_finacing.csv')
            data = data.query("location == @value")
            data.head()
            if len(data) == 0:
                mun.append('null')
            else:
                mun.append(data.iat[0,8])
    return mun

def mun_to_prov(data):
    prov_code = []
    prov_name = []

    for x in data:
        prov_info = pd.read_csv('datasets/final_dataset/municipality.csv')
        value = x 
        query = prov_info.query("municipality == @value")
        if len(query) == 0: 
            prov_code.append('null')
            prov_name.append('null')
        else:
            prov_name.append(query.iat[0,1])
            prov_code.append(query.iat[0,2])

    return prov_code, prov_name

def province(data):
    prov_name = []
    prov_code = []

    for x in data:

        if ':::' in x:
            x = x.split(':::')
            x = x[0]
            x = x.lower()
            x = x.title()
        else:
            x = x.title()

        if x == "Reggio-Nellemilia":
            x = "Reggio Emilia"
        elif x == "Forli-Cesena":
            x = "Forlì-Cesena"
        elif x == "Forli'-Cesena":
            x = "Forlì-Cesena"
        elif x == "Reggio Nell'Emilia":
            x = "Reggio Emilia"

        if x == "Ferrara":
            prov_code.append('FE')
        elif x == "Rimini":
            prov_code.append("RN")
        elif x == "Forlì-Cesena":
            prov_code.append("FC")
        elif x == "Ravenna":
            prov_code.append("RA")
        elif x == "Bologna":
            prov_code.append("BO")
        elif x == "Modena":
            prov_code.append("MO")
        elif x == "Reggio Emilia":
            prov_code.append("RE")
        elif x == "Parma":
            prov_code.append("PR")
        elif x == "Piacenza":
            prov_code.append("PC")
        else:
            x = "null"
            prov_code.append(x)

        prov_name.append(x)

    return prov_code, prov_name

def coordinate(data):
    latitudine = []
    longitudine = []

    for x in data:
        geo = pd.read_json('datasets/original_dataset/italy_geo.json')
        value = x
        query = geo.query("comune == @value")


        if len(query) == 0:
            latitudine.append('null')
            longitudine.append('null')
        else:
            latitudine.append(query.iat[0,3])
            longitudine.append(query.iat[0,2])
    return latitudine, longitudine

def date(data):
    d = []
    for x in data:
        x = str(x)
        if '-' in x:
            date = x.split('-')
            date.reverse()
            x = '/'.join(date)
            d.append(x)
        elif x == "2020":
            date = ['01', '01', x]
            x = '/'.join(date)
            d.append(x)
        else:
            date = [x[6:8], x[4:6],  x[:4] ]
            x = '/'.join(date)
            d.append(x)
    return d

def action_descr(data):
    j = []
    for x in data:
        x = x.lower()
        x = x.capitalize()
        if x == "Non definito":
            x = 'null'
        elif x == "missing":
            x = "null"
        j.append(x)
    return j

def financing(data):
    k = []
    for x in data:
        if x == 0.0:
            x = 'null'
        k.append(x)
    return k


def actions(source_path_list, out_data):

    df1_path = source_path_list[0]
    df2_path = source_path_list[1]
    df3_path = source_path_list[2]
    df4_path = source_path_list[3]
    df5_path = source_path_list[4]

    data_financing = pd.read_csv(df1_path)
    data_financing = data_financing.query("region == 'emilia-romagna'")
    data_financing = data_financing.reset_index()

    df1 = pd.DataFrame(columns=[])
    df1['prov_name'] =  province(data_financing['province'])[1]
    df1['prov_code'] =  province(data_financing['province'])[0]
    df1['municipality'] = data_financing['location_label']
    df1['latitude'] = coordinate(data_financing['location_label'])[0]
    df1['longitude'] = coordinate(data_financing['location_label'])[1]
    df1['date'] = date(data_financing['agreement_date'])
    df1['action_type'] = "reparatory intervention"
    df1['action_description'] = action_descr(data_financing['instability_type'])
    df1['tot_action_financing'] = financing(data_financing['amount_fin'])

    data_interventions = pd.read_csv(df2_path)
    data_interventions = data_interventions.query("region == 'emilia-romagna'")
    data_interventions.reset_index()

    print('df1')

    df2 = pd.DataFrame(columns=[])
    df2['prov_name'] =  province(data_interventions['province'])[1]
    df2['prov_code'] =  province(data_interventions['province'])[0]
    df2['municipality'] = municipality(data_interventions['relation_lot_loc'])
    df2['latitude'] = coordinate(df2["municipality"])[0]
    df2['longitude'] = coordinate(df2["municipality"])[1]
    df2['date'] = date(data_interventions['agreement_date'])
    df2['action_type'] = "reparatory intervention"
    df2['action_description'] = action_descr(data_interventions['type_label'])
    df2['tot_action_financing'] = 'null'

    print('df2')

    opere_difesa = pd.read_csv(df3_path)


    df3 = pd.DataFrame(columns=[])

    mun = municipality(opere_difesa['COMUNE'])

    df3['prov_name'] =  mun_to_prov(mun)[1]
    df3['prov_code'] =  mun_to_prov(mun)[0]
    df3['municipality'] = mun
    df3['latitude'] = coordinate(mun)[0]
    df3['longitude'] = coordinate(mun)[1]
    df3['date'] = date(opere_difesa['ANNO'].astype(int))
    df3['action_type'] = 'preventive measures'
    df3['action_description'] = opere_difesa['TIPO_OPERA']
    df3['tot_action_financing'] = 'null'

    print('df3')

    p1 = pd.read_csv(df4_path, delimiter=';', low_memory=False)
    p1 = p1.query("DEN_REGIONE == 'EMILIA-ROMAGNA'")
    p1 = p1.reset_index()

    df4 = pd.DataFrame(columns = [])
    df4['prov_name'] =  province(p1['DEN_PROVINCIA'])[1]
    df4['prov_code'] =  province(p1['DEN_PROVINCIA'])[0]
    df4['municipality'] = municipality(p1['DEN_COMUNE'])
    df4['latitude'] = coordinate(df4['municipality'])[0]
    df4['longitude'] = coordinate(df4['municipality'])[1]
    df4['date'] = date(p1['OC_DATA_INIZIO_PROGETTO'])
    df4['action_type'] = 'preventive measures'
    df4['action_description'] = action_descr(p1['CUP_DESCR_CATEGORIA'])
    df4['tot_action_financing'] = p1['FINANZ_TOTALE_PUBBLICO']

    print('df4')

    p2 = pd.read_csv(df5_path, delimiter=';', low_memory=False)
    p2 = p2.query("DEN_REGIONE == 'EMILIA-ROMAGNA'")
    p2 = p2.reset_index()

    df5 = pd.DataFrame(columns = [])
    df5['prov_name'] =  province(p2['DEN_PROVINCIA'])[1]
    df5['prov_code'] =  province(p2['DEN_PROVINCIA'])[0]
    df5['municipality'] = municipality(p2['DEN_COMUNE'])
    df5['latitude'] = coordinate(df5['municipality'])[0]
    df5['longitude'] = coordinate(df5['municipality'])[1]
    df5['date'] = date(p2['OC_DATA_INIZIO_PROGETTO'])
    df5['action_type'] = 'preventive measures'
    df5['action_description'] = action_descr(p2['CUP_DESCR_CATEGORIA'])
    df5['tot_action_financing'] = p2['FINANZ_TOTALE_PUBBLICO']

    print('df5')
    df = pd.concat([df1, df2, df3, df4, df5], ignore_index = True, axis = 0)

    df.to_csv(out_data)

actions( ['datasets/original_dataset/r_finacing.csv', 'datasets/original_dataset/r_intervention.csv', 'datasets/original_dataset/Opere_Difesa_2020.csv', 'datasets/original_dataset/progetti_esteso_EMR_2014-2020_20220228.csv', 'datasets/original_dataset/progetti_esteso_EMR_2007-2013_20220228.csv'], 'datasets/final_dataset/actions.csv')


