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

[ReNDiS](http://dati.isprambiente.it/dataset/il-rendis/) is the most valuable dataset for us as it contains:
* Information on interventions
* Information on associated lots
* Georeferencing of interventions
* Projects' financial budgets 
* Disruptions' typologies, lithologies  e realized works
* Classification of hydrogeological disruptions and of works made for protecting the soil (in SKOS format)

[Luoghi](http://dati.isprambiente.it/dataset/i-luoghi/) was used as suport to gather geographical fata about *interventions*, *repair* and *instabilities*
* Official name
* Latitude and longitude of the centroids
* Polygons (shape)
* Administrative hierarchy
* Istat code
* Link to Linked Data Cloud (ISTAT datiopen, geonames,  dbpedia, etc.)

[IdroGEO](https://idrogeo.isprambiente.it/app/page/open-data), finally is another from which we downloaded the following files:
* comuni_pir.csv
* province_pir.csv

The two files contain landslide and flood risk indicators relating to territory, population, families, buildings, industry and service, cultural heritage.  



### MinERva

Other information on hydrogeological disasters has been retrieved from [MinERva](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset)'s catalogue filtering only those datasets sets that made available Open Data formats.

Here we found tot datasets useful for retrieving information on Hydrogeolodical disasters, as well as data on floodings and on the management of coasts and related calamities. 

**Disasters data:**

* *[Segnalazioni fenomeni geologici particolari:](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-13t115808)* 

    containing information on hydrogeological penomena happening in areas that have been striked by 2012 earthquake. Data are recordered from 2012, and are still kept updated.

    * Dataset: Segnalazioni_fenomeni_geologici.csv
    * More info on licence: https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-13t115808/resource/8072010d-870a-426f-a5dd-67dd44f6dc98
    


* *[Dinamica Meteomarina ed Impatti - Località colpite (numero eventi con impatto) mareggiate 1946-2020:](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2021-03-12t110331)* 

    containing information on the most endangered coast areas in terms of erosion.

    * Dataset: Segnalazioni_fenomeni_geologici.csv
    * More info on licence: https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2021-03-12t110331/resource/90f18d54-991c-4999-bc91-cb6bbff5335c
    


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

### geo_italy 

Is a json file stored in [this GitHubrepository](https://github.com/MatteoHenryChinaski/Comuni-Italiani-2018-Sql-Json-excel) by [Matteo Henry Chinaski](https://github.com/MatteoHenryChinaski), could not find a licence ut it was useful to link municipalities to their coordinates, without the need of a third party API being involved in this task. 


## SOFTWARES:

**dbfconv.py** converts .dbf files into .csv files for analysis puprposes

**geoconv.py** converts places' names into latitude and longitude coordinates, in rder to locate them on maps.

**rdf_parser.py** converts rdf data from ispra into dataframes

## CONVERTED AND USEFUL DATASETS.






<hr>

---------------------SCHEMA PALMIRANI--------------------------

## Original dataset

### Old table
In order to carry out our analysis, we chose to use those dataset among the above mentioned.
| ID | Title | Link | Time span | Licence |
| :---         |     :---     |     :---     |     :---     |         :--- |
| D1 | ReNDIs | [url](http://dati.isprambiente.it/dataset/il-rendis/) | 2016 - 2021 | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.it) |
| D2 | Segnalazioni fenomeni geologici particolari | [url](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-13t115808) | 2012 - 2022 | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/legalcode.it)|
| D3 | Banca dati geologica, 1:10.000 - Frane, depositi di versante e depositi alluvionali - 10k: | [url](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-14t131444) | 1982 - 2018 | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/legalcode.it)|
| D4 | Direttiva Alluvioni 2019 II Ciclo - Ambito Regione Emilia-Romagna - Bacini regionali romagnoli, rischio, geometria puntuale | [url](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2020-05-31t195733) | 2013 - 2019 | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/legalcode.it)|
| D5 | Opere di difesa costiera - 2020 | [url](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2022-01-04t151636) | 2020 - 2021 | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/legalcode.it)|
| D6 | Dinamica Meteomarina ed Impatti - Località colpite (numero eventi con impatto) mareggiate 1946-2020 | [url](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2021-03-12t110331)| 1946 - 2020 | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/legalcode.it)|


