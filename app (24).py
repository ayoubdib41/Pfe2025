
import streamlit as st
import pandas as pd
import joblib
import gzip

with gzip.open("quantity_pipeline_compressed.pkl.gz", "rb") as f:
    pipeline = joblib.load(f)

st.title("📊 Application de Prédiction des ventes et quantités")

st.header("🧠 Partie 1 : Choix du type de prédiction temporelle")
granularite = st.selectbox("Niveau de granularité temporelle :", ["Année", "Mois dans une année"])
annee = st.selectbox("Année", list(range(2015, 2026)), index=0)
mois = st.selectbox("Mois", list(range(1, 13)), index=0) if granularite == "Mois dans une année" else 1

st.header("📦 Partie 2 : Type de produit")
filtre = st.radio("Filtrer les produits par :", ["Tous les produits", "Par catégorie", "Par sous-catégorie"])

category = "All"
sub_category = "All"

if filtre == "Par catégorie":
    category = st.selectbox("Sélectionner la catégorie :", ["Furniture", "Office Supplies", "Technology"])
elif filtre == "Par sous-catégorie":
    sub_category = st.selectbox("Sélectionner la sous-catégorie :", [
        "Bookcases", "Chairs", "Phones", "Binders", "Storage", "Accessories"
    ])

if st.button("🔮 Prédire la quantité vendue"):
    input_data = {
        "Order_Year": annee,
        "Order_Month": mois,
        "Discount": 0.0,
        "Category": category if category != "All" else "Furniture",
        "Sub-Category": sub_category if sub_category != "All" else "Chairs",
        "Region": "East",
        "Segment": "Consumer",
        "Ship Mode": "Standard Class"
    }

    df_input = pd.DataFrame([input_data])
    prediction = pipeline.predict(df_input)
    st.success(f"📦 Quantité prédite : {int(prediction[0])} unités")
