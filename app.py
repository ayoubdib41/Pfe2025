
import streamlit as st
import pandas as pd
import joblib

# Chargement du pipeline entraîné
pipeline = joblib.load("quantity_pipeline.pkl")

# Titre
st.title("📦 Prédiction de Quantité Vendue (Superstore)")

# Formulaire dynamique
st.subheader("🧮 Paramètres de prédiction")

# Choix de période
periode = st.selectbox("Période de prédiction", ["Mensuelle", "Annuelle"])
year = st.selectbox("Année", list(range(2015, 2026)), index=3)
month = st.selectbox("Mois", list(range(1, 13)), index=0) if periode == "Mensuelle" else 1
discount = st.slider("Remise (%)", min_value=0.0, max_value=0.9, step=0.05, value=0.0)

# Catégories
category = st.selectbox("Catégorie", ["Furniture", "Office Supplies", "Technology"])
sub_category = st.selectbox("Sous-catégorie", ["Bookcases", "Chairs", "Phones", "Binders", "Storage", "Accessories"])
region = st.selectbox("Région", ["East", "West", "Central", "South"])
segment = st.selectbox("Segment", ["Consumer", "Corporate", "Home Office"])
ship_mode = st.selectbox("Mode de livraison", ["Standard Class", "Second Class", "First Class", "Same Day"])

# Préparation des données d’entrée
input_df = pd.DataFrame([{
    "Order_Year": year,
    "Order_Month": month,
    "Discount": discount,
    "Category": category,
    "Sub-Category": sub_category,
    "Region": region,
    "Segment": segment,
    "Ship Mode": ship_mode
}])

# Prédiction
if st.button("🔮 Prédire la Quantité"):
    prediction = pipeline.predict(input_df)
    st.success(f"📦 Quantité estimée : {int(prediction[0])} unités")
