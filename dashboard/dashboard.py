import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
def load_data():
    data_hari = pd.read_csv('https://raw.githubusercontent.com/abhararzaqi/projekdicoding/refs/heads/main/data/day.csv')
    data_jam = pd.read_csv('https://raw.githubusercontent.com/abhararzaqi/projekdicoding/refs/heads/main/data/hour.csv')
    return data_hari, data_jam

data_hari, data_jam = load_data()



# Transformations
def preprocess_hour_data(data):
    # Kategori cuaca
    def categorize_weather(row):
        if row['weathersit'] == 1:
            return 'Cerah'
        elif row['weathersit'] == 2:
            return 'Mendung / Berkabut'
        elif row['weathersit'] == 3:
            return 'Gerimis / Hujan Salju'
        else:
            return 'Hujan Deras / Badai / Badai Salju'

    # Kategori hari
    def categorize_day(row):
        if row['holiday'] == 0 and row['workingday'] == 1:
            return 'Hari Kerja'
        elif row['holiday'] == 1 and row['workingday'] == 0:
            return 'Hari Libur'
        else:
            return 'Akhir Pekan'

    data['weather_category'] = data.apply(categorize_weather, axis=1)
    data['day_category'] = data.apply(categorize_day, axis=1)
    return data

hour_data = preprocess_hour_data(data_jam)

# Streamlit Layout
st.title("Dashboard Analisis Penyewaan Sepeda")

# Display raw data
if st.checkbox("Tampilkan Data Mentah"):
    st.write("**Data Harian:**")
    st.dataframe(data_hari.head())
    st.write("**Data Jam:**")
    st.dataframe(hour_data.head())

# Visualizations
st.header("Visualisasi Data")

# Penyewaan berdasarkan cuaca
st.subheader("Penyewaan Berdasarkan Cuaca")
fig, ax = plt.subplots()
sns.barplot(x='weather_category', y='cnt', data=hour_data, estimator=sum, ci=None, palette="viridis", ax=ax)
ax.set_title("Total Penyewaan Sepeda Berdasarkan Cuaca")
st.pyplot(fig)

# Penyewaan berdasarkan kategori hari
st.subheader("Penyewaan Berdasarkan Kategori Hari")
fig, ax = plt.subplots()
sns.barplot(x='day_category', y='cnt', data=hour_data, estimator=sum, ci=None, palette="magma", ax=ax)
ax.set_title("Total Penyewaan Sepeda Berdasarkan Kategori Hari")
st.pyplot(fig)

# Gabungan cuaca dan hari
st.subheader("Penyewaan Berdasarkan Cuaca dan Kategori Hari")
fig, ax = plt.subplots()
sns.barplot(x='day_category', y='cnt', hue='weather_category', data=hour_data, estimator=sum, ci=None, palette="plasma", ax=ax)
ax.set_title("Total Penyewaan Sepeda Berdasarkan Cuaca dan Kategori Hari")
st.pyplot(fig)

# Kesimpulan
st.header("Kesimpulan")
st.write("""
- Penyewaan sepeda paling banyak terjadi pada hari kerja, terutama saat cuaca cerah.
- Penyewaan pada hari libur cenderung lebih sedikit dibandingkan akhir pekan.
- Cuaca cerah adalah waktu paling populer untuk bersepeda, diikuti oleh cuaca mendung.
""")