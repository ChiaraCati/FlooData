def territory(source_path, out_data):
    import pandas as pd
    data = pd.read_csv(source_path)
    data = data.query("cod_reg == 8")
    data = data.reset_index()


    df = pd.DataFrame(columns=[])
    df['cod_prov'] = data['cod_prov']

    pro_name = []
    pro_code = []

    for x in df['cod_prov']:
        if x == 99:
            pro_name.append("Rimini")
            pro_code.append("RN")
        if x == 40:
            pro_name.append("Forlì-Cesena")
            pro_code.append("FC")
        if x == 39:
            pro_name.append("Ravenna")
            pro_code.append("RA")
        if x == 38:
            pro_name.append("Ferrara")
            pro_code.append("FE")
        if x == 37:
            pro_name.append("Bologna")
            pro_code.append("BO")
        if x == 36:
            pro_name.append("Modena")
            pro_code.append("MO")
        if x == 35:
            pro_name.append("Reggio Emilia")
            pro_code.append("RE")
        if x == 34:
            pro_name.append("Parma")
            pro_code.append("PR")
        if x == 33:
            pro_name.append("Piacenza")
            pro_code.append("PC")

    df['prov_name'] = pro_name
    df['prov_code'] = pro_code
    df.drop('cod_prov', inplace=True, axis=1)

    if 'comune' in data.columns:

        df['municipality'] = data['comune']

        geo = pd.read_json('datasets/original_dataset/italy_geo.json')

        latitudine = []
        longitudine = []
        for x in df["municipality"]:
            geo = pd.read_json('data/italy_geo.json')
            value = x
            if value == 'Montescudo-Monte Colombo':
                value = 'Montescudo - Monte Colombo'
            if value == 'Sorbolo Mezzani':
                value = 'Sorbolo'
            query = geo.query("comune == @value")
            if len(query) == 0:
                latitudine.append('null')
                longitudine.append('null')
            else:
                latitudine.append(query.iat[0,3])
                longitudine.append(query.iat[0,2])

        df['latitude'] = latitudine
        df['longitude'] = longitudine

    df['area (kmq)'] = data['ar_kmq']
    df['high_hydraulic_risk_area_p3 (%)'] = data['aridp3_p']
    df['medium_hydraulic_risk_area_p2 (%)'] = data['aridp2_p']
    df['low_hydraulic_risk_area_p1 (%)'] = data['aridp1_p']

    df['very_high_landslide_risk_area_p4 (%)'] = data['ar_frp4_p']
    df['high_landslide_risk_area_p3 (%)'] = data['ar_frp3_p']
    df['medium_landslide_risk_area_p2 (%)'] = data['ar_frp2_p']
    df['low_landslide_risk_area_p1 (%)'] = data['ar_frp1_p']
    df['attention_area (%)'] = data['ar_fraa_p']

    df['resident_population (n)'] = data['pop_res011']
    df['high_hydraulic_risk_population_p3 (%)'] = data['popidp3_p']
    df['medium_hydraulic_risk_population_p2 (%)'] = data['popidp2_p']
    df['low_hydraulic_risk_population_p1 (%)'] = data['popidp2_p']

    df['very_high_landslide_risk_population_p4 (%)'] = data['popfrp4_p']
    df['high_landslide_risk_population_p3 (%)'] = data['popfrp3_p']
    df['medium_landslide_risk_population_p2 (%)'] = data['popfrp2_p']
    df['low_landslide_risk_population_p1 (%)'] = data['popfrp1_p']
    df['attention_population (%)'] = data['popfraa_p']

    df['resident_family (n)'] = data['fam_tot']
    df['high_hydraulic_risk_family_p3 (%)'] = data['famidp3_p']
    df['medium_hydraulic_risk_family_p2 (%)'] = data['famidp2_p']
    df['low_hydraulic_risk_family_p1 (%)'] = data['famidp1_p']

    df['very_high_landslide_risk_family_p4 (%)'] = data['famfrp4_p']
    df['high_landslide_risk_family_p3 (%)'] = data['famfrp3_p']
    df['medium_landslide_risk_family_p2 (%)'] = data['famfrp2_p']
    df['low_landslide_risk_family_p1 (%)'] = data['famfrp1_p']
    df['attention_family (%)'] = data['famfraa_p']

    df['building (n)'] = data['ed_tot']
    df['high_hydraulic_risk_building_p3 (%)'] = data['edidp3_p']
    df['medium_hydraulic_risk_building_p2 (%)'] = data['edidp2_p']
    df['low_hydraulic_risk_building_p1 (%)'] = data['edidp1_p']

    df['very_high_landslide_risk_building_p4 (%)'] = data['edfrp4_p']
    df['high_landslide_risk_building_p3 (%)'] = data['edfrp3_p']
    df['medium_landslide_risk_building_p2 (%)'] = data['edfrp2_p']
    df['low_landslide_risk_building_p1 (%)'] = data['edfrp1_p']
    df['attention_building (%)'] = data['edfraa_p']

    df['enterprise (n)'] = data['im_tot']
    df['high_hydraulic_risk_enterprise_p3 (%)'] = data['imidp3_p']
    df['medium_hydraulic_risk_enterprise_p2 (%)'] = data['imidp2_p']
    df['low_hydraulic_risk_enterprise_p1 (%)'] = data['imidp1_p']

    df['very_high_landslide_risk_enterprise_p4 (%)'] = data['imfrp4_p']
    df['high_landslide_risk_enterprise_p3 (%)'] = data['imfrp3_p']
    df['medium_landslide_risk_enterprise_p2 (%)'] = data['imfrp2_p']
    df['low_landslide_risk_enterprise_p1 (%)'] = data['imfrp1_p']
    df['attention_enterprise (%)'] = data['imfraa_p']

    df['cultural_heritage (n)'] = data['n_vir']
    df['high_hydraulic_risk_cultural_heritage_p3 (%)'] = data['bbccidp3_p']
    df['medium_hydraulic_risk_cultural_heritage_p2 (%)'] = data['bbccidp2_p']
    df['low_hydraulic_risk_cultural_heritage_p1 (%)'] = data['bbccidp1_p']

    df['very_high_landslide_risk_cultural_heritage_p4 (%)'] = data['bbccfrp4_p']
    df['high_landslide_risk_cultural_heritage_p3 (%)'] = data['bbccfrp3_p']
    df['medium_landslide_risk_cultural_heritage_p2 (%)'] = data['bbccfrp2_p']
    df['low_landslide_risk_cultural_heritage_p1 (%)'] = data['bbccfrp1_p']
    df['attention_cultural_heritage (%)'] = data['bbccfraa_p']

    df.to_csv(out_data)

territory('datasets/original_dataset/comuni_pir.csv', 'datasets/final_dataset/municipality.csv')
territory('datasets/original_dataset/province_pir.csv', 'datasets/final_dataset/province.csv')

