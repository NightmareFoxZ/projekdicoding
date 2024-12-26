import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title dan Deskripsi
st.title("Dashboard Analisis Penyewaan Sepeda")
st.write("""
Analisis ini dilakukan berdasarkan dataset **Bike Sharing Dataset** untuk melihat pola penyewaan sepeda berdasarkan cuaca, hari, dan kombinasi keduanya.
""")

# Upload Dataset
@st.cache
def load_data():
    data_hari = pd.read_csv('https://github.com/abhararzaqi/projekdicoding/blob/0d18758639986b9203ae6673386ed72064b4fb8e/data/day.csv')
    data_jam = pd.read_csv('https://github.com/abhararzaqi/projekdicoding/blob/0d18758639986b9203ae6673386ed72064b4fb8e/data/hour.csv')
    return data_hari, data_jam

data_hari, data_jam = load_data()

# Menampilkan Data
st.subheader("Data Hari")
st.dataframe(data_hari.head())

st.subheader("Data Jam")
st.dataframe(data_jam.head())

# Visualisasi Cuaca
st.subheader("Total Penyewaan Berdasarkan Cuaca")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=data_jam, estimator=sum, ci=None, palette="viridis", ax=ax1)
ax1.set_title("Total Penyewaan Berdasarkan Cuaca")
st.pyplot(fig1)

# Visualisasi Hari
st.subheader("Total Penyewaan Berdasarkan Hari")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x='workingday', y='cnt', data=data_jam, estimator=sum, ci=None, palette="magma", ax=ax2)
ax2.set_title("Total Penyewaan Berdasarkan Hari")
st.pyplot(fig2)

# Visualisasi Kombinasi
st.subheader("Total Penyewaan Berdasarkan Cuaca dan Hari")
fig3, ax3 = plt.subplots(figsize=(12, 6))
sns.barplot(x='workingday', y='cnt', hue='weathersit', data=data_jam, estimator=sum, ci=None, palette="plasma", ax=ax3)
ax3.set_title("Total Penyewaan Berdasarkan Cuaca dan Hari")
st.pyplot(fig3)

# Kesimpulan
st.subheader("Kesimpulan")
st.write("""
1. Penyewaan sepeda paling banyak terjadi pada hari kerja.
2. Cuaca cerah paling diminati untuk penyewaan sepeda.
3. Kombinasi hari kerja dan cuaca cerah menghasilkan jumlah penyewaan terbanyak.
""")
