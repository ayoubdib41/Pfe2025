import streamlit as st
import pandas as pd
import joblib

# Chargement du modèle
pipeline = joblib.load("sales_pipeline.pkl")

# Configuration de la page
st.set_page_config(page_title="Prédiction des Ventes", page_icon="📈")

# Titre
st.title("📈 Prédiction des ventes - Superstore")

# Style CSS pro
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #f8f9fa, #e9ecef);
    color: #212529;
    font-family: 'Segoe UI', sans-serif;
}
h1, h2, h3 {
    color: #0d6efd;
}
.stButton > button {
    background-color: #0d6efd;
    color: white;
    border: none;
    border-radius: 6px;
}
.stButton > button:hover {
    background-color: #0b5ed7;
}
</style>
""", unsafe_allow_html=True)

st.subheader("🧮 Paramètres de prédiction")

# Choix de la période
periode = st.selectbox("Période de prédiction", ["Mensuelle", "Trimestrielle", "Annuelle"])

# Champs nécessaires
year = st.number_input("Année de commande", min_value=2015, max_value=2025, value=2024)
month = st.selectbox("Mois", list(range(1, 13)), index=0)
discount = st.slider("Remise (%)", min_value=0.0, max_value=0.9, step=0.05, value=0.0)

category = st.selectbox("Catégorie", ["Furniture", "Office Supplies", "Technology"])
sub_category = st.selectbox("Sous-catégorie", ["Bookcases", "Chairs", "Phones", "Binders", "Storage", "Accessories"])
region = st.selectbox("Région", ["East", "West", "Central", "South"])
segment = st.selectbox("Segment", ["Consumer", "Corporate", "Home Office"])
ship_mode = st.selectbox("Mode de livraison", ["Standard Class", "Second Class", "First Class", "Same Day"])

# Simulation raisonnable de valeurs internes nécessaires au modèle
input_data = pd.DataFrame([{
    "Order_Year": year,
    "Order_Month": month,
    "Discount": discount,
    "Category": category,
    "Sub-Category": sub_category,
    "Region": region,
    "Segment": segment,
    "Ship Mode": ship_mode,
    "Quantity": 5,  # Valeur par défaut
    "Profit": 100.0  # Estimation moyenne
}])

# Prédiction
if st.button("🔮 Prédire les ventes"):
    prediction = pipeline.predict(input_data)
    st.success(f"📊 Prédiction ({periode}) : {prediction[0]:.2f} $")
