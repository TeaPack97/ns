
# Proposal  
Tento dokument je výsledkom práce študentov Tomáša Mifkoviča a Benjamína Jozefa Šiškoviča ako návrh projektu na predmet Neurónové siete na FIIT STU v aka. roku 2019/2020.  
  
## Motivácia  
Ako projekt sme si vybrali tému ****Určenie veku na základe fotografie****. Táto téma je zaujímavá vo viacerých smeroch, pretože by sa dala ďalej rozvýjať, hlavne ako zabezpečenie napríklad mobilných zariadení. V našom prípade by sa skôr mohla použiť na rozpoznanie veku používateľa live v aplikáciach na mobilných zariadeniach alebo počítačoch.  
  
Taktiež, v čase keď sa na internete mnohokrát zverejňujú detské fotky, ktoré sa dajú ľahko zneužiť, alebo môžu vystaviť deti do nebezpečných či nepríjemných situácií. Rozpoznanie tváre by mohlo znížíť počet takýchto fotografií, keď pri uploade fotiek vyskočí okno s upozornením.  
  
Náš predmet záujmu spočíva hlavne v tom, aby sme vedeli fotky čo najpresnejšie zaradiť do vekových kategórií deti, mladistvý, mladý, dospelý, dôchodca.  
  
## Podobné práce  
V dnešnom modernom svete existuje veľa rozličných riešení na daný problém. Väčšina veľkých celosvetových firiem si buduje vlastné softvéry alebo služby, ktoré implementujú určitú formu umelej inteligencie (presnejšie neurónovú sieť) na rozpoznanie tváre tzv. face recognition, ktorá sa neustále učí používaním API. Každá takáto spoločnosť si model buduje, trénuje a testuje sama (väčšinou bez zverejnenia svojeho know-how). Medzi takéto firmy môžme zaradiť Apple, Microsoft, Google, či iné. Ako najznámejší príklad na rozpoznanie tváre môžme použiť FaceID od spoločnosti Apple.  
  
****How-old.net**** - webová stránka od spoločnosti Microsoft, ktorá dokáže z fotky identifikovať tvár človeka a snaží sa uhádnuť pohlavie a vek osoby na fotke  
  
