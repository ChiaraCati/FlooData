
'''
MIT License (MIT)
Copyright © 2022 Chiara Catizone, Giulia Venditti

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
import pprint
from unicodedata import category
import rdflib
from rdflib import URIRef, Literal, Namespace
from rdflib.namespace import XSD, RDFS, DCTERMS
from rdflib import Literal
import pandas as pd

#initial dict containing plate codes for italian provinces (manually compiled)
cod_prov = {'Piacenza':'PC', 'Ferrara':'FE', 'Ravenna':'RA', 'Parma':'PR', 'Bologna':'BO', 'Rimini':'RN', "Forli'-Cesena":'FC', "Reggio nell'Emilia":'RE', 'Modena':'MO'}

#urls for type and label we fount in prvious steps (through virtuoso endopoint, used to gather all possible types)
type_data = URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type') 
label = URIRef('http://www.w3.org/2000/01/rdf-schema#label')
# create an empty Graph for the rendis dataset and parse a local RDF file by specifying the format into the graph
path1 = '/Users/chiara/Documents/GitHub/Owater/datasets/originals/AA_20191211_SHP/dissesto_07_06_2022.nt'
rendis_data = rdflib.Graph()
rendis = rendis_data.parse(path1, format='nt')

# create an empty Graph for places dataset and parse a local RDF file by specifying the format into the graph
places_data = rdflib.Graph()
result_places = places_data.parse("../datasets/originals/AA_20191211_SHP/luoghi.nt", format='nt')


#urls for types of records we are looking for 
instability = URIRef('http://dati.isprambiente.it/ontology/core#Instability') 
intervention = URIRef('http://dati.isprambiente.it/ontology/core#Intervention')
repair = URIRef('http://dati.isprambiente.it/ontology/core#Repair') 


#functions for searching stuff

def search_rendis_subj(dataset, pred, obj, string):
    support = list()
    
    if string == 'print':
        for s, p, o in dataset.triples((None, pred, obj)):
            print(str(s))
    if string == 'set':
        
        for s, p, o in dataset.triples((None, pred, obj)):
            support.append(str(s))
    return support 

def search_rendis_preds(dataset, subjects_list, string):
    support = set()

    if string == 'print':
        print('in print')
        for subject_uri in subjects_list:
            subject = URIRef(subject_uri)
            for s, p, o in dataset.triples((subject, None, None)):
                print(str(p))
    if string == 'set':
        print('in set')
        for subject_uri in subjects_list:
            subject = URIRef(subject_uri)
            for s, p, o in dataset.triples((subject, None, None)):
          
                pred = str(p)
                support.add(pred)
            
    return support 

# serch objects once sujects and respective predicates have been found 
def search_rendis_obj(dataset, subjects_list, pred, string):
    support = {}
    support2 = set()

    if string == 'analysis':
        for subject_uri in subjects_list:
            subject = URIRef(subject_uri)
            for s, p, o in dataset.triples((subject, pred, None)):
                support2.add(str(o))
        return support2        
    if string == 'dict':
        for subject_uri in subjects_list:
            subject = URIRef(subject_uri)
            for s, p, o in dataset.triples((subject, pred, None)):
                support[subject]=str(o)
    
        return support 


#function to run on subject to see if they have all the same predicates
def test_predicates(dataset, items): 
    x = 1

    if dataset == 'rendis':
        my_data = rendis
    else:
        my_data ==result_places
    for item_url in items:
        item = URIRef(item_url) 
        support = set()

        for s, p, o in rendis.triples((item, None, None)):
            support.add(p)
    if  x == 1:
        comparison = support
        x -=1
    else:
        if support != comparison:
            print(item_url, 'has different predicates')


#VARIABLES FOR INSTABILITIES

#look for all instabilities
instability_subj = search_rendis_subj(rendis, type_data, instability, 'set')
print(instability_subj)

instability_preds = search_rendis_preds(rendis, instability_subj, 'set')
# print(instability_preds)


# preds results are put into variables
instability_group = URIRef('http://dati.isprambiente.it/ontology/core#instabilityGroup')
instability_relatedTo = URIRef('http://dati.isprambiente.it/ontology/core#instabilityRelatedTo')
instability_type = URIRef('http://dati.isprambiente.it/ontology/core#instabilityType')


#look for Emilia-Romagna's instabilities
I_groups = search_rendis_obj(rendis, instability_subj, instability_group, 'analysis')
# print(I_groups)


I_relation = search_rendis_obj(rendis, instability_subj, instability_relatedTo, 'analysis')
# print(I_relation)

#find predicates of instability relations
I_relation_preds = search_rendis_preds(rendis, I_relation, 'set')
# print(I_relation_preds)

main_lot = URIRef('http://dati.isprambiente.it/ontology/core#isLotOf')
I_relation_lot = search_rendis_obj(rendis, I_relation, main_lot, 'analysis')
print(I_relation_lot)

I_relation_lot_preds = search_rendis_preds(rendis, I_relation_lot, 'set')
# print(I_relation_lot_preds)

# look for lot location
primGeo = URIRef('http://dati.isprambiente.it/ontology/core#primaryGeographicalFeature')
I_relation_lot_location = search_rendis_obj(rendis, I_relation_lot, primGeo, 'analysis')
# print(I_relation_lot_location)

# look for locations predicates inside luoghi 
lot_location_preds = search_rendis_preds(result_places, I_relation_lot_location, 'set')
# print(lot_location_preds)


# look for locations predicates regions inside luoghi 
region = URIRef('http://www.geonames.org/ontology#parentADM1')
I_relation_lot_region = search_rendis_obj(result_places, I_relation_lot_location, region, 'analysis')
print(I_relation_lot_region)


#create a first df with data of instabilities and relatove contract to repair them 
data = {}
x = 0
data['instabilities']=[]
data['contract_url']=[]

for instability_url in instability_subj:
    df_instability = URIRef(instability_url)
    value = data['instabilities']
    if value == None:
        value = list(instability_url)
    else:
        value.append(instability_url)
    
    data['instabilities'] = value


    for s, p, o in rendis.triples((df_instability, instability_relatedTo, None)):
        #add related to item
        value2 = data['contract_url']
        if value2 == None:
            value2 = list(str(o))
        else:
            value2.append(str(o))
        
  


df = pd.DataFrame.from_dict(data)



# add contract lot info when if existing  
df['type'] = 'missing'

for idx, row in df.iterrows():
    subj_url = row.instabilities
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, instability_group, None)):
        lot = str(o)
        df.loc[idx,'type'] = lot

df['subtype'] = 'missing'

for idx, row in df.iterrows():
    subj_url = row.instabilities
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, instability_type, None)):
        lot = str(o)
        df.loc[idx,'subtype'] = lot

df['subtypeLabel'] = 'missing'

for idx, row in df.iterrows():
    subj_url = row.subtype
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, label, None)):
        df.loc[idx,'subtypeLabel'] = o



df['contract_lot'] = 'missing'

for idx, row in df.iterrows():
    subj_url = row.contract_url
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, main_lot, None)):
        lot = str(o)
        df.loc[idx,'contract_lot'] = lot

df['lot_location'] = 'missing'

for idx, row in df.iterrows():
    subj_url = row.contract_lot
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, primGeo, None)):
        loc = str(o)
        df.loc[idx,'lot_location'] = loc


df['lot_location_label'] = 'missing'

for idx, row in df.iterrows():
    subj_url = row.lot_location
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in result_places.triples((subj, label, None)):
    
        df.loc[idx,'lot_location_label'] = o

df['lot_region'] = 'missing'

for idx, row in df.iterrows():
    subj_url = row.lot_location
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in result_places.triples((subj, region, None)):
        o = o.split('/')
    
        df.loc[idx,'lot_region'] = o[-1]



df['lot_prov'] = 'missing'
prov = URIRef('http://www.geonames.org/ontology#parentADM2')
for idx, row in df.iterrows():
    subj_url = row.lot_location
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in result_places.triples((subj, prov, None)):
        o = o.split('/')
        df.loc[idx,'lot_prov'] = o[-1]

df['lot_lat'] = 'missing'
lot_lat = URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#lat')
for idx, row in df.iterrows():
    subj_url = row.lot_location
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in result_places.triples((subj, lot_lat, None)):
        df.loc[idx,'lot_lat'] = o


df['lot_long'] = 'missing'
lot_long = URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#long')
for idx, row in df.iterrows():
    subj_url = row.lot_location
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in result_places.triples((subj, lot_long, None)):
        df.loc[idx,'lot_long'] = o

df.to_csv('r_instabilities.csv', index=False)
df.to_json('r_instabilities.json')


#INTERVENTIoNS MINING

intervention_subj = search_rendis_subj(rendis, type_data, intervention, 'set')
print(intervention_subj)

intervention_preds = search_rendis_preds(rendis, intervention_subj, 'set')
print(intervention_preds)

I_location = search_rendis_obj(rendis, intervention_subj, primGeo, 'analysis')
print(I_location)

type_data = URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type') 
I_type = search_rendis_obj(rendis, intervention_subj, type_data, 'analysis')
print(I_type)

ref = URIRef('http://purl.org/dc/terms/isReferencedBy')
I_ref = search_rendis_obj(rendis, intervention_subj, ref, 'analysis')
print(I_ref)

ref_preds = search_rendis_preds(rendis, I_ref, 'set')
print(ref_preds)

autority_role = URIRef('http://dati.isprambiente.it/ontology/core#role')
A_role = search_rendis_obj(rendis, I_contracting, autority_role, 'analysis')
print(A_role)



agreement = URIRef('http://dati.isprambiente.it/ontology/core#hasAgreement')
I_agreement = search_rendis_obj(rendis, intervention_subj, agreement, 'analysis')
print(I_agreement)

agreement_preds = search_rendis_preds(rendis, I_agreement, 'set')
print(agreement_preds)

data_int = {}

data_int['intervention'] = []
data_int['location'] = []

for intervention_url in intervention_subj:
    df_instability = URIRef(intervention_url)
    value = data_int['intervention']
    if value == None:
        value = list(intervention_url)
    else:
        value.append(intervention_url)
    
    data_int['intervention'] = value


    for s, p, o in rendis.triples((df_instability, primGeo, None)):
        #add related to item
        value2 = data_int['location']
        if value2 == None:
            value2 = list(str(o))
        else:
            value2.append(str(o))

df_int = pd.DataFrame.from_dict(data_int)


df_int['label'] = 'missing'
label = URIRef('http://www.w3.org/2000/01/rdf-schema#label')
for idx, row in df_int.iterrows():
    subj_url = row.intervention
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, label, None)):
        df_int.loc[idx,'label'] = o

df_int['amount_fin'] = 'missing'
label = URIRef('http://dati.isprambiente.it/ontology/core#amountFinanced')
for idx, row in df_int.iterrows():
    subj_url = row.intervention
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, label, None)):
        df_int.loc[idx,'amount_fin'] = o


df_int['has_agreement'] = 'missing'
for idx, row in df_int.iterrows():
    subj_url = row.intervention
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, agreement, None)):
        df_int.loc[idx,'has_agreement'] = o

df_int['agreement_label'] = 'missing'
label = URIRef('http://www.w3.org/2000/01/rdf-schema#label')
for idx, row in df_int.iterrows():
    subj_url = row.has_agreement
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, label, None)):
        df_int.loc[idx,'agreement_label'] = o


df_int['agreement_date'] = 'missing'
date = URIRef('http://purl.org/dc/elements/1.1/date')
for idx, row in df_int.iterrows():
    subj_url = row.has_agreement
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, date, None)):
        df_int.loc[idx,'agreement_date'] = o


df_int['instability_type'] = 'missing'
inst_type = URIRef('http://dati.isprambiente.it/ontology/core#officialInstabilityType')
for idx, row in df_int.iterrows():
    subj_url = row.intervention
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, inst_type, None)):
        df_int.loc[idx,'instability_type'] = o

df_int['location_label'] = 'missing'

for idx, row in df_int.iterrows():
    subj_url = row.location
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in result_places.triples((subj, label, None)):
        df_int.loc[idx,'location_label'] = o
        # print(str(o))


df_int['region'] = 'missing'
for idx, row in df_int.iterrows():
    subj_url = row.location
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in result_places.triples((subj, region, None)):
        o = o.split('/')
        df_int.loc[idx,'region'] = o[-1]

df_int['province'] = 'missing'
prov = URIRef('http://www.geonames.org/ontology#parentADM2')
for idx, row in df_int.iterrows():
    subj_url = row.location
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in result_places.triples((subj, prov, None)):
        o = o.split('/')
        df_int.loc[idx,'province'] = o[-1]

df_int['lat'] = 'missing'
lot_lat = URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#lat')
for idx, row in df_int.iterrows():
    subj_url = row.location
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in result_places.triples((subj, lot_lat, None)):
        df_int.loc[idx,'lat'] = o


df_int['long'] = 'missing'
lot_long = URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#long')
for idx, row in df_int.iterrows():
    subj_url = row.location
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in result_places.triples((subj, lot_long, None)):
        df_int.loc[idx,'long'] = o

df_int.to_csv('r_finacing.csv', index=False)
df_int.to_json('r_finacing.json')


#REPAIR MINING

repair_subj = search_rendis_subj(rendis, type_data, repair, 'set')
print(repair_subj)

repair_preds = search_rendis_preds(rendis, repair_subj, 'set')
print(repair_preds)

categ = URIRef('http://dati.isprambiente.it/ontology/core#repairCategory')
R_categ = search_rendis_obj(rendis, repair_subj, categ, 'analysis')
print(R_categ)


R_categ_preds = search_rendis_preds(rendis, R_categ, 'set')
print(R_categ_preds)

rep_type = URIRef('http://dati.isprambiente.it/ontology/core#repairType')
R_type = search_rendis_obj(rendis, repair_subj, rep_type, 'analysis')
print(R_type)

R_type_preds = search_rendis_preds(rendis, R_type, 'set')
print(R_type_preds)
# # #look for types

relation = URIRef('http://dati.isprambiente.it/ontology/core#repairRelatedTo')
R_relation = search_rendis_obj(rendis, repair_subj, relation, 'analysis')
print(R_relation)



#contract to which the relation is related to 
R_relation_preds = search_rendis_preds(rendis, R_relation, 'set')
print(R_relation_preds)
# # #look for types

# # #look for types
# contract is lot of whic inervention
lot_of = URIRef('http://dati.isprambiente.it/ontology/core#isLotOf')
R_relation_lot = search_rendis_obj(rendis, R_relation, lot_of, 'analysis')
print(R_relation_lot)


R_relation_lot_preds = search_rendis_preds(rendis, R_relation_lot, 'set')
print(R_relation_lot_preds)

data_rep = {}

data_rep['repair'] = []

for repair_url in repair_subj:
    df_repair = URIRef(intervention_url)
    value = data_rep['repair']
    if value == None:
        value = list(repair_url)
    else:
        value.append(repair_url)
    
    data_rep['repair'] = value


df_rep = pd.DataFrame.from_dict(data_rep)

df_rep['label'] = 'missing'
label = URIRef('http://www.w3.org/2000/01/rdf-schema#label')
for idx, row in df_rep.iterrows():
    subj_url = row.repair
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, label, None)):
        df_rep.loc[idx,'label'] = o

df_rep['category'] = 'missing'
for idx, row in df_rep.iterrows():
    subj_url = row.repair
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, categ, None)):
        df_rep.loc[idx,'category'] = o

df_rep['category_label'] = 'missing'
label = URIRef('http://www.w3.org/2000/01/rdf-schema#label')
for idx, row in df_rep.iterrows():
    subj_url = row.category
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, label, None)):
        df_rep.loc[idx,'category_label'] = o


df_rep['repair_type'] = 'missing'
for idx, row in df_rep.iterrows():
    subj_url = row.repair
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, categ, None)):
        df_rep.loc[idx,'repair_type'] = o

df_rep['type_label'] = 'missing'
label = URIRef('http://www.w3.org/2000/01/rdf-schema#label')
for idx, row in df_rep.iterrows():
    subj_url = row.repair_type
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, label, None)):
        df_rep.loc[idx,'type_label'] = o


df_rep['relation'] = 'missing'
for idx, row in df_rep.iterrows():
    subj_url = row.repair
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, relation, None)):
        df_rep.loc[idx,'relation'] = o


df_rep['relation_lot'] = 'missing'
for idx, row in df_rep.iterrows():
    subj_url = row.relation
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, lot_of, None)):
        df_rep.loc[idx,'relation_lot'] = o

df_rep['has_agreement'] = 'missing'
for idx, row in df_rep.iterrows():
    subj_url = row.relation_lot   
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, agreement, None)):
        df_rep.loc[idx,'has_agreement'] = o

df_rep['agreement_label'] = 'missing'
label = URIRef('http://www.w3.org/2000/01/rdf-schema#label')
for idx, row in df_rep.iterrows():
    subj_url = row.has_agreement
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, label, None)):
        df_rep.loc[idx,'agreement_label'] = o


df_rep['agreement_date'] = 'missing'
date = URIRef('http://purl.org/dc/elements/1.1/date')
for idx, row in df_rep.iterrows():
    subj_url = row.has_agreement
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, date, None)):
        df_rep.loc[idx,'agreement_date'] = o

#location of the intervention the repair's contract is referred to 
df_rep['relation_lot_loc'] = 'missing'
for idx, row in df_rep.iterrows():
    subj_url = row.relation_lot
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendis.triples((subj, primGeo, None)):
        df_rep.loc[idx,'relation_lot_loc'] = o


df_rep['region'] = 'missing'
for idx, row in df_rep.iterrows():
    subj_url = row.relation_lot_loc
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in result_places.triples((subj, region, None)):
        o = o.split('/')
        df_rep.loc[idx,'region'] = o[-1]

df_rep['province'] = 'missing'
prov = URIRef('http://www.geonames.org/ontology#parentADM2')
for idx, row in df_rep.iterrows():
    subj_url = row.relation_lot_loc
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in result_places.triples((subj, prov, None)):
        o = o.split('/')
        df_rep.loc[idx,'province'] = o[-1]

df_rep['lat'] = 'missing'
lot_lat = URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#lat')
for idx, row in df_rep.iterrows():
    subj_url = row.relation_lot_loc
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in result_places.triples((subj, lot_lat, None)):
        df_rep.loc[idx,'lat'] = o


df_rep['long'] = 'missing'
lot_long = URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#long')
for idx, row in df_rep.iterrows():
    subj_url = row.relation_lot_loc
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in result_places.triples((subj, lot_long, None)):
        df_rep.loc[idx,'long'] = o




df_rep.to_csv('r_intervention.csv', index=False)
df_rep.to_json('r_intervention.json')


