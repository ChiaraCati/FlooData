# 🌊 FlooData

FlooData is a project developed by Chiara Catizone and Giulia Venditti for the final exam of the course *Open Access and Digital Ethics* held by professor Monica Palmirani at the Master Course of Digital Humanities and Digital Knowldge (Univesity of Bologna) during the A.Y. 2021/2022.


## 🎙 Introduction 

Emilia Romagna is the sixth widest region in Italy in terms of surface area and it has a variegated hydrogeological conformation. This variety offers a moltitude of ecoystems currently undergoing drastic transformations due to climate change as stated by the Emilia Romagna's *Regional Environmental Protection Agency* ( [ARPAE](https://www.arpae.it/it) ) in its report on [Climate change in Emilia-Romagna](https://agricoltura.regione.emilia-romagna.it/produzioni-agroalimentari/temi/bio-agro-climambiente/cambiamento-climatico-in-emilia-romagna). Also, the Italian Institute for Environmental Protection and Research (Istituto Superiore per la Protezione e la Ricerca Ambientale), [ISPRA](https://www.isprambiente.gov.it/it), stated Emilia Romagna's morphology is extremely frigile due to intense weather events and  proneness to landslides of the territory.

Our first objective is, thus, the analyis of the relationship between idrogeological damages and the measures undertaken by different actors consdering them at local, national and (maybe) international level.  

Damages were, then, divided into two categories:

* **Damages on the coast** (mostly damages caused by sea events)
* **Damages on the mainland** (damages cused by floods and earth-quakes)

This distinction was introduced as we elaborated our second objective: whether there is a distinction in terms of risk perception towards these two different areas.

Finally, information on damages has been crossed with information on different kind of activities, mainly distinguishing between preventive measures and reparatory interventions. This further distinction was made with the aim to make explicit the amount of involvement of local and larger scale institutions (both from the private and public, if possible) in the preservation of this territory.


