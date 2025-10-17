# Projekt: Analýza a Predikcia Rizika v Procese Schvaľovania Poistných Zmlúv

## 1. Prehľad Projektu

Tento projekt demonštruje moju schopnosť premostiť dlhoročné skúsenosti v **procesnej a rizikovej analýze** s modernými nástrojmi **Dátovej Vedy (Python, SQL, NLP)**. Cieľom je identifikovať a kvantifikovať faktory v procese schvaľovania poistných zmlúv, ktoré vedú k vyššiemu riziku (napr. storno, nesplácanie, strata klienta).

Projekt je rozdelený na tri fázy:

1.  **SQL Feature Engineering:** Tvorba **kvantifikovateľných prediktorov** z procesných a klientskych dát.
2.  **NLP Feature Engineering:** Prevedenie **neštruktúrovaného textu** (poznámky úradníkov) na číselné prediktory rizika.
3.  **Modelovanie Rizika:** Trénovanie jednoduchého klasifikačného modelu na predikciu rizikových prípadov.

## 2. Metodika a Technický Zásobník

### **Fáza A: Príprava Dát v SQL (Feature Engineering)**

V tejto fáze simulujem dátové transformácie s cieľom vytvoriť prediktívne stĺpce pre model. Hoci mám základné znalosti SQL, dokážem efektívne vytvárať metriky:

* **Vytvorené SQL Metriky:**
    * **Procesný TAT (Turnaround Time):** Výpočet priemernej doby spracovania zmluvy v jednotlivých fázach (pomocou dátových funkcií a `DATE_DIFF`). *Biznis hodnota: Identifikácia úzkych miest v procese.*
    * **Miera Konverzie:** Výpočet úspešnosti schválenia zmluvy na základe typu produktu alebo pobočky (pomocou `JOINs` a `GROUP BY`).
* **Použité Nástroje:** SQL (DQL a DML pre transformáciu dát), Pandas (pre simuláciu načítania a čistenia dát).

### **Fáza B: NLP – Analýza Poznámok **

Momentálne pracujem na implementácii NLP, ktoré premení textové poznámky k zmluvám na číselné prediktory.

* **Kľúčový NLP Krok:** **TF-IDF Vektorizácia.** Namiesto spoliehania sa len na frekvenciu slov, TF-IDF váhy zistia, ktoré **zriedkavé, ale dôležité slová** (napr. "súd", "exekúcia", "nezrovnalosť") najlepšie predpovedajú vysoké riziko.
* **Nástroje:** Python (NLTK, spaCy), Scikit-learn (pre TF-IDF).

## 3. Výsledok a Budúci Krok

**Cieľový Výstup (Proof of Concept):**
Demonštrácia kompletného dátového potrubia (pipeline), kde surové procesné dáta (SQL) a neštruktúrovaný text (NLP) tvoria **finálny Feature Set** (v Pythone), ktorý je pripravený pre **Klasifikačný Model** (napr. Logistická Regresia/Random Forest) na predikciu storno zmluvy.

---

## **Ďalšie Zručnosti a Kontakt**

Som kandidátka s **overenou pracovnou etikou** a **vášňou pre sebavzdelávanie**, čo mi umožňuje rýchlo sa adaptovať. Hľadám príležitosť dokázať svoju hodnotu a procesnú logiku vo vašom dátovom tíme.

* **Kontakt:** janastadtruckerova@gmail.com
* **LinkedIn:** https://www.linkedin.com/in/jana-stadtruckerov%C3%A1-7801779b/
* **Kód K Dispozícii:** (Kód pre SQL/Pandas/NLTK je v súboroch analyza rizika.sql a nlp_risk_model.py.)
