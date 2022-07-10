
import pprint
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
# create an empty Graph for the rendmi dataset and parse a local RDF file by specifying the format into the graph
path1 = '/Users/chiara/Documents/GitHub/Owater/datasets/originals/dissesto_07_06_2022.nt'
rendmi_data = rdflib.Graph()
rendmi = rendmi_data.parse(path1, format='nt')

# create an empty Graph for places dataset and parse a local RDF file by specifying the format into the graph
places_data = rdflib.Graph()
result_places = places_data.parse("../datasets/originals/luoghi.nt", format='nt')


#urls for types of records we are looking for 
instability = URIRef('http://dati.isprambiente.it/ontology/core#Instability') 
intervention = URIRef('http://dati.isprambiente.it/ontology/core#Intervention')
repair = URIRef('http://dati.isprambiente.it/ontology/core#Repair') 


#functions for searching stuff

def search_rendmi_subj(dataset, pred, obj, string):
    support = list()
    
    if string == 'print':
        for s, p, o in dataset.triples((None, pred, obj)):
            print(str(s))
    if string == 'set':
        
        for s, p, o in dataset.triples((None, pred, obj)):
            support.append(str(s))
    return support 

def search_rendmi_preds(dataset, subjects_list, string):
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
def search_rendmi_obj(dataset, subjects_list, pred, string):
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

    if dataset == 'rendmi':
        my_data = rendmi
    else:
        my_data ==result_places
    for item_url in items:
        item = URIRef(item_url) 
        support = set()

        for s, p, o in rendmi.triples((item, None, None)):
            support.add(p)
    if  x == 1:
        comparison = support
        x -=1
    else:
        if support != comparison:
            print(item_url, 'has different predicates')


#VARIABLES FOR INSTABILITIES

#look for all instabilities
instability_subj = search_rendmi_subj(rendmi, type_data, instability, 'set')
print(instability_subj)

instability_preds = search_rendmi_preds(rendmi, instability_subj, 'set')
# print(instability_preds)


# preds results are put into variables
instability_group = URIRef('http://dati.isprambiente.it/ontology/core#instabilityGroup')
instability_relatedTo = URIRef('http://dati.isprambiente.it/ontology/core#instabilityRelatedTo')
instability_type = URIRef('http://dati.isprambiente.it/ontology/core#instabilityType')


#look for Emilia-Romagna's instabilities
I_groups = search_rendmi_obj(rendmi, instability_subj, instability_group, 'analysis')
# print(I_groups)


I_relation = search_rendmi_obj(rendmi, instability_subj, instability_relatedTo, 'analysis')
# print(I_relation)

#find predicates of instability relations
I_relation_preds = search_rendmi_preds(rendmi, I_relation, 'set')
# print(I_relation_preds)

main_lot = URIRef('http://dati.isprambiente.it/ontology/core#isLotOf')
I_relation_lot = search_rendmi_obj(rendmi, I_relation, main_lot, 'analysis')
print(I_relation_lot)

I_relation_lot_preds = search_rendmi_preds(rendmi, I_relation_lot, 'set')
# print(I_relation_lot_preds)

# look for lot location
primGeo = URIRef('http://dati.isprambiente.it/ontology/core#primaryGeographicalFeature')
I_relation_lot_location = search_rendmi_obj(rendmi, I_relation_lot, primGeo, 'analysis')
# print(I_relation_lot_location)

# look for locations predicates inside luoghi 
lot_location_preds = search_rendmi_preds(result_places, I_relation_lot_location, 'set')
# print(lot_location_preds)


# look for locations predicates regions inside luoghi 
region = URIRef('http://www.geonames.org/ontology#parentADM1')
I_relation_lot_region = search_rendmi_obj(result_places, I_relation_lot_location, region, 'analysis')
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


    for s, p, o in rendmi.triples((df_instability, instability_relatedTo, None)):
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
    for s, p, o in rendmi.triples((subj, instability_group, None)):
        lot = str(o)
        df.loc[idx,'type'] = lot

df['subtype'] = 'missing'

for idx, row in df.iterrows():
    subj_url = row.instabilities
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendmi.triples((subj, instability_type, None)):
        lot = str(o)
        df.loc[idx,'subtype'] = lot

