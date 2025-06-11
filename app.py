import streamlit as st
import pandas as pd
import joblib

# Chargement du modèle
pipeline = joblib.load("quantity_pipeline.pkl")

# Titre
st.title("📊 Application de Prédiction des ventes et quantités")

# Partie 1 : Type de prédiction temporelle
st.header("🧠 Partie 1 : Choix du type de prédiction temporelle")
granularite = st.selectbox("Niveau de granularité temporelle :", ["Année", "Mois"])
annee = st.selectbox("Année", list(range(2015, 2026)), index=0)
mois = st.selectbox("Mois", list(range(1, 13)), index=0) if granularite == "Mois" else 1

# Partie 2 : Type de produit
st.header("📦 Partie 2 : Type de produit")
filtre_produit = st.radio("Filtrer les produits par :", ["Tous les produits", "Par catégorie", "Par sous-catégorie"])

# Champs dynamiques selon le filtre
categorie = sous_categorie = None
if filtre_produit == "Par catégorie":
    categorie = st.selectbox("Catégorie", ["Furniture", "Office Supplies", "Technology"])
elif filtre_produit == "Par sous-catégorie":
    sous_categorie = st.selectbox("Sous-catégorie", ["Bookcases", "Chairs", "Phones", "Binders", "Storage", "Accessories"])

# Données d’entrée
input_data = pd.DataFrame([{
    "Order_Year": annee,
    "Order_Month": mois,
    "Category": categorie if categorie else "None",
    "Sub-Category": sous_categorie if sous_categorie else "None",
}])

# Prédiction
if st.button("🔮 Prédire la Quantité"):
    prediction = pipeline.predict(input_data)
    st.success(f"📦 Quantité estimée : {int(prediction[0])} unités")
