# Streamlit ilovasi
import streamlit as st
import pickle
import numpy as np

# Modelni yuklash
with open("airmodel2.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit sarlavhasi
st.title("Xavo sifatini bashorat qilish")
st.write("Bashorat uchun ma'lumotlaringizni kiriting.")

# Foydalanuvchi kiritadigan qiymatlar
st.header("Bashorat uchun ma'lumot kiritish")
indicator_id = st.number_input("Indicator ID", min_value=1, max_value=1000, value=640)
geo_join_id = st.slider("Geo Join ID", min_value=100.0, max_value=500.0, value=409.0)
data_value = st.slider("Data Value", min_value=0.1, max_value=20.0, value=0.3)

# Bashorat
if st.button("Bashorat qilish"):
    input_data = np.array([[indicator_id, geo_join_id, data_value]])
    prediction = model.predict(input_data)
    st.success(f"Bashorat qilingan qiymat: {prediction[0]:.2f}")
