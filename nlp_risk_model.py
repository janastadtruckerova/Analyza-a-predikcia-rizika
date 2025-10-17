# Python Kód (TF-IDF a Klasifikácia)
# Keďže sme SQL dopyty len simulovali (vytvorili sme si premenné, ktoré SQL vracia), v Pythone budeme simulovať celý proces: od textu až po finálnu predikciu rizika.
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# =====================================================================
# KROK 1: NLP DÁTA (Simulácia Predspracovaného Textu z Labu Úverov)
# =====================================================================

# Simulácia poznámok k žiadostiam o úver (očistené od stop words a interpunkcie)
mock_dokumenty = [
    "klient nepredlozil doklady zameskanie platba predosly uver",
    "schvalene bez problemov nizke riziko podla skorngu",
    "exekucia zablokovane ucty vysoke riziko schvalenie zamietnute",
    "nova ziadost klient stabilny prijem bez problemov",
    "zameskanie platba sudy prebieha kontrola dokumenty zlozite",
    "nizke riziko schvalene rychle vybavenie labom"
]

# Cieľová Premenná pre Modelovanie (Riziko úveru: 1 = Vysoké/Zlyhanie, 0 = Nízke/Schválené)
riziko = [1, 0, 1, 0, 1, 0]


# =====================================================================
# KROK 2: TF-IDF VEKTORIZÁCIA (Premena textu na váhy)
# =====================================================================

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(mock_dokumenty)

# Konverzia TF-IDF matice na Pandas DataFrame pre ľahšie spojenie
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())

# Zjednodušená verzia: Vyberáme len tie najdôležitejšie features (napr. exekucia a zameskanie)
# V reálnom projekte by sme vybrali viac, ale pre ukážku stačí kľúčový dôkaz.
tfidf_df_selected = tfidf_df[['exekucia', 'zameskanie']]


# =====================================================================
# KROK 3: SPOJENIE S SQL DÁTAMI A MODELOVANIE
# =====================================================================

# Simulácia SQL Features (TAT = Turnaround Time)
# Tieto dáta pochádzajú zo simulovaného SQL súboru
sql_features = {
    'TAT_dni': [15, 3, 22, 5, 25, 4]
}
sql_df = pd.DataFrame(sql_features)

# Finálne spojenie všetkých dát
X = pd.concat([sql_df, tfidf_df_selected], axis=1)
y = pd.Series(riziko)

print("Finálny Dátový Súbor pre Model (SQL + NLP Features):")
print(X)


# =====================================================================
# KROK 4: KLASIFIKÁCIA RIZIKA (Logistická Regresia)
# =====================================================================

# Delenie dát (aby sme ukázali, že model trénujeme/testujeme)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Trénovanie modelu - Prezentujte, že dokážete použiť klasifikačný model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predikcia a vyhodnotenie (ukážka, že model funguje)
predictions = model.predict(X_test)
score = model.score(X_test, y_test)

print(f"\nModel bol úspešne natrénovaný. Presnosť (Accuracy) na testovacej sade: {score:.2f}")
print("\nKľúčové zistenia (Koeficienty modelu - čo zvyšuje riziko):")
print(pd.Series(model.coef_[0], index=X.columns))
