# SQL Fáza: Vytvorenie Procesných Prediktorov (Feature Engineering)
# Cieľom SQL je transformovať surové dáta z databázových tabuliek na číselné metriky, ktoré odrážajú riziko v procese spracovania úveru. Tieto metriky sa potom spoja s vašou TF-IDF maticou a pôjdu do modelu.
# Simulácia Dát a Kľúčové Tabuľky:
# Žiadosti, proces_log(sledovanie procesov) a klienti
# Feature: Turnaround Time (TAT) – Rýchlosť Procesu
# Problém: Dlhý čas spracovania žiadosti zvyšuje riziko, že klient odíde, alebo že sa zmení jeho finančná situácia. Zručnosť: Použitie dátových funkcií (DATEDIFF alebo DATE_DIFF) a JOINov.
SELECT
    t1.id_ziadosti,
    -- Vypočítaj rozdiel v dňoch medzi podaním a finálnym rozhodnutím
    DATEDIFF('DAY', t1.datum_podania, t2.datum_ukoncenia_fazy) AS TAT_dni
FROM ZIADOSTI t1
JOIN PROCES_LOG t2 ON t1.id_ziadosti = t2.id_ziadosti
WHERE t2.faza_procesu = 'Finalne_Rozhodnutie';
# Feature: Miera Konverzie Pobočky
SELECT
    p.pobocka_id,
    -- Výpočet podielu schválených žiadostí k celkovému počtu
    CAST(SUM(CASE WHEN z.schvaleny_stav = 'Schvaleny' THEN 1 ELSE 0 END) AS REAL) / COUNT(z.id_ziadosti) AS Miera_Schvalenia
FROM ZIADOSTI z
JOIN KLIENTI k ON z.id_klienta = k.id_klienta -- Ak pobočka je v klientoch
GROUP BY p.pobocka_id
ORDER BY Miera_Schvalenia DESC;
