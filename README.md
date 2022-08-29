# 🌊 FlooData

FlooData is a project developed by Chiara Catizone and Giulia Venditti for the final exam of the course *Open Access and Digital Ethics* held by professor Monica Palmirani at the Master Course of Digital Humanities and Digital Knowledge (Univesity of Bologna) during the A.Y. 2021/2022.


## 🎙 Introduction 

Emilia Romagna is the sixth largest region in Italy in terms of surface area, having a variegated hydrogeological conformation. The resulting heterogeneity of ecosystems is currently undergoing drastic transformations, due to climate change, as stated by the Emilia Romagna's Regional Environmental Protection Agency, [ARPAE](https://www.arpae.it/it), in its report on [climate change in Emilia-Romagna](https://agricoltura.regione.emilia-romagna.it/produzioni-agroalimentari/temi/bio-agro-climambiente/cambiamento-climatico-in-emilia-romagna). Also on the national level, the Italian Institute for Environmental Protection and Research, [ISPRA](https://www.isprambiente.gov.it/it), stated that the Italian hydrogeological morphology is extremely fragile, due to intense weather events and proneness to landslides of the territory.

Our project's objectives are to return an overview of the relationship between hydrogeological disruptions and the measures – undertaken by local communities – to deal with them, and to inform end-users on the hydrogeological risk in Emilia Romagna's Provinces. Here, we introduce information on different human activities related to our topic, distinguishing between **preventive measures** and **reparatory interventions**, and making explicit the involvement of local communities in preserving their territory. Also, we present the characterization of each province in terms of lndslide and hydraulic risk.



## 🏞 Scenario

