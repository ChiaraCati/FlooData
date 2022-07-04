# FlooData
 Project for Open Access and Digital ethics.

## Introduction 

FlooData is a project developed by Chiara Catizone and Giulia Venditti for the final exam of the course *Open Access and Digital Ethics* held by professor Monica Palmirani at the Master Course of Digital Humanities and Digital Knowldge (Univesity of Bologna) during the A.Y. 2021/2022.

The project's aim is to make a valuable reuse of idrogeological Open Data concerning the Italian Region of Emilia-Romagna.

Our first objective is to analyze if there is a relationship between idrogeological damages and the measures undertaken by different actors consdering them at local, national and (maybe) international level.  

Damages were, then, divided into two categories:

* **Damages on the coast** (mostly damages caused by sea events)
* **Damages on the mainland** (damages cused by floods and earth-quakes)

This distinction was introduced as we elaborated our second objective: whether there is a distinction in terms of risk perception towards these two different areas[^1].

Finally, information on damages has been crossed with information on different kind of activities, mainly distinguishing between preventive measures and reparatory interventions. This further distinction was made with the aim to make explicit the amount of involvement of local and larger scale institutions (both from the private and public, if possible) in the preservation of this territory.


## Scenario


Emilia-Romagna is the sixth widest region in Italy in terms of surface area.and it has a variegated hydrogeological conformation. This variety offers a moltitude of ecoystems currently undergoing drastic transformations due to climate change as stated by the Emilia-Romagna's *Regional Environmental Protection Agency* ( [ARPAE](https://www.arpae.it/it) ) in its report on [Climate change in Emilia-Romagna](https://agricoltura.regione.emilia-romagna.it/produzioni-agroalimentari/temi/bio-agro-climambiente/cambiamento-climatico-in-emilia-romagna). The increasemnt of temperatures is now affecting stability of natural water sources as well as the wellbeing of water surfaces and rivers on mainland and the preservation of coast areas. 


