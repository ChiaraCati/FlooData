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

While looking for data and other helpful information on hydrogeological damages in Emilia-Romagna we found out ISPRA itself has made available a project on Open Data:[LinkedIspra] following W3S guidelines on Linked Open Data.

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
Containing information on hydrogeological penomena happening in areas that have been striked by 2012 earthquake. Data are recordered from 2012, and are still kept updated.

More info on licence: https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-13t115808/resource/8072010d-870a-426f-a5dd-67dd44f6dc98

* *[Banca dati geologica, 1:10.000 - Frane, depositi di versante e depositi alluvionali - 10k:](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-14t131444)* containing information on disruptions happening in Emilia-ROmagna since 1982 untill 2018. In this datasets we also found geospatial data – including the name of the location, and descriptive data of diruptions' state, nature, etc. 
    
dataset: Coperture_quaternarie_10K.csv



* *[Direttiva Alluvioni 2019 II Ciclo - Ambito Regione Emilia-Romagna - Bacini regionali romagnoli, rischio, geometria puntuale:](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2020-05-31t195733)*
    La cartografia rappresenta gli elementi a rischio con geometria PUNTUALE che possono subire potenziali conseguenze negative derivanti dalle alluvioni relativamente all'ambito dell'Unit of Management (UoM) bacini regionali romagnoli (ITR081), combinando la probabilità di allagamento con la vulnerabilità ai fenomeni alluvionali e con il valore degli elementi esposti, classifica il territorio in 4 classi di rischio, R1 (moderato), R2 (medio), R3 (elevato), R4 (molto elevato), ai sensi del D.P.C.M. 29 settembre 1998.
    
    * Dataset on coast points: RUOM_Aree_Costiere_Marine_ITR081FRMRERPOINT_2019.csv 

    * Dataset on mainland points: RUOM_Reticolo_Principale_ITR081FRMRERPOINT_2019.csv


* *[Opere di difesa costiera - 2020](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2022-01-04t151636)*

Il 'Catalogo delle opere di difesa' contiene le informazioni relative alle protezioni costiere presenti sia a mare che nell'entroterra del litorale emiliano-romagnolo. Tali opere sono state erette nel tempo da parte di enti diversi, allo scopo di difendere le spiagge dal fenomeno dell'erosione e l'entroterra dagli allagamenti in occorrenza degli eventi di alta marea eccezionale.

Più info sulla licenza: https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2022-01-04t151636/resource/f68b9850-9e24-4bd2-bd89-3ee04b7a4817


*[Dinamica Meteomarina ed Impatti - Località colpite (numero eventi con impatto) mareggiate 1946-2020](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2021-03-12t110331)*


Le cartografie riassumono la distribuzione dei diversi tipi di danno registrati lungo la costa regionale nel periodo 1946-2020, in occasione di eventi di mareggiata. Le mappe illustrano infatti le località che sono state colpite con maggiore ricorrenza dalle mareggiate e la tipologia di danno subito. Le località riportate sono quelle che ricorrono con maggior frequenza nelle segnalazioni (generalmente con più di 5 segnalazioni) mentre i vari generi di impatto sono state sintetizzate in cinque categorie: E: erosione della spiaggia e della duna. I: sommersione per ingressione marina. T: tracimazione dei canali e dei porto-canali. D: danni alle opere marittime e di difesa. B: danni agli stabilimenti balneari e alle infrastrutture. I dati combinano le informazioni contenute nel lavoro 'Le mareggiate e gli impatti sulla costa in Emilia-Romagna 1946-2010' (pubblicato al indirizzo https://ambiente.regione.emilia-romagna.it/it/geologia/pubblicazioni/libri/mareggiate-impatti-costa-Emilia-Romagna) con i dati archiviati nella banca dati regionale denominata in_Storm dal 2011 al 2020 (pubblicato al indirizzo https://ambiente.regione.emilia-romagna.it/it/geologia/geologia/costa/pdf/mareggiate-e-impatti_al-2020_indicatori-e-tendenze_contributo-sgss-alla-smacc_macro3-4.pdf/view)

Suscettibilita_costa_combinata




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

## General Analysis 
In order to carry out our analysis, we chose to use those dataset among the above mentioned.

| ID | Title | Link | Time span | Licence |
| :---         |     :---     |     :---     |     :---     |         :--- |

##
## Footnotes


[^1] cfr. Unesco's definition of Water-Disasters at https://en.unesco.org/themes/water-security/hydrology/water-related-disasters