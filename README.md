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

2. Qualcosa sul dissesto idrogeologico 
As the Italian Institute for Environmental Protection and Research, [ISPRA](oip) (Istituto Superiore per la Protezione e la Ricerca Ambientale), ([ISPRA]()) stated ER's morphology is extremely frigile due to intense weather events and  proneness to landslides of the territory.

3. Perché è mportante ed utile questo lavrintense methereological or dato il contesto di cui sopra?




 Dati sulle alluvioni e sulle calamità costiere in emilia romagna,
 incrociati con i lavori di prevenzine e ricostruzione.

## DATASETS:
Almeno 2

- uno sulla situazione idrica, quindi: calamità idriche come alluvioni, mareggiate, trremoti 
- uno sulle iniziative: preventivo e riparativo (distinguwre tipo iniziative: pub/priv, naz/regio/internaz)
## SOFTWARES:

**dbfconv.py** converts .dbf files into .csv files for analysis puprposes
**geoconv.py** converts places' names into latitude and longitude coordinates, in rder to locate them on maps.

## CONVERTED AND USEFUL DATASETS.

### Source:
*MinERva:*

https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2022-01-04t151636

### Dataset:
*Opere di difesa costiera - 2020*

Il 'Catalogo delle opere di difesa' contiene le informazioni relative alle protezioni costiere presenti sia a mare che nell'entroterra del litorale emiliano-romagnolo. Tali opere sono state erette nel tempo da parte di enti diversi, allo scopo di difendere le spiagge dal fenomeno dell'erosione e l'entroterra dagli allagamenti in occorrenza degli eventi di alta marea eccezionale.

### Source:
*MinERva:*

https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2021-03-12t110331

### Dataset:
*Dinamica Meteomarina ed Impatti - Località colpite (numero eventi con impatto) mareggiate 1946-2020*


Le cartografie riassumono la distribuzione dei diversi tipi di danno registrati lungo la costa regionale nel periodo 1946-2020, in occasione di eventi di mareggiata. Le mappe illustrano infatti le località che sono state colpite con maggiore ricorrenza dalle mareggiate e la tipologia di danno subito. Le località riportate sono quelle che ricorrono con maggior frequenza nelle segnalazioni (generalmente con più di 5 segnalazioni) mentre i vari generi di impatto sono state sintetizzate in cinque categorie: E: erosione della spiaggia e della duna. I: sommersione per ingressione marina. T: tracimazione dei canali e dei porto-canali. D: danni alle opere marittime e di difesa. B: danni agli stabilimenti balneari e alle infrastrutture. I dati combinano le informazioni contenute nel lavoro 'Le mareggiate e gli impatti sulla costa in Emilia-Romagna 1946-2010' (pubblicato al indirizzo https://ambiente.regione.emilia-romagna.it/it/geologia/pubblicazioni/libri/mareggiate-impatti-costa-Emilia-Romagna) con i dati archiviati nella banca dati regionale denominata in_Storm dal 2011 al 2020 (pubblicato al indirizzo https://ambiente.regione.emilia-romagna.it/it/geologia/geologia/costa/pdf/mareggiate-e-impatti_al-2020_indicatori-e-tendenze_contributo-sgss-alla-smacc_macro3-4.pdf/view)




#### Dati disponibili corsi d'acqua:

**Constrolo qualità fiumi, utile perché hanno anche gli id**

https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/rete-regionale-per-la-qualita-ambientale-acque-superficiali-fluviali-dati-2010-2020/resource/25b540a9-012e-48ae-bddf-54a94b252732

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

**Banca dati geologica**

https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-14t131444

*Dataset disponibili che potrebbero interessarci:*

* Carta Inventario delle frane e Archivio storico delle frane
https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-14t131444/resource/743a65a3-2c8b-4e44-b041-064372358715


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


## Footnotes


[^1] cfr. Unesco's definition of Water-Disasters at https://en.unesco.org/themes/water-security/hydrology/water-related-disasters