As the Italian Institute for Environmental Protection and Research (Istituto Superiore per la Protezione e la Ricerca Ambientale), [ISPRA](https://www.isprambiente.gov.it/it), stated ER's morphology is extremely frigile due to intense weather events and  proneness to landslides of the territory.

3. Perché è importante ed utile questo lavrintense methereological or dato il contesto di cui sopra?

Through this project our aim is to give a clear view over risky areas triangulated with quantitative data on chatastrophic events and data on related activities(formulare un po' meglio).s

### ISPRA

While kooking fo data and other helpful information on hydrogeological damages in Emilia-Romagna we found out ISPRA itself has made available a project on Open Data:[LinkedIspra] following W3S guidelines on Linked Open Data.

Here the institution makes available 5 different OA datasets, queriable trough an endpoint API made available using Virtuoso. 
**The datasets are the following ones:**(da tradurre)
* *ReNDiS:* Il Repertorio Nazionale degli interventi per la Difesa del Suolo
* *CdS:* Il consumo di suolo in Italia
* *RMN:* La Rete Mareografica Nazionale
* *RON:* Rete Ondametrica Nazionale
* *Luoghi:* Dai sistemi cartografici dell’ISPRA i dati delle regioni, delle province e dei comuni d’Italia (Elaborazioni su fonte Istat).
Il dataset dei luoghi è di primaria importanza per l’integrazione delle differenti fonti di origine.

[ReNDIs](http://dati.isprambiente.it/dataset/il-rendis/) is the most valuable dataset for us as it contains: (da capire se i dati dell'endpoint sono aggionrati ad oggi  al 2016 )
* Information on interventions
* Information on associated lots
* Georeferencing of interventions
* Projects' financial budgets 
* Disruptions' typologies, lithologies  e realized works
* Classification of hydrogeological disruptions and of works made for protecting the soil (in SKOS format)



### MinERva

Other information on hydrogeological disasters has been retrieved from [MinERva](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset)'s catalogue filtering only those datasets sets that made available Open Data formats.

Here we found tot datasets useful for retrieving information on Hydrogeolodical disasters, as well as data on floodings and on the management of coasts and related calamities. 

**Disasters data:**

* *[Segnalazioni fenomeni geologici particolari:](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-13t115808)* 
    containing information on hydrogeological penomena happening in areas that have been striked by 2012 earthquake. Data are recordered from 2012, and are still kept updated.

    * Dataset: Segnalazioni_fenomeni_geologici.csv
    * More info on licence: https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-13t115808/resource/8072010d-870a-426f-a5dd-67dd44f6dc98
    

* *[Banca dati geologica, 1:10.000 - Frane, depositi di versante e depositi alluvionali - 10k:](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-14t131444)* 
    containing information on disruptions happening in Emilia-ROmagna since 1982 untill 2018. In this datasets we also found geospatial data – including the name of the location, and descriptive data of diruptions' state, nature, etc. 
    
    * Dataset: Coperture_quaternarie_10K.csv
    * More info on licence: https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-14t131444/resource/45092acf-cca2-42c5-805c-fda27bc97135?inner_span=True
    


* *[Direttiva Alluvioni 2019 II Ciclo - Ambito Regione Emilia-Romagna - Bacini regionali romagnoli, rischio, geometria puntuale:](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2020-05-31t195733)*
    La cartografia rappresenta gli elementi a rischio con geometria PUNTUALE che possono subire potenziali conseguenze negative derivanti dalle alluvioni relativamente all'ambito dell'Unit of Management (UoM) bacini regionali romagnoli (ITR081), combinando la probabilità di allagamento con la vulnerabilità ai fenomeni alluvionali e con il valore degli elementi esposti, classifica il territorio in 4 classi di rischio, R1 (moderato), R2 (medio), R3 (elevato), R4 (molto elevato), ai sensi del D.P.C.M. 29 settembre 1998.

    * Dataset on coast points: RUOM_Aree_Costiere_Marine_ITR081FRMRERPOINT_2019.csv 
    * More info in licence: https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2020-05-31t195733/resource/fe415132-b4ea-4f76-a76b-748b9ab22afe?inner_span=True
    * Dataset on mainland points: RUOM_Reticolo_Principale_ITR081FRMRERPOINT_2019.csv
    * More info in licence: https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2020-05-31t195733/resource/4e9a9ce2-065b-41c9-9bc9-406f59c19f8e?inner_span=True

* **Related human activities** (both preventive measures and reparatory acts)**

* *[Opere di difesa costiera - 2020](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2022-01-04t151636)*

    Il 'Catalogo delle opere di difesa' contiene le informazioni relative alle protezioni costiere presenti sia a mare che nell'entroterra del litorale emiliano-romagnolo. Tali opere sono state erette nel tempo da parte di enti diversi, allo scopo di difendere le spiagge dal fenomeno dell'erosione e l'entroterra dagli allagamenti in occorrenza degli eventi di alta marea eccezionale.

    * Dataset: Opere_Difesa_2020.csv
    * Più info sulla licenza: https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2022-01-04t151636/resource/f68b9850-9e24-4bd2-bd89-3ee04b7a4817


### OpenCoesione

[OpenCoesione](https://opencoesione.gov.it/it/) by the Italian Government has been another useful resolurce, as it makes available data dumps on projects grupoed by Region. 
We downloaded the dataset containing information on projects undertaken in Emilia-Romangna at this url https://opencoesione.gov.it/it/opendata/#!progetti_regione_section.
   
* Dataset: progetti_esteso_EMR_2007-2013_20220228.csv
* Dataset: progetti_esteso_EMR_2014-2020_20220228.csv

X Giulia: Tutti i dati di OpenCoesione sono rilasciati con licenza CC BY 4.0 


## SOFTWARES:

**dbfconv.py** converts .dbf files into .csv files for analysis puprposes

**geoconv.py** converts places' names into latitude and longitude coordinates, in rder to locate them on maps.

## CONVERTED AND USEFUL DATASETS.






#### Da vedere se integrare perchéforse inutili:

**Datibacino Po:**

https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/pai-bacino-fiume-po-fasce-fluviali/resource/1f0b43c4-4bcc-497c-8af4-6ba2cb750c1e

*Dataset disponibili che potrebbero interessarci:*

* Aree inondabili bacino fiume Po:
https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/pai-bacino-fiume-po-fasce-fluviali/resource/1f0b43c4-4bcc-497c-8af4-6ba2cb750c1e

**Dati  bacino Reno:**

https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/pai-bacino-fiume-po-fasce-fluviali


*Dataset disponibili che potrebbero interessarci:*

* Aree alta probabilità inondazione fiume Reno:
https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/pai-bacino-reno-rischio-idraulico-e-assetto-della-rete-idrografica/resource/1408fbe8-fe7f-4a61-aba5-b5ed7bc8ee07

* localizzazione delle situazioni a rischio elevato o molto elevato:
https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/pai-bacino-reno-rischio-idraulico-e-assetto-della-rete-idrografica/resource/c84abc40-4543-4612-b210-99627fa6bfcf


#### Dati finanziamenti per interventi:
Analisi etica a partire da quello dei terremoti 

**Finanziamenti Piani di Azione Ambientali**

Elenco dei finanziamenti per gli interventi previsti dal Piano di Azione Ambientale, dati aggiornati al 2021 

https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/finanziamenti-piani-di-azione-ambientali-1523630733363-1846

**FIN_Bonifiche Mezzi statali**
Ci sono un paio di bonifiche a dei torrenti può torare utile da aggregare ad altre info 
https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/finanziamenti-statali-bonifiche-1523630733354-1846/resource/8cc2700c-f21c-47c5-9041-2d7b0f4eb375


**FIN_Bonifiche Mezzi regionali**
Idem sopra
https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/finanziamenti-regionali-bonifiche-1523630733353-1846/resource/efd3b9b6-7ec9-4cde-972e-72ffe695836e


## Data Inspection 
(testo utile dal sito)
Here insert visualization plus a brif data Analysis. Discourse proposal:

What is the water disaster? How many disasters a year? What is the typology of the water disaster? What is their distribution on the territory?
How potentially harmful are these disasters? (4 types?) Which areas are most affected?
How do humans react to the water disaster? Who finances the initiatives? Are there more preventive or interventional initiatives?
Report interesting foundings over data

## Appunti 


- uno sulla situazione idrica, quindi: calamità idriche come alluvioni, mareggiate, trremoti 
- uno sulle iniziative: preventivo e riparativo (distinguwre tipo iniziative: pub/priv, naz/regio/internaz)


<hr>

---------------------SCHEMA PALMIRANI--------------------------

## Original dataset and mushup dataset(s) 
In order to carry out our analysis, we chose to use those dataset among the above mentioned.

| ID | Title | Link | Time span | Licence |
| :---         |     :---     |     :---     |     :---     |         :--- |
| D1 | ReNDIs | [url](http://dati.isprambiente.it/dataset/il-rendis/) | 2016 - (?) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.it) |
| D2 | Segnalazioni fenomeni geologici particolari | [url](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-13t115808) | 2012 - 2022 | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/legalcode.it)|
| D3 | Banca dati geologica, 1:10.000 - Frane, depositi di versante e depositi alluvionali - 10k: | [url](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-14t131444) | 1982 - 2018 | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/legalcode.it)|
| D4 | Direttiva Alluvioni 2019 II Ciclo - Ambito Regione Emilia-Romagna - Bacini regionali romagnoli, rischio, geometria puntuale | [url](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2020-05-31t195733) | 2013 - 2019 | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/legalcode.it)|
| D4 | Opere di difesa costiera - 2020 | [url](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2022-01-04t151636) | 2020 - 2021 | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/legalcode.it)|
| D5 | Dinamica Meteomarina ed Impatti - Località colpite (numero eventi con impatto) mareggiate 1946-2020 | [url](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2021-03-12t110331)| 1946 - 2020 | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/legalcode.it)|