### New table
| ID | Title | Link | Time span | Licence |
| :---         |     :---     |     :---     |     :---     |         :--- |
| D1 | ReNDIs | [url](http://dati.isprambiente.it/dataset/il-rendis/) | 2016 - 2021 | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.it) |
| D2 | Luoghi | [url](http://dati.isprambiente.it/dataset/i-luoghi/) | 2016 | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.it) |
| D3 | Segnalazioni fenomeni geologici particolari | [url](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-13t115808) | 2012 - 2022 | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/legalcode.it)|
| D4 | Opere di difesa costiera - 2020 | [url](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2022-01-04t151636) | 2020 - 2021 | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/legalcode.it)|
| D5 | Dinamica Meteomarina ed Impatti - Località colpite (numero eventi con impatto) mareggiate 1946-2020 | [url](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2021-03-12t110331)| 1946 - 2020 | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/legalcode.it)|
| D6 | IdroGEO - Comuni pir | [url](https://idrogeo.isprambiente.it/app/page/open-data)| 1946 - 2020 | [ CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.it)|
| D7 | IdroGEO - Province pir | [url](https://idrogeo.isprambiente.it/app/page/open-data)| 1946 - 2020 | [ CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.it)|
| D8 | OpenCoesione - Progetti esteso EMR 2007-2013 | [url](https://opencoesione.gov.it/it/opendata/#!progetti_section)| 1946 - 2020 | [ CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.it)|
| D9 | OpenCoesione - Progetti esteso EMR 2014-2020 | [url](https://opencoesione.gov.it/it/opendata/#!progetti_section)| 2014-2020 | [ CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.it)|

## Quality analysis of the datasets
The following criteria must be met in order to manage the level of information quality as set out by the National Guidelines for the Improvement of Public Information Assets in the [Context of Data Quality](https://docs.italia.it/italia/daf/lg-patrimonio-pubblico/it/bozza/aspettiorg.html#qualita-dei-dati):

* *Accurancy*: the data's properties accurately reflect the true worth of the concept or event being referenced;
* *Completness*: the data is comprehensive with regard to all of its expected values and the relevant entities (sources) that contribute to the definition of the procedure;
* *Coherence*: in terms of how the administration's owner uses the data, neither the data nor its attributes can be related to other data;
* *Promptness*: the data, and its attributes, is updated with respect to the procedure to which it refers.

### Old table
| Dataset | Accurancy | Completness | Coherence | Promptness |
| :---         |     :---     |     :---     |     :---     |     :---   |
| D1        |     :---     |     :---     |     :---     |     Satisfied: the dataset is updated daily, ours is updated untill 6/7/2022 |
| D2         |     Satisfied     |     Not satisfied: 81.91%    |     Satisfied.     |       Not satisfied: Last update was on 31/12/2020 |
| D3         |     Not satisfied: There is no clear meaning of CP_LEGE column.    |     Not satisfied: 71.72%     |     Satisfied.     |         Not satisfied: Last update was on 	05/07/2018 |
| D4         |     Not satisfied: There is no clear meaning of the column names, no explanation of needs for between CODAREA, CODSCEN and AMBTER colums  |     Not satisfied: 58.3%     |     Not satisfied: Arbitrary use of uppercase and lowercase     |         Not satisfied: Last update was on 17/02/2022 |
| D5         |     Not satisfied: There is no clear meaning of some column names   |      Not satisfied: 81.05%     |     Not satisfied: There is no standard of defining "null" values, empty fields remain empty or are filled by "nessuno"     |         Not satisfied: Last update was on 01/01/2021 |
| D6         |     Satisfied.     |     Satisfied.    |     Not satisfied: Arbitrary representation of thousands (AAAAMMDD - e.g. 20090205);     |         Not satisfied: Last update was on 01/01/2020 |

### New table
| Dataset | Accurancy | Completness | Coherence | Promptness |
| :---         |     :---     |     :---     |     :---     |     :---   |
| **D1 and D2\***       |   Satisfied, it creates meaningful links between different kind of records (e.g., geological instabilities are linked to and their respective repairs link to the same contract, and when ossible are represented as a group      |     99.16 %    |     Not satisfied: Arbitrary use of uppercase and lowercase and uncomprehensible characters in some labels    |  <li>D1: Satisfied: the dataset is updated daily, ours is updated untill 6/7/2022<<li>D2: Not satisfied: last update on 22/03/2016|
| **D3**         |     Satisfied     |     Not satisfied: 81.91%    |     Satisfied.     |       Not satisfied: Last update was on 31/12/2020 |
| **D4**         |     Not satisfied: There is no clear meaning of some column names   |      Not satisfied: 80.4%     |     Not satisfied: There is no standard of defining "null" values, empty fields remain empty or are filled by "nessuno"     |         Not satisfied: Last update was on 01/01/2021 |
| **D5**         |     Satisfied     |     Satisfied: 100%    |     Not satisfied: Arbitrary representation of thousands (AAAAMMDD - e.g. 20090205);     |         Not satisfied: Last update was on 01/01/2020 |
| **D6**         |     Satisfied        |      :---       |      Satisfied, data and variables are coherent and exhaustly explained in dataset's metadata available [here](https://idrogeo.isprambiente.it/app/page/open-data)  |       Satisfied: last update 2021 with new ISTAT codes  |
| **D7**        |     Satisfied        |      :---       |      Satisfied, data and variables are coherent and exhaustly explained in dataset's metadata available [here](https://idrogeo.isprambiente.it/app/page/open-data)  |       Satisfied: last update 2021 with new ISTAT codes  |
| **D8**         |     :---        |      :---       |      :---         |         :---     |
| **D9**         |     :---        |      :---       |      :---         |         :---     |

\* Datasets were merged and sampled down as ReNDiS geographical data relies on Luoghi's. The merged dataframe was sampled down for analysis, as it contained more than a million entries.

Below result retriven by our software [completness.py](software/completness.py):

### Old table
| Dataset | Total values | Null values | Completness |
| :---         |     :---     |     :---     |    :---     |  
| D1         |     :---     |     :---     |    :---     |  
| D2         |     763     |     138     |    81.91%     |  
| D3         |     587860     |     166254     |    71.72%     |  
| D4         |     9624     |     4021     |    58.3%     |  
| D5         |     38164     |     7232     |    81.05%     | 
| D6         |     48150     |     0     |    100%     |  

### New table
| Dataset | Total values | Null values | Completness |
| :---         |     :---     |     :---     |    :---     |  
| **D1 a D2\***      |     :---     |     :---     |    :---     | 
| **D3**         |     763     |     138     |    81.91%     |  
| **D4**         |     38164     |     7232     |    81.05%     | 
| **D5**         |     48150     |     0     |    100%     |  
| **D6**         |     :---     |     :---     |    :---     |  
| **D7**         |     :---     |     :---     |    :---     |  
| **D8**         |     :---     |     :---     |    :---     |  
| **D9**         |     :---     |     :---     |    :---     |  


## Legal analysis 
Legal analysis is required to ensure the long-term viability of the data generation and dissemination process, as well as to produce a balanced service that is in accordance with the public function and individual rights. As a result, the legal analysis of the sources seeks to assess these precarious balances, emphasising use restrictions, objectives of competence, right determination, and licence conditions.

In order to put this into practise, we evaluated all legal facets of the dataset lifetime using a reference checklist. The check list consists of a series of questions that must be answered with a Yes, No, or Not Verifiable for each aspect.

### Old Table
| **Privacy** | Issues | D1 | D2 |  D3 | D4 | D5 | D6 |
| ----------- | --------| ------|--------|-------|---------|---------|---------|
| | Are the data free from any personal information that can directly identify the individual?  If not, is this information authorized by law?| Yes  | Yes | Yes | Yes | Yes | Yes |
| | Are the data free from any sensitive information that can be traced back to the individual? If not, is this information authorized by law? | yes | yes | yes | yes | yes | yes |
| | Are the data free from any information relating to the subject that, when crossed with data commonly found on the web, can identify the individual? If not, is this information authorized by law? | yes |yes | yes | yes | yes | yes |
| | Are the data free from any record relating to refugees, protected by justice, victims of violence or in any case protected categories? | yes |yes | yes | yes | yes | yes |
| | Did you use a tool to calculate the risk of de-anonymization of your dataset before publishing it? |/ |/|/|/|/| / |
| | Do you display any search services that can filter the data in order to obtain a single geolocated record? | no | no | no | no | no | no |
| **Intellectual Property Rights of the Source** | | |
| | Did you create the data? | no | no | no | no | no | no |
| | Are you the owner of the data even if you did not create it yourself? | no | no | no | no | no | no |
| | Are you sure you are not using data for which there is a third party license or patent? | yes |yes| yes | yes|yes| yes |
| | If the data is not yours, do you have an agreement or license authorizing you to publish it? | yes | yes | yes | yes | yes | yes |
| **Release license** | | |
| | Do you release the data you own with a license? | yes | yes | yes | yes | yes | yes |
| | Have you also included the safeguard clause “In any case, the data cannot be used to re-identify data subjects”? | no|no|no|no|no| no |
| **Limitations on public access** | | |
| | Have you checked that there are no legal or contractual impediments preventing the publication of the data? | yes | yes | yes | yes | yes | yes |
| | Have you checked if there are no security reasons of public order or nationality that prevent you from publishing the data? |yes |yes | yes | yes |yes| yes |
| | Have you checked if there are no reasons related to professional secrecy that prevent the publication of the data? | yes | yes | yes | yes | yes | yes |
| | Have you checked if there are no reasons related to the state secret that prevent the publication of the data? | yes | yes | yes | yes | yes | yes |
| **Economical Conditions** | | |
| | Have you verified that you can release the data for free without breaking any public finance rules? |yes |yes |  yes |yes | yes | yes |
| | If you have imposed economic conditions for using the data, are you sure you have imposed a price to cover only the marginal costs? |/  |/ |/ |/ |/| / |
| **Temporary aspects** | | | 
| | Do you have a temporary policy for updating the dataset? | no|no|no|no|no| no |
| | Do you have some mechanism for informing the end-user that the dataset is updated at a given time to avoid mis-usage and so potential risk of damage? | yes|yes|yes|yes|yes| yes |
| | Are the data updated frequently in order to heal any information that is harmful to people or organizations? | not specified | not specified | not specified | not specified | not specified | not specified |
| | Does the data have legal or jurisprudential prohibitions that prevent it from being indexed by search engines? |no |no|no|no|no|no|

### New Table
**Privacy** | Issues | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 |
| ----------- | --------| ------|--------|-------|---------|---------|---------| ---------|---------------| ---------|
| | Are the data free from any personal information that can directly identify the individual?  If not, is this information authorized by law?| No, indviduals with responsibilities on recorded data can be recognized | Yes  | Yes | Yes | Yes | :---  | :---  | :---  | :---  |
| | Are the data free from any sensitive information that can be traced back to the individual? If not, is this information authorized by law? | No, yes |Yes | Yes | Yes | Yes | :---  | :---  | :---  | :---  |
| | Are the data free from any information relating to the subject that, when crossed with data commonly found on the web, can identify the individual? If not, is this information authorized by law? | No, yes | Yes | Yes | Yes | Yes  | :---  | :---  | :---  | :---  |
| | Are the data free from any record relating to refugees, protected by justice, victims of violence or in any case protected categories? | yes | Yes | Yes | Yes | Yes | :---  | :---  | :---  |
| | Did you use a tool to calculate the risk of de-anonymization of your dataset before publishing it? | / | / | / | / | / | / | / | / | / |
| | Do you display any search services that can filter the data in order to obtain a single geolocated record? | No | No | No | No | No | No  | No  | No  | No  |
| **Intellectual Property Rights of the Source** | | |
| | Did you create the data? | No | No  | No | No | No | No  | No  | No  | No  |
| | Are you the owner of the data even if you did not create it yourself? | No | No  | No | No | No | No  | No  | No  | No  |
| | Are you sure you are not using data for which there is a third party license or patent? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  |
| | If the data is not yours, do you have an agreement or license authorizing you to publish it? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  |
| **Release license** | | |
| | Do you release the data you own with a license? | Yes | Yes  | Yes | Yes | Yes | Ye  | Yes  | Yes  | Yes  |
| | Have you also included the safeguard clause “In any case, the data cannot be used to re-identify data subjects”? | No | No  | No | No | No | No  | No  | No  | No  |
| **Limitations on public access** | | |
| | Have you checked that there are no legal or contractual impediments preventing the publication of the data? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  |
| | Have you checked if there are no security reasons of public order or nationality that prevent you from publishing the data? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  |
| | Have you checked if there are no reasons related to professional secrecy that prevent the publication of the data? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  |
| | Have you checked if there are no reasons related to the state secret that prevent the publication of the data? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  |
| **Economical Conditions** | | |
| | Have you verified that you can release the data for free without breaking any public finance rules? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  |
| | If you have imposed economic conditions for using the data, are you sure you have imposed a price to cover only the marginal costs? | / | / | / | / | / | / | / | / | / |
| **Temporary aspects** | | |
| | Do you have a temporary policy for updating the dataset? | No | No  | No | No | No | No  | No  | No  | No  |
| | Do you have some mechanism for informing the end-user that the dataset is updated at a given time to avoid mis-usage and so potential risk of damage? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  |
| | Are the data updated frequently in order to heal any information that is harmful to people or organizations? | Yes| No | Yes | No, the dataset itself represents a specific year | Not specified | Not specified  | Not specified  | :---  | :---  |
| | Does the data have legal or jurisprudential prohibitions that prevent it from being indexed by search engines? | no | :---  | no | no | no | :---  | :---  | :---  | :---  |
## Ethical analysis 
For our ethical analysis, we took in consideration the main aspects and principles of data ethics: the importance of the human being, transparency, accountability, equality. In addition, we analyzed also if our dataset were free from cognitive bias.

Datasets regarding environmental damage and relative interventions are free of sensitive data since they rely on geographical and amministrative informationn data that are, for their own nature transparent and equal. As averages the data gives information about the region as a whole and do not pose individual privacy risk.

However, we take in account that there are chances of people acting on te collected information to look for more secure and mantained area within the region Emila Romagna, but that does not look like an ethical issue as much as a normal inferencial process granted to common citizens and perfectly sustainable.

## Technical analysis 

**D1**

*Format:* .nt

*Metadata:* 

*URI:*

*Provenance:*

**D2**

*Format:* .nt

*Metadata:* 

*URI:*

*Provenance:*


**D3**

*Format:*

*Metadata:* Information and metadata are provided about owner, contacts, author, date of the catalogue shema, date of dataset, additional information.

*URI:* [https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-13t115808](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-13t115808)

*Provenance:* [Area Geologia, Suoli e Sismica - Settore Difesa del Territorio - Regione Emilia-Romagna](https://ambiente.regione.emilia-romagna.it/it/geologia)



**D4**

*Format:*

*Metadata:* Information and metadata are provided about owner, contacts, author, date of the catalogue shema, date of dataset, additional information.

*URI:* [https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2022-01-04t151636](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2022-01-04t151636)

*Provenance:* [Area Geologia, Suoli e Sismica - Settore Difesa del Territorio - Regione Emilia-Romagna](https://ambiente.regione.emilia-romagna.it/it/geologia)

**D5**

*Format:*

*Metadata:* Information and metadata are provided about owner, contacts, author, date of the catalogue shema, date of dataset, additional information.

*URI:* [https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2021-03-12t110331](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2021-03-12t110331)

*Provenance:* [Area Geologia, Suoli e Sismica - Settore Difesa del Territorio - Regione Emilia-Romagna](https://ambiente.regione.emilia-romagna.it/it/geologia)

**D6**

*Format:* .nt

*Metadata:* 

*URI:*

*Provenance:*

**D7**

*Format:* .nt

*Metadata:* 

*URI:*

*Provenance:*

**D8**

*Format:* .nt

*Metadata:* 

*URI:*

*Provenance:*

**D9**

*Format:* .nt

*Metadata:* 

*URI:*

*Provenance:*

## Mashup and output datasets
Abbiamo combinato i dati in questo modo (spiegare metodo).

A summary table of the produced mashup dataset:

| ID | Domain | XML/SDMX-ML | JSON | CSV |
|  :---     |      :---     |     :---     |     :---     |    :---     |
| MD1         |     :---     |     :---     |     :---     |    :---     |
| MD2         |     :---     |     :---     |     :---     |     :---     |

In doing so, we adhered to the FAIR principles outlined in the [FAIR Data Management Guidelines in Horizon 2020](https://ec.europa.eu/research/participants/data/ref/h2020/grants_manual/hi/oa_pilot/h2020-hi-oa-data-mgt_en.pdf). To put it another way, we worked to make our research data accessible, searchable, interoperable, and reusable (FAIR).Those principles include 3 types of entities: data, metadata and infrastructure. Given the analysis, we can state that our research data are compliant with the FAIR principles.

**Findable:**

* (Meta)data are assigned a unique identifier: both the data we retrieved from the source datasets, the mashed up data, and the metadata we developed in accordance with the DCAT-AP are compatible with this point, providing URI.
* Data are described with rich metadata: we linked a substantial amount of DCAT-AP specification-compliant metadata to our data, including not only all required classes and their corresponding necessary characteristics but also certain suggested and optional features that were helpful for our data.
* Metadata clearly and explicitly include the identifier of the data they describe: we used the DCAT-AP optional attribute for datasets dct:identifier to attach a unique identifier of the data described with the metadata for each dataset that is a part of a catalogue as well as for our own dataset.

**Accessible:**

* (Meta)data are retrievable by their identifier using a standardised communications protocol: all the data we collected and mashed up and the relative metadata are retrievable through the HTTP or its extension HTTPS.
* The protocol is open, free, and universally implementable: HTTP and HTTPS are compliant with these characteristics.
* Metadata are accessible, even when the data are no longer available: metadata will remain accessible from the metadata web page of this web resource.

**Interoperable:**

* (Meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation: the mashed-up data was represented using JSON, CSV, and XML, and the metadata was described and organised using RDF using the Turtle syntax.
* (Meta)data use vocabularies that follow FAIR principles: 

**Reiusable**

* Meta(data) is richly described with a plurality of accurate and relevant attributes: data and metadata are represented by a wide and varied set of labels, such as the date of data collection and change, the licence, the publisher, the originator, and their content.

* (Meta)data are released with a clear and accessible data usage license: The FlooData datasets are made available under the terms of the [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/legalcode.it) Licence, which are specific to the dataset and associated metadata we provided.

* (Meta)data are associated with detailed provenance: in the metadata encoding of our project, data provenance information is provided in a machine-readable way.

* (Meta)data meet domain-relevant community standards: 

## Sustainability
The data sets used to create Floodata, which examines the dangers by flooding catastrophes and related interventions in the Emilia Romagna area, come from a variety of sources. The original datasets used for this project are currently being maintained by the appropriate institutions or organisations, but this site was created as the final project for the [Open Access and Digital Ethics](https://www.unibo.it/it/didattica/insegnamenti/insegnamento/2020/424645) course of the Master's Degree Course in [Digital Humanities and Digital Knowledge](https://corsi.unibo.it/2cycle/DigitalHumanitiesKnowledge) (a.y. 2021/22) at the [University of Bologna](https://www.unibo.it/it). The dataset is not actively maintained.

## License
For the metadata, the documentation and the website we decided to use the same license: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.it). The license for the code is [GNU-GPL](https://www.gnu.org/licenses/gpl-3.0.html).
For the Libraries we used in Javascript, Python and HTML, the licenses are:

| Library | License |
| :---         |     :---     | 
| Bulma | [MIT](https://opensource.org/licenses/mit-license.php)|
| :---         |     :---     | 

Mashed-up datasets is licensed under a [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) License. More about our license:

| | MD1 | MD2 |
| :---         |     :---     |     :---     |  
| Identifier         |     :---     |     :---     |   
| Title         |     :---     |     :---     |  
| Description         |     :---     |     :---     |    
| Modified         |     :---     |     :---     |  
| Theme         |     :---     |     :---     |    
| Rights Holder         |     :---     |     :---     |  
| Subject         |     :---     |     :---     |   
| Publisher         |     :---     |     :---     |  
| Issued         |     :---     |     :---     |    
| Keywords         |     :---     |     :---     |    
| Source         |     :---     |     :---     |    
| Temporal Coverage         |     :---     |     :---     |    
| Spatial Coverage         |     :---     |     :---     |   
| Data Format         |     :---     |     :---     |    
| URL         |     :---     |     :---     |    
| License         |     :---     |     :---     |    
| Download         |     :---     |     :---     |   
| RDF         |     :---     |     :---     |  

## Visualizations
To allow users to make full use of the data, n visualizations have been provided. Abbiamo deciso di investigare questi quesiti che potete trovare nelle sezione data inspection:
* uno
* uno
* uno
* uno

## RDF assertation of data
Their metadata are supplied in accordance with the [DCAT AP version 2.0.0 guidelines](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/200) in order to achieve the goal of providing the user with more reusable and interoperable data. The final dataset's entirety as well as each individual dataset's metadata are supplied.

## Final remarks

## Footnotes

[^1] cfr. Unesco's definition of Water-Disasters at https://en.unesco.org/themes/water-security/hydrology/water-related-disasters