# Proposal
Tento dokument je výsledkom práce študentov Tomáša Mifkoviča a Benjamína Jozefa Šiškoviča ako návrh projektu na predmet Neurónové siete na FIIT STU v aka. roku 2019/2020.

## Motivácia
Ako projekt sme si vybrali tému **Určenie veku na základe fotografie**. Táto téma je zaujímavá vo viacerých smeroch, pretože by sa dala ďalej rozvýjať, hlavne ako zabezpečenie naprŕklad mobilných zariadení. V našom prípade by sa skôr mohla použiť na rozpoznanie veku používateľa live v aplikáciach na mobilných zariadeniach alebo počítačoch. 

Taktiež, v čase keď sa na internete mnohokrát zverejňujú detské fotky, ktoré sa dajú ľahko zneužiť, alebo môžu vystaviť deti do nebezpečných či nepríjemných situácií. Rozpoznanie tváre by mohlo znížíť počet takýchto fotografií, keď pri uploade fotiek vyskočí okno s upozornením.

Náš predmet záujmu spočíva hlavne v tom, aby sme vedeli fotky čo najpresnejšie zaradiť do vekových kategórií deti, mladistvý, mladý, dospelý, dôchodca. 

## Podobné práce

## Dataset

## High-level solution proposal
V čase písanie návrhu sme absolvovali prednášku z predmetu o téme zisťovania hrán v obrázkoch. Túto tému si budeme musieť naštudovať podrobnejšie. 
Ako prvý krok budeme určovať pohlavie jedinca na fotke, kedže jedinci v rovnakom veku ale rôznym pohlavím prejavujú inak - vrásky, plešatosť...
Po natrénovaní neurónovej siete na datasetoch spomenutých vyššie vyskúšame fotky

 - naše, teda presne vieme, aký vek sme na nich mali
 - vybraté fotky z datasetov, pre overenie, či je to priamo naučené alebo nastane nejaká odchylka 
 - fotky z AIS
 
 Údaje, ktoré nám poskytne neurónová sieť porovnáme so skutočnými hodnotami a tak vypočítame odchylku hodnôt. Budeme sa zároveň sústrediť, v ktorom veku nastala najväčšia odchylka a zistíme, prečo sa tak stalo.
 
 -  _Related Work_ - Shortly describe how were similar problems solved by other people.
 -  _Datasets_ - What datasets exist that can be used to train the task, how much data is available, what are the properties of these data.