Abbiamo combinato i dati in questo modo (spiegare metodo) e abbiamo ottenuto questo dataset:

| ID | Title | Link | Time span | Licence |
| :---         |     :---     |     :---     |     :---     |         :--- |


## Quality analysis of the datasets
The following criteria must be met in order to manage the level of information quality as set out by the National Guidelines for the Improvement of Public Information Assets in the [Context of Data Quality](https://docs.italia.it/italia/daf/lg-patrimonio-pubblico/it/bozza/aspettiorg.html#qualita-dei-dati):

* *Accurancy*: the data's properties accurately reflect the true worth of the concept or event being referenced;
* *Completness*: the data is comprehensive with regard to all of its expected values and the relevant entities (sources) that contribute to the definition of the procedure;
* *Coherence*: in terms of how the administration's owner uses the data, neither the data nor its attributes can be related to other data;
* *Promptness*: the data, and its attributes, is updated with respect to the procedure to which it refers.

| Dataset | Accurancy | Completness | Coherence | Promptness |
| :---         |     :---     |     :---     |     :---     |         :--- |
| D1        |     :---     |     :---     |     :---     |         :--- |
| D2         |     :---     |     :---     |     :---     |         :--- |
| D3         |     :---     |     :---     |     :---     |         :--- |
| D4         |     :---     |     :---     |     :---     |         :--- |
| D5         |     :---     |     :---     |     :---     |         :--- |
| D6         |     :---     |     :---     |     :---     |         :--- |

## Legal analysis 
Legal analysis is required to ensure the long-term viability of the data generation and dissemination process, as well as to produce a balanced service that is in accordance with the public function and individual rights. As a result, the legal analysis of the sources seeks to assess these precarious balances, emphasising use restrictions, objectives of competence, right determination, and licence conditions.

In order to put this into practise, we evaluated all legal facets of the dataset lifetime using a reference checklist. The check list consists of a series of questions that must be answered with a Yes, No, or Not Verifiable for each aspect.

| Legal issues | D1 | D2 | D3 | D4 | D5 |
| :---         |     :---     |     :---     |     :---     |         :--- |
| 1. Privacy        |     :---     |     :---     |     :---     |         :--- |         :--- |
| 	1.1 Is the dataset free of any personal data as defined in the Regulation (EU) 2016/679?        |     :---     |     :---     |     :---     |         :--- |         :--- |
| 	1.2 Is the dataset free of any indirect personal data that could be used for identifying the natural person?        |     :---     |     :---     |     :---     |         :--- |         :--- |
| 	If so, is there a law that authorize the PA to release them? Or any other legal basis? Identify the legal basis.        |     :---     |     :---     |     :---     |         :--- |         :--- |
| 	1.3 Is the dataset free of any particular personal data (art. 9 GDPR)?        |     :---     |     :---     |     :---     |         :--- |         :--- |
| 	If so is there a law that authorize the PA to release them?        |     :---     |     :---     |     :---     |         :--- |         :--- |
| 		1.4 Is the dataset free of any information that combined with common data available in the web, could identify the person?        |     :---     |     :---     |     :---     |         :--- |         :--- |
| 	If so, is there a law that authorize the PA to release them?        |     :---     |     :---     |     :---     |         :--- |         :--- |
| 		1.5 Is the dataset free of any information related to human rights (e.g. refugees, witness protection, etc.)?       |     :---     |     :---     |     :---     |         :--- |         :--- |
| 		1.6 Do you use a tool for calculating the range of the risk of de-anonymization?        |     :---     |     :---     |     :---     |         :--- |         :--- |
| 	Do you anonymize the dataset? With which technique?        |     :---     |     :---     |     :---     |         :--- |         :--- |
| 		Did you check the three mandatory parameters: singling out, linking out, inference out?        |     :---     |     :---     |     :---     |         :--- |         :--- |
| 		1.7 Are you using geolocalization capabilities ?       |     :---     |     :---     |     :---     |         :--- |         :--- |
| 		Do you check that the geolocalization process can’t identify single individuals in some circumstances?       |     :---     |     :---     |     :---     |         :--- |         :--- |
| 			1.8 Did you check that the open data platform respect all the privacy regulations (registration of the end-user, profiling, cookies, analytics, etc.)?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 			1.9 Do you know who are in your open data platform the Controller and Processor of the privacy data of the system?      |     :---     |     :---     |     :---     |         :--- |         :--- |
| 			1.10 Where are the datasets physically stored (country and jurisdiction)?       |     :---     |     :---     |     :---     |         :--- |         :--- |
| 			Do you have a cloud computing platform?      |     :---     |     :---     |     :---     |         :--- |         :--- |
| 		Have you checked the privacy regulation of the country where the dataset is physically stored? (territoriality)       |     :---     |     :---     |     :---     |         :--- |         :--- |
| 			1.11 Do you have non-personal data?       |     :---     |     :---     |     :---     |         :--- |         :--- |
| 		2. IPR of the dataset       |     :---     |     :---     |     :---     |         :--- |         :--- |
| 		2.1 Have you created and generated the dataset ?       |     :---     |     :---     |     :---     |         :--- |         :--- |
| 		2.2 Are you the owner of the dataset? Who is the owner?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 		2.3 Are you sure to not use third party data without the proper authorization and license ?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 		Are the dataset free from third party licenses or patents?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 		2.4 Have you checked if there are some limitations in your national legal system for releasing some kind of datasets with open license?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 			3. Licenses     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 			3.1 Do you release the dataset with an open data license ?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 		In case of the use of CC0 do you check that you have all the right necessary for this particular kind of license (e.g., jurisdiction)?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 			3.2 Do you include the clause: "In any case the dataset can’t be used for re-identifying the person" ?    |     :---     |     :---     |     :---     |         :--- |         :--- |
| 		3.3 Do you release the API (in case you have) with an open source license ?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 			3.4 Do you check that the open data/API platform license regime is compliance with your IPR policy?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 				Do you have all the licences related to the open data platform/API software?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 				4. Limitations on public access     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 				4.1 Do you check that the dataset concerns your institutional competences, scope and finality?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 					Do you check if the dataset concerns other public administration competences?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 				4.2 Do you check the limitations for the publication stated by your national legislation or by the EU directives ?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 				4.3 Do you check if there are some limitations connected to the international relations, public security or national defence ?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 				4.4 Do you check if there are some limitations concerning the public interest ?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 				4.5 Do you check the international law limitations ?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 				4.6 Do you check the INSPIRE law limitations for the spatial data?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 				5. Economical Conditions     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 				5.1 Do you check that the dataset could be released for free ?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 				5.2 Do you check if there are some agreements with some other partners in order to release the dataset with a reasonable price ?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 				5.3 Do you check if the open data platform terms of service include a clause of “non liability agreement” regarding the dataset and API provided ?   |     :---     |     :---     |     :---     |         :--- |         :--- |
| 				5.4 In case you decide to release the dataset to a reasonable price do you check if the limitation imposed by the new directive 2019/1024/EU are respected ?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 				Are you able to calculate the “marginal cost”?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 				Are you able to justify the “reasonable return on investment” limited to cover the costs of collection, production, reproduction, dissemination, preservation and rights clearance?    |     :---     |     :---     |     :---     |         :--- |         :--- |
| 					There is a national law that justify your public administration to apply the “reasonable return of investment”?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 						5.5 In case you decide to release the dataset to a reasonable price do you check the e-Commerce directive1 and regulation?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 			6. Temporary aspects     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 					6.1 Do you have a temporary policy for updating the dataset?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 					6.2 Do you have some mechanism for informing the end-user that the dataset is updated at a given time to avoid mis-usage and so potential risk of damage ?     |     :---     |     :---     |     :---     |         :--- |         :--- |
| 				6.3 Did you check if the dataset for some reason can’t be indexed by the research engines (e.g. Google, Yahoo, etc.) ?   |     :---     |     :---     |     :---     |         :--- |         :--- |
| 				6.4 In case of personal data, do you have a reasonable technical mechanism for collecting request of deletion (e.g. right to be forgotten)?     |     :---     |     :---     |     :---     |         :--- |         :--- |


## Ethical analysis 

## Technical analysis 


## Sustainability
The data sets used to create Floodata, which examines the dangers by flooding catastrophes and related interventions in the Emilia Romagna area, come from a variety of sources. The original datasets used for this project are currently being maintained by the appropriate institutions or organisations, but this site was created as the final project for the [Open Access and Digital Ethics](https://www.unibo.it/it/didattica/insegnamenti/insegnamento/2020/424645) course of the Master's Degree Course in [Digital Humanities and Digital Knowledge](https://corsi.unibo.it/2cycle/DigitalHumanitiesKnowledge) (a.y. 2021/22) at the [University of Bologna](https://www.unibo.it/it). The dataset is not actively maintained.

## License

## Visualizations

## RDF assertation of data

## Final remarks

## Footnotes


[^1] cfr. Unesco's definition of Water-Disasters at https://en.unesco.org/themes/water-security/hydrology/water-related-disasters