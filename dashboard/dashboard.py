import analisispenjualaansepeda  # Import file yang dihasilkan dari Jupyter Notebook
import streamlit as st

st.title("Dashboard Analisis")
st.write("Berikut hasil analisis:")
st.pyplot(analisispenjualaansepeda.plot_data())  # Contoh memanggil fungsi plotting