Through this project our aim is to give a clear view over risky areas triangulated with quantitative data on chatastrophic events and data on related activities(formulare un po' meglio).


## 🏞 Scenario

**ISPRA** is also the institution that created some Open Data repositories we relied on, when gathering the original data for building FlooData. 
[LinkedIspra](http://dati.isprambiente.it/) is their pilot project oh production of Linked Open Data following W3S guidelines. It is represented by a Catalog (issued in 2016) of 5 datasets:  
* [ReNDiS](http://dati.isprambiente.it/dataset/il-rendis/), the National Directory of Soil Defense Interventions
* [CDS](http://dati.isprambiente.it/dataset/cds/), theLand Consumption in Italy
* [RMN](http://dati.isprambiente.it/dataset/rmn-la-rete-mareografica-nazionale/), the  National Mareographic Network
* [RON](http://dati.isprambiente.it/dataset/ron-rete-ondametrica-nazionale/), the 
National Wave Network
* [Luoghi](http://dati.isprambiente.it/dataset/i-luoghi/), 
the data of the regions from the cartographic systems of ISPRA
</br>

The second project made available by ISPRA we used for creating FlooData is [IdroGEO](https://idrogeo.isprambiente.it/app/), a platform allowing consultation of download and sharing of data, maps, reports, documents of the Italian Landslide Inventory - IFFI. The platform has an [Open Data section](https://idrogeo.isprambiente.it/app/page/open-data) from which it is possible to download data concerning landslides, available in open format and with [CreativeCommons](https://creativecommons.org/) licences. 
</br>
</br>

The fourth platform we used is [MinERva](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset).
MinERva is the point of reference and information sharing held by the Directorate General for Territory and Environment Care of the **[Region of Emilia Romagna](https://www.regione.emilia-romagna.it/)**. It contains various databases classified following the Comprehensive Knowledge Archive Network [(CKAN)](https://ckan.org/) grouping and of the UN 2030 Agenda in [Sustainable Developement Goals](https://www.un.org/en/sustainable-development-goals) che è un sistema open source e basato sul web per la raccolta, la catalogazione e la distribuzione di dati.
</br>
</br>

[OpenCoesione](https://opencoesione.gov.it/it/) – the [Italian government](https://www.governo.it/)'s open gov initiative on cohesion policies in Italy – makes available datasets offering a partial return of the monitoring system managed by the [State General Accounting](http://www.rgs.mef.gov.it/); in a form suitable to respond to the cognitive interests of citizens. In the [Open Data section](https://opencoesione.gov.it/it/opendata/#!progetti_section) datsets on projects are available for download and re-use.

The final data source employed in the constuction of FlooData datasets  is a [GitHub repository](https://github.com/MatteoHenryChinaski/Comuni-Italiani-2018-Sql-Json-excel) by [Matteo Henry Chinaski](https://github.com/MatteoHenryChinaski). The author does not provide a licence or waiver for the data they created. However it is possible to collaborate and freely download data, withouth specifying any legal restricion. The data contained in this resource is of topologycal and topohographical nature as it contains places names, cxoordinates, istat codes, dimensions and  statistics (out of date) of different Italian areas, spanning from single municipalities to the entire natainal territory. 


## 📂 Original and mashed-up datasets

### Original datasets descriptions

**[ReNDiS](http://dati.isprambiente.it/dataset/il-rendis/)** contains information on interventions; associated lots,; georeferencing,; projects' financial budgets; disruptions' typologies, lithologies  and realized works; classification of hydrogeological disruptions and of works made for protecting the soil (in SKOS format)

**[Luoghi](http://dati.isprambiente.it/dataset/i-luoghi/)** was used as suport to gather geographical fata about *interventions*, *repair* and *instabilities*. It contains places's fficial names; latitude and longitude of the centroids; polygons (shape); administrative hierarchy; Istat codes, link to Linked Data Cloud (ISTAT datiopen, geonames,  dbpedia, etc.)

**[Segnalazioni fenomeni geologici particolari](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-13t115808)**, groups reports on particular hydrogeological phenomena made by citizens to the Regional Geological Service since may 2012, in localities hit by that year's hearthquake disaster. The reports were grouped into six categories: gas leaks from water wells and / or from the ground; wells for water with the presence of hot water; fish deaths; presence of fractures and / or subsidence of the ground; appearance of volcanoes of mud and / or sand; water wells dried up.

**[Opere di difesa costiera - 2020](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2022-01-04t151636)** contains information on the coastal protections present both at sea and in the hinterland of the Emilia-Romagna coast. 

**[Dinamica Meteomarina ed Impatti - Località colpite (numero eventi con impatto) mareggiate 1946-2020](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2021-03-12t110331contains)** the name of the moslty eroded areas by calmities that have striken in the time-span 1946-2020

**[IdroGEO - Comuni](https://idrogeo.isprambiente.it/app/page/open-data)** and **[IdroGEO - Province](https://idrogeo.isprambiente.it/app/page/open-data)** contain landslide and flood risk indicators relating to territory, population, families, buildings, industry and service, cultural heritage.  

**[Progetti esteso EMR 2007-2013](https://opencoesione.gov.it/it/opendata/#!progetti_section)** and **[Progetti esteso EMR 2014-2020](https://opencoesione.gov.it/it/opendata/#!progetti_section)** contain track recors of cohesion projects in Emilia Romagna, trasversally describing their management

**[Italy geo](https://github.com/MatteoHenryChinaski/Comuni-Italiani-2018-Sql-Json-excel/blob/master/italy_geo.json)** is a dataset we used to link municipalities and provinces coming from previous datasets to their latitude and longitude coordinates


The below table is a resume of datasets selected for our project, and that have been mashed up to create FlooData final datasets.

| ID | Dataset | Source | Time span | Licence |
| :---         |     :---     |     :---     |     :---     |    :--- |   
| **D1** | [ReNDIs](http://dati.isprambiente.it/dataset/il-rendis/) | [LinkedIspra](http://dati.isprambiente.it/) | 2016 - 2021 | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.it) |
| **D2** | [Luoghi](http://dati.isprambiente.it/dataset/i-luoghi/) | [LinkedIspra](http://dati.isprambiente.it/) | 2016 | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.it) |
| **D3** | [Segnalazioni fenomeni geologici particolari](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-13t115808) | [MinERva](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset) | 2012 - 2022 | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/legalcode.it)|
| **D4** | [Opere di difesa costiera - 2020](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2022-01-04t151636) | [MinERva](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset) | 2020 - 2021 | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/legalcode.it)|
| **D5** | [Dinamica Meteomarina ed Impatti - Località colpite (numero eventi con impatto) mareggiate 1946-2020](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2021-03-12t110331)| [MinERva](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset) | 1946 - 2020 | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/legalcode.it)|
| **D6** | [Comuni](https://idrogeo.isprambiente.it/app/page/open-data) |  [IdroGEO](https://idrogeo.isprambiente.it/app/) | 2017 | [CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.it)|
| D7 | [Province](https://idrogeo.isprambiente.it/app/page/open-data) |  [IdroGEO](https://idrogeo.isprambiente.it/app/) | 2017 | [CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.it)|
| **D8** | [Progetti esteso EMR 2007-2013](https://opencoesione.gov.it/it/opendata/#!progetti_section) | [OpenCoesione](https://opencoesione.gov.it/it/) | 2007-2013 | [CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.it)|
| **D9** | [Progetti esteso EMR 2014-2020](https://opencoesione.gov.it/it/opendata/#!progetti_section) | [OpenCoesione](https://opencoesione.gov.it/it/) | 2007-2013 | [CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.it)|
| **D10** | [Italy geo](https://github.com/MatteoHenryChinaski/Comuni-Italiani-2018-Sql-Json-excel/blob/master/italy_geo.json) | [Comuni-Italiani-2018 GitHub](https://github.com/MatteoHenryChinaski/Comuni-Italiani-2018-Sql-Json-excel) | 2014-2018 | Not specified |
</br>

### Mashed-up datasets descriptions

**[Activities](datasets/final_dataset/actions.csv)** is the mashed-up dataset containing data about reparatoriy and preventive interventions on hydrogeological disasters involving Emilia Romagna.

**[Disruptions](datasets/final_dataset/disruptions.csv)** is the mashed-up dataset containing data about hydrogeological disasters involving Emilia Romagna.

**[Municipality](datasets/final_dataset/municipality.csv)** is the mashed-up dataset containing data on floading risk, area anf geographical information of Emilia Romagna's municipalities.

**[Province](datasets/final_dataset/province.csv)** is the mashed-up dataset containing data on floading risk, area anf geographical information of Emilia Romagna's provinces.

The below table is a resume of datasets created by FlooData, containing  information on hydrogeological disasters, interventions and geographical data useful for their visualization on maps anf other graphs.

| ID | Dataset | Original dataset | Time span | Licence |
| :---         |     :---     |     :---     |     :---     |    :--- |   
| **MD1** | [Activities](datasets/final_dataset/actions.csv) | **D1**,**D2**,**D4**,**D8**,**D9**,**D10** | 2016 - 2021 | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.it) |
| **MD2** | [Disruptions](datasets/final_dataset/disruptions.csv) | **D1**,**D2**,**D3**,**D5**,**D10**| 2016 | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.it) |
| **MD3** | [Municipality](datasets/final_dataset/municipality.csv) | **D6**, **D10**| 2012 - 2022 | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.it)|
| **MD4** | [Province](datasets/final_dataset/province.csv) | **D7**,**D10** | 2020 - 2021 | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.it)|


## 💎 Quality analysis of the datasets
The following criteria must be met in order to manage the level of information quality as set out by the National Guidelines for the Improvement of Public Information Assets in the [Context of Data Quality](https://docs.italia.it/italia/daf/lg-patrimonio-pubblico/it/bozza/aspettiorg.html#qualita-dei-dati):

* *Accurancy*: the data's properties accurately reflect the true worth of the concept or event being referenced;
* *Completness*: the data is comprehensive with regard to all of its expected values and the relevant entities (sources) that contribute to the definition of the procedure;
* *Coherence*: in terms of how the administration's owner uses the data, neither the data nor its attributes can be related to other data;
* *Promptness*: the data, and its attributes, is updated with respect to the procedure to which it refers.

| Dataset | Accurancy | Completness | Coherence | Promptness |
| :---         |     :---     |     :---     |     :---     |     :---   |
| **D1 and D2\***       |   Satisfied, it creates meaningful links between different kind of records (e.g., geological instabilities are linked to and their respective repairs link to the same contract, and when ossible are represented as a group      |     Not satisfied: 93.9%    |     Not satisfied: Arbitrary use of uppercase and lowercase and uncomprehensible characters in some labels    |  <li>D1: Satisfied: the dataset is updated daily, ours is updated untill 6/7/2022<<li>D2: Not satisfied: last update on 22/03/2016|
| **D3**         |     Satisfied     |     Not satisfied: 81.9%%    |     Satisfied.     |       Not satisfied: Last update was on 31/12/2020 |
| **D4**         |     Not satisfied: There is no clear meaning of some column names   |      Not satisfied: 80.4%     |     Not satisfied: There is no standard of defining "null" values, empty fields remain empty or are filled by "nessuno"     |         Not satisfied: Last update was on 01/01/2021 |
| **D5**         |     Satisfied     |     Satisfied: 100%    |     Not satisfied: Arbitrary representation of thousands (AAAAMMDD - e.g. 20090205);     |         Not satisfied: Last update was on 01/01/2020 |
| **D6**         |     Satisfied        |       Not satisfied: 99.6%       |      Satisfied |       Satisfied: last update 2021 with new ISTAT codes  |
| **D7** | Satisfied | Not satisfied: 99.7% | Satisfied |      Satisfied: last update 2021 with new ISTAT codes  |
| **D8**         |     Satisfied        |      Not satisfied: 75.8%       |      Satisfied         |         Satisfired: last update may 2022      |
| **D9**         |     Satisfied        |      Not satisfied: 71.1%        |      Satisfied         |         Satisfied: last update may 2022     |
| **D10**         |     Satisfied        |      Satisfied       |      Satisfied          | Not Satisfied: last update 2017 |

\* Datasets were merged and sampled down as ReNDiS geographical data relies on Luoghi's. The resulting merged dataframes  we use as starting point for data mash up, were also used for analysis, as the original df it contained more than a million entries. 

Below we present the quantitative data retriven during our Quality analysis, fully available at [quality.ipynb](software/quality.ipynb):
 

| Dataset | Total values | Null values | Completness |
| :---         |     :---     |     :---     |    :---     |  
| **D1 a D2\***      |     395728     |     35307     |    93.9     |  
| **D3**         |     763     |     138     |    81.9%     |  
| **D4**         |     38164     |     7232     |     80.4%     | 
| **D5**         |     380     |     0     |    100%     |  no
| **D6**         |     979972     |     3500     |    99.6%      |  
| **D7**         |     13161     |     34     |    99.7%     |  
| **D8**         |     3449466    |     835602     |    75.8%     |  
| **D9**         |     6131986     |     1773353     |    71.1%     |  
| **D10**         |     31920     |     3     |    99.9%     |  

\* Datasets were merged and sampled down as ReNDiS geographical data relies on Luoghi's. The resulting merged dataframes  we use as starting point for data mash up, were also used for analysis, as the original df it contained more than a million entries. Values here represent the sum and mean of the merged datasets 

## Legal analysis 
Legal analysis is required to ensure the long-term viability of the data generation and dissemination process, as well as to produce a balanced service that is in accordance with the public function and individual rights. As a result, the legal analysis of the sources seeks to assess these precarious balances, emphasising use restrictions, objectives of competence, right determination, and licence conditions.

### Original Datasets
In order to put this into practise, we evaluated all legal facets of the dataset lifetime using a reference checklist. The check list consists of a series of questions that must be answered with a Yes, No, or Not Verifiable for each aspect.

**Privacy** | Issues | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 |
| ----------- | --------| ------|--------|-------|---------|---------|---------| ---------|---------------| ---------|---------|
| | Are the data free from any personal information that can directly identify the individual?  If not, is this information authorized by law?| No, yes |Yes | Yes | Yes | Yes | Yes  | Yes  | Yes | Yes  | Yes  |
| | Are the data free from any sensitive information that can be traced back to the individual? If not, is this information authorized by law? | No, yes |Yes | Yes | Yes | Yes | Yes  | Yes  | Yes | Yes  | Yes  |
| | Are the data free from any information relating to the subject that, when crossed with data commonly found on the web, can identify the individual? If not, is this information authorized by law? | No, yes | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  | Yes  | Yes  |
| | Are the data free from any record relating to refugees, protected by justice, victims of violence or in any case protected categories? | Yes | Yes | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  | Yes  |
| | Did you use a tool to calculate the risk of de-anonymization of your dataset before publishing it? | / | / | / | / | / | / | / | / | / | / |
| | Do you display any search services that can filter the data in order to obtain a single geolocated record? | No | No | No | No | No | No  | No  | No  | No  | No  |
| **Intellectual Property Rights of the Source** | | |
| | Did you create the data? | No | No  | No | No | No | No  | No  | No  | No  | No  |
| | Are you the owner of the data even if you did not create it yourself? | No | No  | No | No | No | No  | No  | No  | No  | No  |
| | Are you sure you are not using data for which there is a third party license or patent? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  | Yes |
| | If the data is not yours, do you have an agreement or license authorizing you to publish it? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  | No* |
| **Release license** | | |
| | Do you release the data you own with a license? | Yes | Yes  | Yes | Yes | Yes | Ye  | Yes  | Yes  | Yes  | Yes |
| | Have you also included the safeguard clause “In any case, the data cannot be used to re-identify data subjects”? | No | No  | No | No | No | No  | No  | No  | No  | No |
| **Limitations on public access** | | |
| | Have you checked that there are no legal or contractual impediments preventing the publication of the data? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  | Yes |
| | Have you checked if there are no security reasons of public order or nationality that prevent you from publishing the data? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  | Yes |
| | Have you checked if there are no reasons related to professional secrecy that prevent the publication of the data? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  | Yes |
| | Have you checked if there are no reasons related to the state secret that prevent the publication of the data? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  | Yes |
| **Economical Conditions** | | |
| | Have you verified that you can release the data for free without breaking any public finance rules? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  | Yes |
| | If you have imposed economic conditions for using the data, are you sure you have imposed a price to cover only the marginal costs? | / | / | / | / | / | / | / | / | / | / |
| **Temporary aspects** | | |
| | Do you have a temporary policy for updating the dataset? | No | No  | No | No | No | No  | No  | No  | No  | No |
| | Do you have some mechanism for informing the end-user that the dataset is updated at a given time to avoid mis-usage and so potential risk of damage? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  | Yes  |
| | Are the data updated frequently in order to heal any information that is harmful to people or organizations? | Yes| No | Yes | No | Not Verifiable | No|  Not Verifiable  | Yes | Yes | No |
| | Does the data have legal or jurisprudential prohibitions that prevent it from being indexed by search engines? | No | No  | No | No | No | No  | No  | No  | No  | No |

**Licences**


| ID | Dataset | Licence |
| :---         |     :---     |   :--- |   
| **D1** | [ReNDIs](http://dati.isprambiente.it/dataset/il-rendis/) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.it) |
| **D2** | [Luoghi](http://dati.isprambiente.it/dataset/i-luoghi/) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.it) |
| **D3** | [Segnalazioni fenomeni geologici particolari](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-13t115808) | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/legalcode.it)|
| **D4** | [Opere di difesa costiera - 2020](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2022-01-04t151636) | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/legalcode.it)|
| **D5** | [Dinamica Meteomarina ed Impatti - Località colpite (numero eventi con impatto) mareggiate 1946-2020](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2021-03-12t110331)| [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/legalcode.it)|
| **D6** | [Comuni](https://idrogeo.isprambiente.it/app/page/open-data) | [CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.it)|
| D7 | [Province](https://idrogeo.isprambiente.it/app/page/open-data) | [CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.it)|
| **D8** | [Progetti esteso EMR 2007-2013](https://opencoesione.gov.it/it/opendata/#!progetti_section) | [CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.it)|
| **D9** | [Progetti esteso EMR 2014-2020](https://opencoesione.gov.it/it/opendata/#!progetti_section) | [CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.it)|
| **D10** | [Italy geo](https://github.com/MatteoHenryChinaski/Comuni-Italiani-2018-Sql-Json-excel/blob/master/italy_geo.json) | Not specified |


## Ethical analysis 

Under an *ethical* point of view, we considered the importance of the human being, transparency, accountability, and equality. 
Along with this ethical aspects, we also considered other criteria such as sustainable re-use of the data gathered, and presence of information of public interest when choosing **FlooData**'s source data, as we wanted to account for the management of financings (Open Coesione), the presence risk of hydrogeological disasters in the whole area of Emilia-Romagna, the amount of preventive interventions and following reparations. 

The data gathered is managed by producers in a transparent way, as documentation on project and/or datasets, licences, and policies are made available to final users, avoiding cognitive biases and legal misunderstanding in terms of data re-use.


The original datasets mainly represent, envirnmental– and  geodata. This kind of data naturally avoids discriminations, stereotyping, crystallization, distortion of the history, misrepresentation of reality, and manipulation of the cultural identity of a country/community.
As averages the data gives information about the region as a whole and do not pose individual privacy risk.


Data relating to communities of people living in endangered area comes from the two sets coming from ISPRAS's project ***IdroGeo***. 
*D6* and *D7* contain information on families living in areas with high, medium and low flooding risk **(?)**. Even though this information is linked to natural persons, it is made available for public interest purposes, anonimized, and in form of statistical data, in compliance with the Art. 89 of GDPR. Additionally this kind of data – when made public – might be a call to action to sensibilize people on climate change and hydrogeological issues.
Finally, we noticed **ReNDis** makes accessible the names of whom is responsible for recordered interventions. We consider the presence of identity data in this set as legitimate, sice names of public officers are by nature of public domain. 

For ethical requirements we also rely on [Accenture](https://www.accenture.com/us-en)'s Data Ethics Decision Making Guidelines, in particular considering these aspectsl data gathered and presented on Floodata has been downloaded directly from sources website's or other institutional aggregators such as **MinERva** and **OpenCoesione**. 
The datasets used have all been made available for re-use by producers. The reuse of this data on FlooData, is consistent with creators's specific intent of displaying the hydrogeological situation of the studied area.

We take into account that there are chances of people acting on the collected information to look for more secure and mantained area within the region Emila Romagna, but that does not look like an ethical issue as much as a normal inferencial process granted to common citizens.



## Technical analysis 

### Original datasets

**LinkedIspra** data – *D1* and *D2* - is accessible through a Virtuoso sparQL enpoint and rdf triples of the data was available form download. We have chosen to directly download the ReNdmi and Luoghi RDF triples dumps as the SQL EndPoint  didn't ensure back-end stability and reliability during oour research period. 
*Format* of downloaded data is .nt
*Provenance*: [ISPRA](http://dati.isprambiente.it/id/organization/ispra/html)

| Metadata | URI | Description | Modification date | Label | Keywords | Title | Identifier | Type | Publisher | Distribution | Landing Page | Theme | Creator | Accrual Periodicity |  Language | Rights Holder |
| :---  | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **[D1](http://dati.isprambiente.it/id/dissesto/html)** | http://dati.isprambiente.it/id/dissesto/html | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[D2](http://dati.isprambiente.it/id/place/html)** | http://dati.isprambiente.it/id/place/html | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅|  🚫 | ✅ | ✅ | ✅ | ✅| ✅| 


**Minerva**'s datasets – *D3* *D4* and *D5* - are accessible through a Moka viever service available for download as OpenData. 
Along with datasets' metadata, MinERva provides information about responsible body, reference structure, referent, author
 and dates about catalog cards and physical data.
*Format* of downloaded data is .zip from which we extracted a .dbf file
*Provenance*: [ISPRA](http://dati.isprambiente.it/id/organization/ispra/html)


| Metadata | URI | Dataset ID | Other ID | Themes | Sub-themes | Geographic coverage | Geonames URI | Language | Accural Frequency | Version | Creator | Scale  | Conformity | GEMET Category |  Environmental thematic | Spatial |
| :---  | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **[D3](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-13t115808)** | https://mappegis.regione.emilia-romagna.it/moka/ckan/conoscenza_sottosuolo/Segnalazioni_fenomeni_geologici.zip | ✅ | 🚫 | ✅ | 🚫 | ✅ | 🚫 | ✅ | ✅ | 🚫 | 🚫 | ✅ | 🚫 | ✅ | ✅ | ✅ |
| **[D4](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2022-01-04t151636)** | https://mappegis.regione.emilia-romagna.it/moka/ckan/costa/Opere_Difesa_2020.zip | ✅ | 🚫 | 🚫 | 🚫 | ✅ | 🚫 | ✅ | ✅ | 🚫 | 🚫 | ✅ | ✅ |  ✅ | ✅| ✅|
| **[D5](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2021-03-12t110331)** | https://mappegis.regione.emilia-romagna.it/moka/ckan/costa/Localita_colpite_Erosione_1946_2020.zip |✅ | 🚫 | ✅ | 🚫 | ✅ | 🚫 | ✅ | ✅ | 🚫 | 🚫 | ✅ | 🚫 | ✅ | ✅ | ✅| 


[IdroGEO](https://idrogeo.isprambiente.it/app/) data is available for download in different formats: XLS, CSV and JSON. The platform also allows downlloading the .csv file congaining descriptions and source of the columns in the datasets. 
*Format* of downloaded data is .csv
*Provenance*: https://idrogeo.isprambiente.it/app/page/open-data

IRI is not specified and Basic metadata is provided for *D6* and *D7*  such as:
- Title 
- Description with Version and Year
- Licence 
- Format
- Table columns' Metadata



[OpenCoesione](https://opencoesione.gov.it/it/) allows download of open access datasets representing partial renstitutions of the projects they keep track to. It is possible for everyone to download them in .csv and .xls format
*Format* of downloaded data is .csv
*Provenance*: https://opencoesione.gov.it/it/


IRI is not specified and Basic metadata is provided for *D8* and *D9*  such as:
- Title 
- Description
- Licence 
- Format


[Italy geo](https://github.com/MatteoHenryChinaski/Comuni-Italiani-2018-Sql-Json-excel/blob/master/italy_geo.json) datasets can be freely downloaded from github using -curl request or just  by downloading the file. No specific meatdata is provided for the sets, just labels ofthe content. 
*Format* of downloaded data is .json
*Provenance*: https://github.com/MatteoHenryChinaski/Comuni-Italiani-2018-Sql-Json-excel/blob/master/italy_geo.json

[Resume table of source datasets' technical analysis](Originals_table.md)

### Mashup and output datasets

All data processing tasks undertaken for creating the mashed-up datasets were carried out using Python versions 3.9 and 3.10 and built-in/open-source methods.

For creating the new datasets we disposed of two different kinds of file formats:

* NT
* DBF
* CSV
* JSON

#### Pre processing

**N-Triples** files needed to be preprocessed and parsed into datafames. 
To accomplish this we developed a script [rdf_parse.py](software/rdf_parser.py) to merge the ReNDi and Luoghi data in and create three dataframes, containing of data on hydrogeological disruptions, reparations and their financing. 
The script uses the ldflib to parse thr .nt files and through the class Thypology it gathers the main subjects we want to retrieve: instabilities, interventions(financings), and repairs.
Then for each subject we extracted predicates related to them and use them as labels for creating the dataframes' columns. 

For each column to be created we iterated triples formed as <*Object*><*Columnlabel*><*object*> and selected the corresponding object as that cell values.
For insertng geographical datawe started from ReNDiS lots locations and queried the Luoghi dataset loooking for their labels, province, latitude and longitude. 

The resulting dataframes have been temoporarly saved in .csv format for later merging with other datasets. 

**DBF** files have been converted automatically into csv files using the software dbf.py developed for this purpose. The software cnverts the files keeping their original names through the use of dbf_read librry's DBF method to open this kind of file, which is then saved in .csv format.

#### Merging 

The second step consists in the merging of the JSON and CSV files.

The original data has been mashed-up to create the FlooDatas's 4 datasets contained in our catalog.

Using our softwares actions.py and territory .py we created respectively MD1, and MD3/MD4. 

* **actions.py** selects all Emilia-Romagna's projects (subsetting the original dataset when necessary, e.g., DF1), and constructs the columns based on the information we selected from source dataframes. 
Resulting df is then saved into .json and .csv format for future visualization and consultation purposes. 

* **territory.py** is feeded with *DF6* and *DF7*. Here we select interesting classes from the IdroGeo's datasets such as percentages of risk and atention percentages of families, enterprises and cultural heritage. 
To create MD3 we crossed place names contained in D6 with data in *D10* to find with municipalities latitue and longitude coordinates.


Finally MD2 has been produced by selecting and giving a standard name to the columns representing data necessary for our project we the useful columns  of datasets on hydrogeological dissest.
The production workflow in visible in notebook  [Disruptions.ipynb](software/Disruptions.ipynb)

The resulting datasets are composed as listed:

| MD1 Columns |  |  |  |
| - | -  | - | - |
| prov_nameprov_code | municipality| latitude | longitude |
|date | action_type | action_description|tot_action_financing|

| MD2 Columns |   |  |  |
| - | -  | - | - |
| id | type | municipality | prov_code |
| latitude | longitude | date | |

| MD3 Columns |   | | |
| - | -  | - | - |
|prov_name|prov_code|municipality|latitude|longitude|
|area (kmq)|high_hydraulic_risk_area_p3 (%)|medium_hydraulic_risk_area_p2 (%)|low_hydraulic_risk_area_p1 (%)|
|very_high_landslide_risk_area_p4 (%) | high_landslide_risk_area_p3 (%)|medium_landslide_risk_area_p2 (%)|low_landslide_risk_area_p1 (%)|
|attention_area (%)|resident_population (n)|high_hydraulic_risk_population_p3 (%)|
medium_hydraulic_risk_population_p2 (%)|
|low_hydraulic_risk_population_p1 (%)|very_high_landslide_risk_population_p4 (%)|high_landslide_risk_population_p3 (%)|medium_landslide_risk_population_p2 (%)|low_landslide_risk_population_p1 (%)|
|attention_population (%)|resident_family (n)|high_hydraulic_risk_family_p3 (%)|medium_hydraulic_risk_family_p2 (%)|
|low_hydraulic_risk_family_p1 (%)|very_high_landslide_risk_family_p4 (%)|high_landslide_risk_family_p3 (%)|medium_landslide_risk_family_p2 (%)|
|low_landslide_risk_family_p1 (%)|attention_family (%)|building (n)|high_hydraulic_risk_building_p3 (%)|medium_hydraulic_risk_building_p2 (%)|
|low_hydraulic_risk_building_p1 (%)|very_high_landslide_risk_building_p4 (%)|high_landslide_risk_building_p3 (%)|medium_landslide_risk_building_p2 (%)|
|low_landslide_risk_building_p1 (%)|attention_building (%)|enterprise (n)|high_hydraulic_risk_enterprise_p3 (%)|medium_hydraulic_risk_enterprise_p2 (%)|
|low_hydraulic_risk_enterprise_p1 (%)|very_high_landslide_risk_enterprise_p4 (%)|high_landslide_risk_enterprise_p3 (%)|medium_landslide_risk_enterprise_p2 (%)|
|low_landslide_risk_enterprise_p1 (%)|attention_enterprise (%)|cultural_heritage (n)|high_hydraulic_risk_cultural_heritage_p3 (%)|
|medium_hydraulic_risk_cultural_heritage_p2 (%)|low_hydraulic_risk_cultural_heritage_p1 (%)|very_high_landslide_risk_cultural_heritage_p4 (%)|high_landslide_risk_cultural_heritage_p3 (%)|
|medium_landslide_risk_cultural_heritage_p2 (%)|low_landslide_risk_cultural_heritage_p1 (%)|attention_cultural_heritage (%)||

| MD4 Columns |  |  |  |
| - | -  | - | - |
|prov_name|prov_code|area (kmq)|high_hydraulic_risk_area_p3 (%)|medium_hydraulic_risk_area_p2 (%)|
|low_hydraulic_risk_area_p1 (%)|very_high_landslide_risk_area_p4 (%)|high_landslide_risk_area_p3 (%)|medium_landslide_risk_area_p2 (%)|
|low_landslide_risk_area_p1 (%)|attention_area (%)|resident_population (n)|high_hydraulic_risk_population_p3 (%)|medium_hydraulic_risk_population_p2 (%)|
|low_hydraulic_risk_population_p1 (%)|very_high_landslide_risk_population_p4 (%)|high_landslide_risk_population_p3 (%)|
|medium_landslide_risk_population_p2 (%)|low_landslide_risk_population_p1 (%)|attention_population (%)|resident_family (n)|
|high_hydraulic_risk_family_p3 (%)|medium_hydraulic_risk_family_p2 (%)|low_hydraulic_risk_family_p1 (%)|very_high_landslide_risk_family_p4 (%)|
|high_landslide_risk_family_p3 (%)|medium_landslide_risk_family_p2 (%)|low_landslide_risk_family_p1 (%)|attention_family (%)|building (n)|
|high_hydraulic_risk_building_p3 (%)|medium_hydraulic_risk_building_p2 (%)|low_hydraulic_risk_building_p1 (%)|very_high_landslide_risk_building_p4 (%)|
|high_landslide_risk_building_p3 (%)|medium_landslide_risk_building_p2 (%)|low_landslide_risk_building_p1 (%)|attention_building (%)|
|enterprise (n)|high_hydraulic_risk_enterprise_p3 (%)|medium_hydraulic_risk_enterprise_p2 (%)|low_hydraulic_risk_enterprise_p1 (%)|
|very_high_landslide_risk_enterprise_p4 (%)|high_landslide_risk_enterprise_p3 (%)|medium_landslide_risk_enterprise_p2 (%)|low_landslide_risk_enterprise_p1 (%)|
|attention_enterprise (%)|cultural_heritage (n)|high_hydraulic_risk_cultural_heritage_p3 (%)|medium_hydraulic_risk_cultural_heritage_p2 (%)|
|low_hydraulic_risk_cultural_heritage_p1 (%)|very_high_landslide_risk_cultural_heritage_p4 (%)|high_landslide_risk_cultural_heritage_p3 (%)|medium_landslide_risk_cultural_heritage_p2 (%)|
|low_landslide_risk_cultural_heritage_p1 (%)|attention_cultural_heritage (%)|||


A summary table of the produced mashup dataset:

| ID | Theme | Formats | Licence | IRI |
|  :---     |     :---      |     :---     |     :---     |    :---     |
| MD1         |     Actions     |     CSV/JSON     |     CC-BY SA 4.0     |    :---     |
| MD2         |     Disruptions     |     CSV/JSON     |     CC-BY SA 4.0     |     :---     |
| MD3         |     hydrogeological risk in municipalities     |     CSV/JSON     |     CC-BY SA 4.0     |    :---     |
| MD4         |     hydrogeological risk in provinces     |     CSV/JSON     |     CC-BY SA 4.0     |     :---     |

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

**Reusable**

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

**RDFs **

ttl files validated with http://ttl.summerofcode.be/
graphs created using https://www.ldf.fi/service/rdf-grapher


## Final remarks

## Footnotes

[^1] cfr. Unesco's definition of Water-Disasters at https://en.unesco.org/themes/water-security/hydrology/water-related-disasters