df['subtypeLabel'] = 'missing'

for idx, row in df.iterrows():
    subj_url = row.subtype
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendmi.triples((subj, label, None)):
        df.loc[idx,'subtypeLabel'] = o



df['contract_lot'] = 'missing'

for idx, row in df.iterrows():
    subj_url = row.contract_url
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendmi.triples((subj, main_lot, None)):
        lot = str(o)
        df.loc[idx,'contract_lot'] = lot

df['lot_location'] = 'missing'

for idx, row in df.iterrows():
    subj_url = row.contract_lot
    subj = URIRef(subj_url)
    # print(row.contract_url)
    for s, p, o in rendmi.triples((subj, primGeo, None)):
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






# I_type1 = search_rendmi_obj('rendmi', instability_subj, instability_type, 'analysis')
# print(I_type1)

# I_type2 = search_rendmi_obj('rendmi', instability_subj, type_data, 'analysis')
# print(I_type2)

# I_label = search_rendmi_obj('rendmi', instability_subj, label, 'analysis')
# print(I_label)




# intervention_subj = search_rendmi_subj('rendmi', type_data, intervention, 'set')
# print(intervention_subj)

# repair_subj = search_rendmi_subj('rendmi', type_data, repair, 'set')
# print(repair_subj)

# # #look for types


# # for s, p, o in result.triples((None, type, None)):
# #     types.add(o)

# # print(types)

# # #INTERVENTIONS
# # # interventions = set()
# # # type = URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type') 
# # # intervention = URIRef('http://dati.isprambiente.it/ontology/core#Intervention') 

# # # for s, p, o in result.triples((None, type, intervention)):
# # #     interventions.add(s)

# # # print(list(interventions)[0])


# # #INTERVENTIONS predicates
# # # preds_interventions = set()
# # # intervention = URIRef('http://dati.isprambiente.it/id/ihi/intervention/232/02') 

# # # for s, p, o in result.triples((intervention, None, None)):
# # #     preds_interventions.add(p)

# # # print(preds_interventions)

# # #INTERVENTIONS test

# # # for intervention_uri in interventions:
# # #     intervention_this = URIRef(intervention_uri) 
# # #     pred_this = set()

# # #     for s, p, o in result.triples((intervention, None, None)):
# # #         pred_this.add(p)
    
# # #     if pred_this != preds_interventions:
# # #         print(intervention_this, 'has different predicates')

# # #Instability

# # instabilities = set()
# # type = URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type') 
# # instability = URIRef('http://dati.isprambiente.it/ontology/core#Instability') 

# # for s, p, o in result.triples((None, type, instability)):
# #     instabilities.add(s)

# # print(list(instabilities)[0])

# # #Instability predicates
# # preds_instability = set()
# # instability = URIRef('http://dati.isprambiente.it/id/ihi/instability/108/082di-6') 

# # for s, p, o in result.triples((instability, None, None)):
# #     preds_instability.add(p)

# # print(preds_instability)

# # #Instability test

# # for intervention_uri in instabilities:
# #     instability_this = URIRef(intervention_uri) 
# #     preds_this = set()

# #     for s, p, o in result.triples((instability_this, None, None)):
# #         preds_this.add(p)
    
# #     if preds_this != preds_instability:
# #         p
        
# # #Repair

# # repairs = set()
# # type = URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type') 
# # repair = URIRef('http://dati.isprambiente.it/ontology/core#Repair') 
# # for s, p, o in result.triples((None, type, repair)):
# #     repairs.add(s)
# # print(list(repairs)[0])

# # #Repair predicates
# # preds_repairs = set()
# # repair = URIRef('http://dati.isprambiente.it/id/ihi/repair/036/061sf-32') 

# # for s, p, o in result.triples((repair, None, None)):
# #     preds_repairs.add(p)

# # print(preds_repairs)

# # #Repair test
# # x= 0
# # for repair_uri in repairs:
# #     repair_this = URIRef(repair_uri) 
# #     preds_thiss = set()

# #     for s, p, o in result.triples((repair_this, None, None)):
# #         preds_thiss.add(p)
    
