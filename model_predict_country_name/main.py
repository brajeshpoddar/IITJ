from pathlib import Path
import sys

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from inference import predict_capital

st.title("Country Capital Predictor")

country_name = st.text_input("Enter a country name")

if st.button("Predict capital"):
    if not country_name.strip():
        st.warning("Enter a country name first.")
    else:
        capital = predict_capital(country_name.strip())
        st.write(f"Predicted capital: {capital}")