****[aws.amazon.com/rekognition](https://l.facebook.com/l.php?u=http%3A%2F%2Faws.amazon.com%2Frekognition%3Ffbclid%3DIwAR3iEaIrIPUXmKaZK5Bbalfv2Iolo7zZ6QeZLh_OZYXOU7I-HCUGinbSqPk&h=AT3tWLPu8hdlVrodHoLUsLshIt7cxJB_bb1chxdPR4-5RY-_QP4ePzhkE3vrMMVZpUnx_2BzRNDtiivWtoP9DS5kIuMyoR1pCrAqSN-mZDkSYT7DfzKJmwNcTJs)**** - je projekt spoločnosti Amazon, ktorý dokáže rozpoznávať z videí a fotiek rôzne objekty, ale predovšetkým aj tváre ľudí. Aplikácia dokáže zistiť pohlavie človeka, či sa usmieva, či je šťastný či má okuliare a pod.  
  
****[https://www.learnopencv.com/age-gender-classification-using-opencv-deep-learning-c-python/?fbclid=IwAR0rxSPssBGnjFOm3WsMx3jp7hqA24hicUu4iFADi9DrNjj0qQaALCERGuU](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.learnopencv.com%2Fage-gender-classification-using-opencv-deep-learning-c-python%2F%3Ffbclid%3DIwAR0-TjKPteiZV8VWnH_uVZ4k3cudK6iSWSiuVb0uC4UKeB243TwFGe-3UNU&h=AT3tWLPu8hdlVrodHoLUsLshIt7cxJB_bb1chxdPR4-5RY-_QP4ePzhkE3vrMMVZpUnx_2BzRNDtiivWtoP9DS5kIuMyoR1pCrAqSN-mZDkSYT7DfzKJmwNcTJs)**** - je open-source riešenie na tento problém. V tomto riešení používajú konvolučnú neurónovú sieť (3 konvolučné vrstvy, 2 plne prepojené vrstvy a 1 výstupnú vrstvu). Neurónová sieť odhaduje vek a pohlavie osoby na fotke. Vek odhaduje klasifikačným prístupom - čiže snaží sa odhadnúť vekovú skupinu ľudí namiesto presného veku. V takomto prípade sú výsledky presnejšie a oveľa jednoduchšie vypočítať výsledok.  
## Dataset  
Aby sme vedeli náš model čo najlepšie vytrénovať a kvalitne ho otestovať, potrebujeme veľké množstvo fotiek. Dolu vypísané webové linky nám poskytujú voľne dostupný zdroj fotiek osôb spolu s dodatočnými informáciami ako pohlavie či vek osoby na fotke.  
  
****[https://talhassner.github.io/home/projects/Adience/Adience-data.html](https://l.facebook.com/l.php?u=https%3A%2F%2Ftalhassner.github.io%2Fhome%2Fprojects%2FAdience%2FAdience-data.html%3Ffbclid%3DIwAR133qYxnhoqIIyKc5RcXZylKH-VDTnn5ElPblOw8nxmMzjoJHuCgLOEO6A&h=AT3tWLPu8hdlVrodHoLUsLshIt7cxJB_bb1chxdPR4-5RY-_QP4ePzhkE3vrMMVZpUnx_2BzRNDtiivWtoP9DS5kIuMyoR1pCrAqSN-mZDkSYT7DfzKJmwNcTJs)**** - The Open University of Israel poskytujú databázu nefiltrovaných snímok tvári ľudí na klasifikáciu pohlavia a veku človeka (celkovo 26 580 snímok) s 8 vekovými skupinami (0-2, 4-6, 8-13, 15-20, 25-32, 38-43, 48-53, 60-)  
  
****[https://github.com/JingchunCheng/All-Age-Faces-Dataset?fbclid=IwAR0xZCjKKWhJBbce__VZdTO4SN62hbn_45pbB-h6AgO-gDboi_d9vNjOqQY](https://github.com/JingchunCheng/All-Age-Faces-Dataset?fbclid=IwAR3sesRO_P9-hGeQN2xfupIsEbIuUNNH2Ul_wPLgaH32d-O6ivTsBIv567A)**** - voľne dostupný zdroj fotiek tvári ľudí prevažne z ázie. Celkový počet je 13 322 fotiek s vekovým rozpätím od 2 do 80 rokov.  
  
****[https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/?fbclid=IwAR07Vw9R8yi2P_D5EiXBCfZ3CYeNo92b5Z9ZWkuHo_tnWoq_8Aw5TRvhxWQ](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/?fbclid=IwAR2gdfJaA7KQTlDkklFt-F6FykOHYWlTSxy2IFt7ozbznOMBQzeBGdDgKzo)**** - voľne dostupná databáza fotiek z celého sveta, ktoré sú vhodné na trénovanie a testovanie neurónových sietí. Celkový počet je viac ako 500 000.  
  
****[https://susanqq.github.io/UTKFace/?fbclid=IwAR2IuscY8oJ6ubuUdKCMRgCtZ0ZQJ38VMMykgbwK7WZK3LLvszBGp26HOyY](https://susanqq.github.io/UTKFace/?fbclid=IwAR1D0BTb3iHv6Kdis_5BjvzuridO1z74BsgsPj-sC7iMMZm66UztECDFOro)**** - voľne dostupná databáza fotiek poskytujúca doplňujúce informácie o fotkách s celkovým počtom viac ako 20 000.  
  
## High-level solution proposal  
V čase písania návrhu sme absolvovali prednášku z predmetu o téme zisťovania hrán v obrázkoch. Túto tému si budeme musieť naštudovať podrobnejšie.  
Po natrénovaní neurónovej siete na datasetoch spomenutých vyššie vyskúšame fotky  
  
- naše, teda presne vieme, aký vek sme na nich mali  
- vybraté fotky z datasetov, pre overenie, či je to priamo naučené alebo nastala nejaká odchylka  
- fotky z AIS  
  
Údaje, ktoré nám poskytne neurónová sieť porovnáme so skutočnými hodnotami a tak vypočítame odchylku hodnôt. Budeme sa zároveň sústrediť, v ktorom veku nastala najväčšia odchylka a zistíme, prečo sa tak stalo.