# #     if preds_thiss != preds_repairs:
# #         x +=1
# #         # print(repair_this, 'has different predicates', preds_thiss)

# # print(x)
# # print(len(repairs))


# # #find locality of interventions and 

# # er_interventions = set()
# # geo_feature = URIRef('http://dati.isprambiente.it/ontology/core#primaryGeographicalFeature')
# # parent1 = URIRef('http://www.geonames.org/ontology#parentADM1')
# # emro = URIRef('http://dati.isprambiente.it/id/place/emilia-romagna')

# # for interv in interventions:
# #     for s, p, o in result.triples((interv, geo_feature, None)):
# #         for place, p2, o2 in result_places.triples((o, parent1, None)):
# #           if o2 == emro:
# #             er_interventions.add(str(s))

# # print(er_interventions)

# # #find locations

# # intervention_locations = list()
# # location = URIRef('http://dati.isprambiente.it/ontology/core#primaryGeographicalFeature')
# # for inter in er_interventions:
# #     inter = URIRef(inter)
# #     for s, p, o in result.triples((inter, location, None)):
# #         this_label = str(o)

# #         intervention_locations.append(this_label)

# # print('tot interventions in Emilia_Romagna',len(intervention_locations))
# # intervention_locations = set(intervention_locations)
# # print('tot places in which interventions happen', len(intervention_locations))

# # luoghi_preds = set()


# # for s, p, o in result_places.triples((None, None, None)):
# #     luoghi_preds.add(p)

# # print(luoghi_preds)

# # names_places = {}
# # label = URIRef('http://www.w3.org/2000/01/rdf-schema#label')
# # for urls in intervention_locations:
# #     place = URIRef(urls)
# #     for s, p, o in result_places.triples((place, label, None)):
# #         this_label = str(o)

# #         names_places[urls]=this_label

# # print(names_places)

# # #find provinces
# # province = URIRef('http://www.geonames.org/ontology#parentADM2')
# # for urls, place in names_places.items():
# #     # print(urls)
# #     url = URIRef(urls)
    
# #     for s, p, o in result_places.triples((url, province, None)):
# #         pred = URIRef('http://www.geonames.org/ontology#name')
# #         for s2, p2, o2 in result_places.triples((o,pred, None)):
# #             code = cod_prov[str(o2)]
# #             new_value = [place, code]
# #             names_places[urls]=new_value
# # print(names_places)

# # #add lat and long 
# # lat = URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#lat')
# # long = URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#long')
# # for urls, items in names_places.items():
# #     # print('items:', items)
# #     url = URIRef(urls)
    
# #     for s, p, o in result_places.triples((url, lat, None)):
        
# #         new_value = items
# #         new_value.append(str(o))
# #         names_places[urls]=new_value

# # for urls, items in names_places.items():
# #     # print('items:', items)
# #     url = URIRef(urls)
    
# #     for s, p, o in result_places.triples((url, long, None)):
        
# #         new_value = items
# #         new_value.append(str(o))
# #         names_places[urls]=new_value

       
# # print(names_places)

# # #merge interventions with places
# # loc = URIRef('http://dati.isprambiente.it/ontology/core#primaryGeographicalFeature')

# # final_dict = {}
# # for interv_uri in er_interventions:
# #     inter = URIRef(interv_uri)
# #     for s,p,o in result.triples((inter, loc, None)):
# #         # print(names_places[str(o)])
# #         value = names_places[str(o)]
# #     final_dict[interv_uri]= value

# # pprint.pprint(final_dict)
# # #add label
# # label = URIRef('http://www.w3.org/2000/01/rdf-schema#label')

# # another_dict = final_dict
# # for interv_uri in er_interventions:
# #     print('uri',interv_uri)
# #     inter = URIRef(interv_uri)
# #     old_value = final_dict[interv_uri]
# #     value = []
# #     for s,p,o in result.triples((inter, label, None)):
# #         print(p ,o)
# #         old_value.append(str(o))
# #         print('old= ', interv_uri, old_value)
        
# # #         value.append(str(o))

# # #     old_vaue.append(value)
# # #     # print(new_value)
# # #     another_dict[interv_uri]= new_value
# # # print(another_dict)