**ISPRA** is the owner institution of some of the Open datasets we relied on while gathering source data or building FlooData's Catalogue. 
[LinkedIspra](http://dati.isprambiente.it/) is their pilot project on Linked Open Data following W3S guidelines. It is a Catalog (issued in 2016) composed of 5 datasets:  
* [ReNDiS](http://dati.isprambiente.it/dataset/il-rendis/), the National Directory of Soil Defense Interventions
* [CDS](http://dati.isprambiente.it/dataset/cds/), the Land Consumption in Italy
* [RMN](http://dati.isprambiente.it/dataset/rmn-la-rete-mareografica-nazionale/), the  National Mareographic Network
* [RON](http://dati.isprambiente.it/dataset/ron-rete-ondametrica-nazionale/), the 
National Wave Network
* [Luoghi](http://dati.isprambiente.it/dataset/i-luoghi/), 
the data of the regions from the cartographic systems of ISPRA
</br>

The second ISPRA project we used for creating FlooData is **[IdroGEO](https://idrogeo.isprambiente.it/app/)**, a platform allowing consultation, download and sharing of data, maps, reports, and documents of the Italian Landslide Inventory - [IFFI](https://www.progettoiffi.isprambiente.it/en/). The platform has an [Open Data section](https://idrogeo.isprambiente.it/app/page/open-data), where one can download data concerning landslides, available in Open format and with [Creative Commons](https://creativecommons.org/) licences. 
</br>

Another platform we used is **[MinERva](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset)**.
MinERva is the point of reference and information sharing held by the Directorate General for Territory and Environment Care of the *[Region of Emilia Romagna](https://www.regione.emilia-romagna.it/)*. It contains various databases classified following the Comprehensive Knowledge Archive Network [(CKAN)](https://ckan.org/) grouping and the UN 2030 Agenda in [Sustainable Development Goals](https://www.un.org/en/sustainable-development-goals). MinERva is an open-source and web-based system, for data gathering, cataloguing and dissemination.
</br>

**[OpenCoesione](https://opencoesione.gov.it/it/)** – the [Italian government](https://www.governo.it/)'s open gov initiative on cohesion policies in Italy – makes their datasets available, offering a partial return of the monitoring system managed by the [State General Accounting](http://www.rgs.mef.gov.it/); in a form suitable to respond to the cognitive interests of citizens. In the [Open Data section](https://opencoesione.gov.it/it/opendata/#!progetti_section), the datasets on projects are available for download and re-use.

The final data source employed in the construction of FlooData datasets is a **[GitHub repository](https://github.com/MatteoHenryChinaski/Comuni-Italiani-2018-Sql-Json-excel)** by [Matteo Henry Chinaski](https://github.com/MatteoHenryChinaski). The author does not provide a licence or waiver for the data they created. However, it is possible to collaborate and freely download the dataset without specifying any legal restrictions. The data contained in this resource is of topological and topographical nature: place names, coordinates, ISTAT codes, dimensions and statistics (out of date) of different Italian areas, spanning from single municipalities to the entire national territory. 


## 📂 Original and mashed-up datasets

### Original datasets descriptions

**[ReNDiS](http://dati.isprambiente.it/dataset/il-rendis/)** contains information on interventions, associated lots, georeferencing, projects' financial budgets, disruptions' typologies, lithologies and realized works, classification of hydrogeological disruptions and of works for protecting the soil. Geographical data has labels linked to the second dataset.

**[Luoghi](http://dati.isprambiente.it/dataset/i-luoghi/)** was used as support to gather geographical data about *interventions*, *repair* and *instabilities*. It contains places' official names; latitude and longitude of the centroids; polygons (shape); administrative hierarchy; Istat codes, and links to Linked Data Cloud (ISTAT datiopen, Geonames,  DBpedia, etc.)

**[Segnalazioni fenomeni geologici particolari](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-13t115808)**, groups reports on particular hydrogeological phenomena made by citizens to the Regional Geological Service since may 2012, in localities hit by that year's earthquake disaster.

**[Opere di difesa costiera - 2020](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2022-01-04t151636)** contains information on the coastal protections present both at sea and in the hinterland of the Emilia-Romagna coast. 

**[Dinamica Meteomarina ed Impatti - Località colpite (numero eventi con impatto) mareggiate 1946-2020](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2021-03-12t110331contains)** contains the name of the moslty eroded areas by calmities that have striken in the time-span 1946-2020. Istat codes of municipalities are present in the dataset.

**[Province](https://idrogeo.isprambiente.it/app/page/open-data)** contains landslide and flood risk indicators relating to territory, population, families, buildings, industry and service, and cultural heritage. Istat codes of Regions and Provinces are present in the dataset.

**[Progetti esteso EMR 2007-2013](https://opencoesione.gov.it/it/opendata/#!progetti_section)** and **[Progetti esteso EMR 2014-2020](https://opencoesione.gov.it/it/opendata/#!progetti_section)** contain track records of cohesion projects in Emilia Romagna, transversally describing their management.they have ISTAT codes and denominations for Region, prvinces and Municipalities. It contains ISTAT codes for each municipality.

**[Italy geo](https://github.com/MatteoHenryChinaski/Comuni-Italiani-2018-Sql-Json-excel/blob/master/italy_geo.json)** is a dataset we used to link municipalities and provinces coming from previous datasets to their latitude and longitude coordinates.


The below table is a resume of datasets selected for our project, and that has been mashed up to create FlooData final datasets.


| ID | Dataset | Source | Time span | Licence |
| :--- | :--- | :--- | :--- | :--- |   
| **D1** | [ReNDIs](http://dati.isprambiente.it/dataset/il-rendis/) | [LinkedIspra](http://dati.isprambiente.it/) | 2016 - 2021 | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.it) |
| **D2** | [Luoghi](http://dati.isprambiente.it/dataset/i-luoghi/) | [LinkedIspra](http://dati.isprambiente.it/) | 2016 | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.it) |
| **D3** | [Segnalazioni fenomeni geologici particolari](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-13t115808) | [MinERva](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset) | 2012 - 2022 | [CC BY 3.0 IT](https://creativecommons.org/licenses/by/3.0/legalcode.it)|
| **D4** | [Opere di difesa costiera - 2020](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2022-01-04t151636) | [MinERva](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset) | 2020 - 2021 | [CC BY 3.0 IT](https://creativecommons.org/licenses/by/3.0/legalcode.it)|
| **D5** | [Dinamica Meteomarina ed Impatti - Località colpite (numero eventi con impatto) mareggiate 1946-2020](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2021-03-12t110331)| [MinERva](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset) | 1946 - 2020 | [CC BY 3.0 IT](https://creativecommons.org/licenses/by/3.0/legalcode.it)|
| **D6** | [Province](https://idrogeo.isprambiente.it/app/page/open-data) |  [IdroGEO](https://idrogeo.isprambiente.it/app/) | 2017 | [CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.it)|
| **D7** | [Progetti esteso EMR 2007-2013](https://opencoesione.gov.it/it/opendata/#!progetti_section) | [OpenCoesione](https://opencoesione.gov.it/it/) | 2007-2013 | [CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.it)|
| **D8** | [Progetti esteso EMR 2014-2020](https://opencoesione.gov.it/it/opendata/#!progetti_section) | [OpenCoesione](https://opencoesione.gov.it/it/) | 2007-2013 | [CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.it)|
| **D9** | [Italy geo](https://github.com/MatteoHenryChinaski/Comuni-Italiani-2018-Sql-Json-excel/blob/master/italy_geo.json) | [Comuni-Italiani-2018 GitHub](https://github.com/MatteoHenryChinaski/Comuni-Italiani-2018-Sql-Json-excel) | 2014-2018 | Not specified |


</br>

### Mashed-up datasets descriptions

**[Activities](datasets/final_dataset/actions.csv)** is the first mashed-up dataset. It covers Emilia Romagna's data on reparatory and preventive interventions against hydrogeological disasters. THe data for each activity is about its location, description, type, data and geo-data.

**[Disruptions](datasets/final_dataset/disruptions.csv)** is the second mashed-up dataset containing data about hydrogeological disasters involving Emilia Romagna sucha s the type, the municipality in which it is located.

**[Hydrogeological risk](datasets/final_dataset/province.csv)** is the third mashed-up dataset containing data on flooding risk, area and geographical information of Emilia Romagna's provinces.

All mashed-up datasets use geographical data such as latitude, longitude and national standard province abbreviations.

The below table is a resume of datasets created by FlooData, containing information on hydrogeological disasters, interventions and geographical data useful for their visualization on maps and other graphs.

| ID | Dataset | Original dataset | Time span | 
| :---         |     :---     |     :---     |     :---     |  
| **MD1** | [Activities](datasets/final_dataset/actions.csv) | **D1**,**D2**,**D4**,**D7**,**D8**,**D9** | 2004 - 2021 |
| **MD2** | [Disruptions](datasets/final_dataset/disruptions.csv) | **D1**,**D2**,**D3**,**D5**,**D9**| None| 
| **MD3** | [Hydrogeological risk](datasets/final_dataset/province.csv) | **D6**,**D9** | None |


## 💎 Quality analysis of the datasets
The below criteria must be met, to manage the level of information quality as set out by the National Guidelines for the Improvement of Public Information Assets in the [Context of Data Quality](https://docs.italia.it/italia/daf/lg-patrimonio-pubblico/it/bozza/aspettiorg.html#qualita-dei-dati):

* *Accuracy*: the data's properties accurately reflect the true worth of the concept or referenced event ;
* *Completeness*: the data is comprehensive concerning all of its expected values and the relevant entities (sources) that contribute to the definition of the procedure;
* *Coherence*: in terms of how the administration's owner uses the data, neither the data nor its attributes can relate to other data;
* *Promptness*: the data, and its attributes, are updated to the procedure to which it refers.

| Dataset | Accurancy | Completness | Coherence | Promptness |
| :---         |     :---     |     :---     |     :---     |     :---   |
| **D1 and D2\***       |   Satisfied, it creates meaningful links between different kind of records (e.g., geological instabilities are linked to and their respective repairs link to the same contract, and when ossible are represented as a group      |     Not satisfied: 93.9%    |     Not satisfied: Arbitrary use of uppercase and lowercase and uncomprehensible characters in some labels    |  <li>D1: Satisfied: the dataset is updated daily, ours is updated untill 6/7/2022<<li>D2: Not satisfied: last update on 22/03/2016|
| **D3**         |     Satisfied     |     Not satisfied: 81.9%%    |     Satisfied    |       Not satisfied: Last update was on 31/12/2020 |
| **D4**         |     Not satisfied: There is no clear meaning of some column names   |      Not satisfied: 80.4%     |     Not satisfied: There is no standard of defining "null" values, empty fields remain empty or are filled by "nessuno"     |         Not satisfied: Last update was on 01/01/2021 |
| **D5**         |     Satisfied     |     Satisfied   |     Not satisfied: Arbitrary representation of thousands (AAAAMMDD - e.g. 20090205)     |         Not satisfied: Last update was on 01/01/2020 |
| **D6** | Satisfied | Not satisfied: 99.7% | Satisfied |      Satisfied: last update 2021 with new ISTAT codes  |
| **D7**         |     Satisfied        |      Not satisfied: 75.8%       |      Satisfied         |         Satisfied: last update may 2022      |
| **D8**         |     Satisfied        |      Not satisfied: 71.1%        |      Satisfied         |         Satisfied: last update may 2022     |
| **D9**         |     Satisfied        |      Satisfied       |      Satisfied          | Not Satisfied: last update 2018 |

<sup><sub>\* Datasets were merged and sampled down as ReNDiS geographical data relies on Luoghi's. The data frames we used for mash-up were also used as analysis samples of the over one million original entries. </sub></sup>

Below we present the quantitative data retrieved during our Quality analysis, fully available at [quality.ipynb](software/quality.ipynb):


| Dataset | Total values | Null values | Completness |
| :---         |     :---     |     :---     |    :---     |  
| **D1 a D2\***      |     395728     |     35307     |    93.9     |  
| **D3**         |     763     |     138     |    81.9%     |  
| **D4**         |     38164     |     7232     |     80.4%     | 
| **D5**         |     380     |     0     |    100%     |  no
| **D6**         |     13161     |     34     |    99.7%     |  
| **D7**         |     3449466    |     835602     |    75.8%     |  
| **D8**         |     6131986     |     1773353     |    71.1%     |  
| **D9**         |     31920     |     3     |    99.9%     |  


<sup><sub>\* Datasets were merged and sampled down as ReNDiS geographical data relies on Luoghi's. The data frames we used for mash-up were also used as analysis samples of the over one million original entries. Values here represent the sum and mean of the merged datasets.</sub></sup> 

## ⚖️ Legal analysis 
Legal analysis is required to ensure the long-term viability of the data generation and dissemination process, produce a balanced service in accordance with the public function and individual rights. As a result, the legal analysis of the sources seeks to assess these precarious balances, emphasising use restrictions, objectives of competence, rights determination, and licence conditions.

We evaluated all legal facets of the dataset lifetime using a reference checklist. The check list consists of a series of questions that answered with a Yes, No, or Not Verifiable for each aspect.

**Privacy** | Issues | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 |
| ----------- | --------| ------|--------|-------|---------|---------|---------| ---------|---------------| ---------|
| | Are the data free from any personal information that can directly identify the individual?  If not, is this information authorized by law?| No, yes |Yes | Yes | Yes | Yes | Yes  | Yes | Yes  | Yes  |
| | Are the data free from any sensitive information that can be traced back to the individual? If not, is this information authorized by law? | No, yes |Yes | Yes | Yes | Yes | Yes  | Yes | Yes  | Yes  |
| | Are the data free from any information relating to the subject that, when crossed with data commonly found on the web, can identify the individual? If not, is this information authorized by law? | No, yes | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  | Yes  |
| | Are the data free from any record relating to refugees, protected by justice, victims of violence or in any case protected categories? | Yes | Yes | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  |
| | Did you use a tool to calculate the risk of de-anonymization of your dataset before publishing it? | / | / | / | / | / | / | / | / | / | 
| | Do you display any search services that can filter the data in order to obtain a single geolocated record? | No | No | No | No | No | No  | No  | No  | No  | 
| **Intellectual Property Rights of the Source** | | |
| | Did you create the data? | No | No  | No | No | No | No  | No  | No  | No  | 
| | Are you the owner of the data even if you did not create it yourself? | No | No  | No | No | No | No  | No  | No  | No  | 
| | Are you sure you are not using data for which there is a third party license or patent? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  |
| | If the data is not yours, do you have an agreement or license authorizing you to publish it? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | No* |
| **Release license** | | |
| | Do you release the data you own with a license? | Yes | Yes  | Yes | Yes | Yes | Yes | Yes  | Yes  | Yes  | 
| | Have you also included the safeguard clause “In any case, the data cannot be used to re-identify data subjects”? | No | No  | No | No | No | No  | No  | No  | No  | 
| **Limitations on public access** | | |
| | Have you checked that there are no legal or contractual impediments preventing the publication of the data? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  | 
| | Have you checked if there are no security reasons of public order or nationality that prevent you from publishing the data? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes |
| | Have you checked if there are no reasons related to professional secrecy that prevent the publication of the data? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  | 
| | Have you checked if there are no reasons related to the state secret that prevent the publication of the data? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  | 
| **Economical Conditions** | | |
| | Have you verified that you can release the data for free without breaking any public finance rules? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  | 
| | If you have imposed economic conditions for using the data, are you sure you have imposed a price to cover only the marginal costs? | / | / | / | / | / | / | / | / | / |
| **Temporary aspects** | | |
| | Do you have a temporary policy for updating the dataset? | No | No  | No | No | No | No  | No  | No  | No  | 
| | Do you have some mechanism for informing the end-user that the dataset is updated at a given time to avoid mis-usage and so potential risk of damage? | Yes | Yes  | Yes | Yes | Yes | Yes  | Yes  | Yes  | Yes  | 
| | Are the data updated frequently in order to heal any information that is harmful to people or organizations? | Yes| No | Yes | No | No |  No  | No | No |
| | Does the data have legal or jurisprudential prohibitions that prevent it from being indexed by search engines? | No | No  | No | No | No | No  | No  | No  | No  | 

### Licences mashed-up datasets

Final licences for the mashed-up datasets have been chosen according to licence compatibility.

In the following table, we listed all original datasets licences and found them to be all commercial, 3 of them national, all the remaining ones international, as a result of this analysis we decided to give all mashed-up datasets a CC-BY-SA 4.0 licence to allow their mash-up and make them re-usable at international level.

| ID      | Dataset | Originals' licences | Final licence |
| :---    | :---    | :---                |     :---     |  
| **MD1** | [Activities](datasets/final_dataset/actions.csv) |  CC-BY 4.0, CC-BY 4.0, CC-BY 3.0, CC-BY-SA 4.0, CC-BY-SA 4.0, Not specified| [CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.it) |
| **MD2** | [Disruptions](datasets/final_dataset/disruptions.csv) | CC-BY 4.0, CC-BY 4.0, CC-BY 3.0, CC-BY 3.0, Not specified| [CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.it) |
| **MD3** | [Hydrogeological risk](datasets/final_dataset/province.csv) | CC-BY-SA 4.0,  Not specified | [CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.it) |


## 🫂 Ethical analysis 

From an *ethical* point of view, we considered the importance of the human being interest, individiual data control and transparency, accountability, and equality, folowwing [DataEthics' principles](https://dataethics.eu/data-ethics-principles/)
Along with these ethical aspects, we also considered other criteria such as sustainable re-use of the data gathered, and presence of information of public interest when choosing **FlooData**'s source data, as we wanted to account for the management of financings (Open Coesione), the present risk of hydrogeological disasters in the whole area of Emilia-Romagna, the number of preventive interventions and following reparations. 

The data gathered is transparently managed by producers, as documentation on project and/or datasets, licences, and policies are made available to final users, avoiding cognitive biases and legal misunderstanding in terms of data re-use.


The original datasets mainly represent environmental– and geodata. This kind of data naturally avoids discrimination, stereotyping, crystallization, distortion of the history, misrepresentation of reality, and manipulation of the cultural identity of a country/community.
On average, the data gives information about the region as a whole and do not pose an individual's privacy risk.


Data relating to communities of people living in the endangered area comes from the two sets coming from ISPRAS's project ***IdroGeo***. 
*D6* contains information on families living in areas with high, medium and low flooding and hydraulic risks. Even though this information is linked to natural persons, it is made available for public interest purposes, anonymized, and in form of statistical data, in compliance with the Art. 89 of GDPR. Additionally, this kind of data – when made public – might be a call to action to sensibilize people on climate change and hydrogeological issues.
Finally, we noticed that **ReNDis** makes accessible the names of whom are responsible for recorded interventions. We consider the presence of identity data in this set legitimate since names of public officers are by nature in the public domain. 

For ethical requirements, we also rely on [Accenture](https://www.accenture.com/us-en)'s Data Ethics Decision Making Guidelines. Thus, data gathered and presented on Floodata has been downloaded directly from sources' websites or other institutional aggregators such as **MinERva** and **OpenCoesione**. 
The datasets used have all been made available for re-use by producers. The re-use of this data on FlooData is consistent with the creators' specific intent of displaying the hydrogeological situation of the studied area.

Finally, we take into account that there are chances of people acting on the collected information to look for a more secure and maintained area within the region Emila Romagna, but that does not look like an ethical issue as much as a normal inferential process granted to citizens.



## ⚙️ Technical analysis 

### Original datasets

#### [LinkedIspra](http://dati.isprambiente.it/) 
Data – *D1* and *D2* - are accessible through a Virtuoso SPARQL endpoint, and data dumps made of RDF triples of the data were available for download. We downloaded the N-Triples dumps as the SQL EndPoint didn't ensure back-end stability and reliability during our research period. 
*Format* of downloaded data is .nt
*Provenance*: [ISPRA](http://dati.isprambiente.it/id/organization/ispra/html)

| Metadata | **[D1](http://dati.isprambiente.it/id/dissesto/html)** | **[D2](http://dati.isprambiente.it/id/place/html)** |
| :---  | :--- | :--- | 
| URI | [dissesto](http://dati.isprambiente.it/id/dissesto/html) | [place](http://dati.isprambiente.it/id/place/html) | 
| Description |  ✅ |  ✅ | 
| Modification date |  ✅ |  ✅ | 
| Label |  ✅ |  ✅ | 
| Keywords |  ✅ |  ✅ | 
| Title |  ✅ |  ✅ | 
| Identifier |  ✅ |  ✅ | 
| Type |  ✅ |  ✅ | 
| Publisher | ✅ |  ✅ | 
| Distribution | ✅ |  ✅ | 
| Landing Page | ✅ |  🚫 |
| Theme | ✅ |  ✅ | 
| Creator |  ✅ |  ✅ | 
| Accrual Periodicity | ✅ |  ✅ | 
| Language | ✅ |  ✅ | 
| Rights Holder | ✅ |  ✅ | 


#### [Minerva](https://datacatalog.regione.emilia-romagna.it/catalogCTA/)
Datasets – *D3* *D4* and *D5* - are accessible through a Moka viewer service available for download as OpenData. 
Along with datasets' metadata, MinERva provides information about the responsible body, reference structure, referent, author
 and dates about catalogue cards and physical data.
*Format* of downloaded data is .zip from which we extracted a .dbf file
*Provenance*: [ISPRA](http://dati.isprambiente.it/id/organization/ispra/html)


| Metadata | **[D3](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2017-06-13t115808)** | **[D4](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2022-01-04t151636)** | **[D5](https://datacatalog.regione.emilia-romagna.it/catalogCTA/dataset/r_emiro_2021-03-12t110331)** | 
| :---  | :--- | :--- | :--- |
| URI | [Segnalazioni_fenomeni_geologici](https://mappegis.regione.emilia-romagna.it/moka/ckan/conoscenza_sottosuolo/Segnalazioni_fenomeni_geologici.zip) | [Opere_Difesa_2020](https://mappegis.regione.emilia-romagna.it/moka/ckan/costa/Opere_Difesa_2020.zip) | [Localita_colpite_Erosione_1946_2020](https://mappegis.regione.emilia-romagna.it/moka/ckan/costa/Localita_colpite_Erosione_1946_2020.zip) |
| Dataset ID | ✅ |  ✅ |  ✅ | 
| Other ID | 🚫 |  🚫 | 🚫 |
| Themes | ✅ |  🚫 | ✅ | 
| Sub-themes | 🚫 |  🚫 | 🚫 |
| Geographic coverage | ✅ |  ✅ |  ✅ | 
| Geonames URI | 🚫 |  🚫 | 🚫 |
| Language | ✅ |  ✅ |  ✅ | 
| Accural Frequency | ✅ |  ✅ | ✅ | 
| Version | 🚫 |  🚫 | 🚫 |
| Creator | 🚫 |  🚫 | 🚫 |
| Scale  | ✅ |  ✅ |  ✅ | 
| Conformity | 🚫 |  ✅ | 🚫 |
| GEMET Category | ✅ |  ✅ |  ✅ | 
| Environmental thematic | ✅ |  ✅ |  ✅ | 
| Spatial | ✅ |  ✅ |  ✅ | 


#### [IdroGEO](https://idrogeo.isprambiente.it/app/) 
*D6* data is available for download in different formats: XLS, CSV and JSON. The platform also allows downloading the .csv file containing descriptions and the source of the columns in the datasets. <br>
*Format* of downloaded data is .csv<br>
*Provenance*: https://idrogeo.isprambiente.it/app/page/open-data

IRI is not specified and Basic metadata is provided for *D6* such as:
- Title 
- Description with Version and Year
- Licence 
- Format
- Table columns' Metadata



#### [OpenCoesione](https://opencoesione.gov.it/it/)
 *D7* and *D8* representing a part of the projects OpenCOesione is keep ing track of. Everyone can download them in .csv and .xls format.<br>
*Format* of downloaded data is .csv<br>
*Provenance*: https://opencoesione.gov.it/it/


IRI is not specified and Basic metadata is provided for *D7* and *D8*  such as:
- Title 
- Description
- Licence 
- Format


#### [Italy geo](https://github.com/MatteoHenryChinaski/Comuni-Italiani-2018-Sql-Json-excel/blob/master/italy_geo.json) 
Datasets *D9* can be freely downloaded from GitHub using -curl request or download the file. No specific metadata is supplied, with exceptions made for content labels. <br>
*Format* of downloaded data is .json <br>
*Provenance*: https://github.com/MatteoHenryChinaski/Comuni-Italiani-2018-Sql-Json-excel/blob/master/italy_geo.json

[Resume table of source datasets' technical analysis](technical_table.md)

### Mashup and output datasets

All data processing tasks undertaken for creating the mashed-up datasets were carried out using Python versions 3.9 and 3.10 and built-in/open-source methods.

For creating the new datasets we disposed of four different kinds of file formats:

* NT
* DBF
* CSV
* JSON

#### Pre-processing



**N-Triples** files needed to be pre-processed and parsed into data frames. 
To accomplish this, we developed a script [rdf_parse.py](software/rdf_parser.py) to merge the ReNDi and Luoghi data and create three data frames containing data on hydrogeological disruptions, reparations and their financing. 
The script uses the rdflib to parse the .nt files, and through class "typology", it gathers the main subjects we want to retrieve: instabilities, interventions(financings), and repairs.
Then for each subject, we extracted the predicates co-occurring with it and used them as labels for creating the data frame's columns. 

For each column to be created we iterated triples formed as <*Subject*><*Column label*><*object*> and select the corresponding object as that cell value.
For inserting geographical data, we started from ReNDiS lots locations and queried the Luoghi dataset looking for their labels, province, latitude and longitude. 

The resulting data frames were temporarily saved in .csv format for later merging with other datasets. 

**DBF** files have been converted automatically into CSV files using the software [dbfconv.py](software/dbfconv.py) developed for this purpose. The software converts the files keeping their original names using the dbf_read library's DBF method to open this kind of file saved in .csv format.
#### Merging 

The second step consists of the merging of the JSON and CSV files.

The original data has been mashed-up to create three datasets in FlooDatas's catalogue.

Using our software actions.py and territory .py, we created respectively **MD1**and **MD3**. 

* **actions.py** selects all Emilia-Romagna's projects (subsetting the original dataset when necessary, e.g., DF1), and constructs the columns based on the information we selected from source data frames. 
Resulting df is then saved into .json and .csv format for future visualization and consultation purposes. 

* **territory.py** is fed with *DF6*. Here we select interesting classes from IdroGeo's datasets such as percentages of risk and attention percentages of families, enterprises and cultural heritage. 
To create MD3 we crossed place names contained in D6 with data in *D10* to find municipalities' latitude and longitude coordinates.


Finally, we have  produced **MD2** by selecting and giving standard names to columns representing the data necessary for our project.
The production workflow is visible in notebook [disruptions.ipynb](software/Disruptions.ipynb)

#### Revision
Final modifications have been made to each dataset to translate the data from Italian to English, and remove null values or unnecessary data. This last process can be found in [datasets_update.ipynb](software/datasets_update.ipynb)

A summary table of the produced mashup dataset:

|   ID      |   Theme   |   Distribution Formats     |   Licence    |   IRI     |
|   :---    |   :---    |   :---        |   :---    |   :---    |
|   MD1     |   Actions |   CSV/JSON    |   CC-BY SA 4.0    |    https://github.com/ChiaraCati/Owater/resource/dataset/MD1     |
|   MD2     |   Disruptions | CSV/JSON  |   CC-BY SA 4.0    |    https://github.com/ChiaraCati/Owater/resource/dataset/MD2     |
|   MD3     |   Hydrogeological risk in provinces  |  CSV/JSON  |   CC-BY SA 4.0  |   https://github.com/ChiaraCati/Owater/resource/dataset/MD3 |


#### FAIR principles


In doing so, we adhered to the FAIR principles outlined in the [FAIR Data Management Guidelines in Horizon 2020](https://ec.europa.eu/research/participants/data/ref/h2020/grants_manual/hi/oa_pilot/h2020-hi-oa-data-mgt_en.pdf). To put it another way, we worked to make our research data accessible, searchable, interoperable, and reusable (FAIR). Those principles include three types of entities: data, metadata and infrastructure. Given the analysis, we can state that our research data is compliant with the FAIR principles.

**Findable:**

* (Meta)data are assigned a unique identifier: both the data we retrieved from the source datasets, the mashed-up data, and the metadata we developed following the [DCAT AP version 2.0.0 guidelines](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/200) are compatible with this point, providing URIs.
* Data are described with rich metadata: we linked a substantial amount of DCAT-AP specification-compliant metadata to our data, including not only all required classes and their corresponding necessary characteristics but also certain suggested and optional features that were helpful for our data.
* Metadata clearly and explicitly include the identifier of the data they describe: we used the DCAT-AP optional attribute for datasets dct:identifier to attach a unique identifier of the data described with the metadata for each dataset that is a part of a catalogue as well as for our dataset.

**Accessible:**

* (Meta)data are retrievable by their identifier using a standardised communications protocol: all the data we collected and mashed up and the relative metadata are retrievable through the HTTP or its extension HTTPS.
* The protocol is open, free, and universally implementable: HTTP and HTTPS are compliant with these characteristics.
* Metadata is accessible, even when the data are no longer available: metadata will remain accessible from the metadata web page of this web resource.

**Interoperable:**

* (Meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation: the mashed-up data was represented using JSON, CSV, and XML, and the metadata was described and organised using RDF using the Turtle syntax.
* (Meta)data use vocabularies that follow FAIR principles: 

**Reusable**

* Meta(data) is richly described with a plurality of accurate and relevant attributes: data and metadata are represented by a wide and varied set of labels, such as the date of data collection and change, the licence, the publisher, the originator, and their content.

* (Meta)data are released with a clear and accessible data usage license: The FlooData datasets are made available under the terms of the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode.it) Licence, which are specific to the dataset and associated metadata we provided.

* (Meta)data are associated with detailed provenance: in the metadata encoding of our project, data provenance information is provided in a machine-readable way.

* (Meta)data meet domain-relevant community standards.

## 🌱 Sustainability
The datasets used to create Floodata, which examines the dangers by flooding catastrophes and related interventions in the Emilia Romagna area, come from multiple sources. The souce data used for this project is currently being maintained by the originating institutions or organisations. This website re-uses this data, and was developed as the final project for the [Open Access and Digital Ethics](https://www.unibo.it/it/didattica/insegnamenti/insegnamento/2020/424645) course of the Master's Degree Course in [Digital Humanities and Digital Knowledge](https://corsi.unibo.it/2cycle/DigitalHumanitiesKnowledge) (a.y. 2021/22) at the [University of Bologna](https://www.unibo.it/it). The datasets produced for this project are not actively maintained.


## 🎢 Visualizations
We started this phase of the project writing down a list of questions to describe hydrogeological disasters in Emilia Romagna, keeping in mind eventual linitations of the data we have collected. Then, we have analysed our mashed-up data to answer these questions, and used [Highcharts JS](https://www.highcharts.com/) to plot them in graphs and allow users to make full use of the data in our [website](https://chiaracati.github.io/Owater/).

### Questions

1. What kinds of hydrogeological disasters do we find in Emilia Romagna, and what is their distribution on this territory? 
    - Map of Emilia Romagna, divided into provinces, with bubbles pointing to disruptions' locations (latitude, longitude and municipality), also their type and amount per type information has been specified in tooltips.<br>
    [Code example](https://www.highcharts.com/blog/chartchooser/map-comparison-continuous/ )
    - Sunburst of the total amount of disasters divided by province and then divided by typology<br>
    [Code example](https://www.highcharts.com/blog/chartchooser/sunburst-categorical-composition/)

2. How potentially harmful are these disasters? Which areas are most affected?
    - Choropleth map showing the geographical distribution of risk areas, concerning hydraulic risk, landslide risk, and focusing probability of risk for the families, population, enterprises, buildings and cultural heritage.<br>
    [Code example](https://www.highcharts.com/blog/tutorials/effectively-visualizing-us-election-results/)

3. How does the local community react to the water disaster, what is the yearly rate of financings devolved to hydrogeological disruption? Are there more preventive or reparatory initiatives? What kind of interventions have been performed, and what is the amount of financings for each Province?
    - Choropleth map showing the distribution of financings over the 9 provinces, with complementary line charts showing the trend of investments made by each Province <br>
    [Code example](https://www.highcharts.com/demo/maps/rich-info )
    -  Bar chart of the total amount of financings for preventive and reparatory interventions divided by Province<br>
    [Code example]https://www.highcharts.com/blog/chartchooser/bar-categorical-comparison/)
    -  Sunburst of the total amount of financings divided by Province and then divided by typology<br>
    [Code example](https://www.highcharts.com/blog/chartchooser/sunburst-categorical-composition/)

### Licences

- **Visualizations:** Highcharts JS which is open-source for non-commercial projects, [Standard Licence Agreement](https://wp-assets.highcharts.com/www-highcharts-com/blog/wp-content/uploads/2022/05/02081809/Highsoft-Standard-License-Agreement-14.1-2.pdf) 
- **Website:** HTML5 template **"Bulma"** by [Jeremy Thomas](https://jgthms.com/), [MIT](https://opensource.org/licenses/mit-license.php), 
  


## 📢 RDF assertion of data
Our metadata are supplied following the [DCAT AP version 2.0.0 guidelines](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/200) to achieve the goal of providing the user with more reusable and interoperable data. The catalogue's – and each dataset– metadata are supplied [here](https://github.com/ChiaraCati/Owater/tree/main/metadata), and each .ttl file has been validated through http://ttl.summerofcode.be/. 

Below we listed metadata used for the catalogue and datasets

|   Metadata       |   Catalogue    |   Datasets   |
|   :---           |   :---         |   :---        |
|   adms:identifier|    ✅          |    ✅          |
|   dct:title      |    ✅          |    ✅          |
|   dct:description|    ✅          |    ✅          |
|   dct:keyword    |    🚫          |    ✅          |
|   dct:issued     |    ✅          |    ✅          |
|   dct:modified   |    ✅          |    ✅          |
|   dct:theme      |    🚫          |    ✅          |
|   dcat:datasets  |    ✅          |    🚫          |
|   dct:publisher  |    ✅          |    ✅          |
|   dct:creator    |    ✅          |    ✅          |
|   dct:contactPoint|   🚫          |    ✅          |
|   dct:source     |    🚫          |    ✅          |
|   dct:language   |    ✅          |    ✅          |
|   dct:distribution|   🚫          |    ✅          |
|   dct:license	   |    ✅          |    ✅          |
|   dct:rights     |    ✅          |    ✅          |
|   dct:rightsHolder|   🚫          |    ✅          |
|   foaf:homepage  |    ✅          |    ✅          |

## 🌈 Final remarks

[Add conclusions]