import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Judul Dashboard
st.title("Dashboard Penyewaan Sepeda")

# Deskripsi
st.markdown("""
Dashboard ini menganalisis pengaruh faktor cuaca (temperatur, kelembapan, dan kecepatan angin) terhadap jumlah penyewa sepeda dan 
menunjukkan pola penyewaan sepeda berdasarkan waktu dan hari dalam seminggu.
""")

# Load Data
day_df = pd.read_csv('day.csv')  # Ganti dengan data Anda
hour_df = pd.read_csv('hour.csv')  # Ganti dengan data Anda

# 1. Analisis Korelasi antara Faktor Cuaca dan Jumlah Penyewa
st.header("Pengaruh Faktor Cuaca terhadap Jumlah Penyewa Sepeda")

weather_factors = ['temp', 'hum', 'windspeed', 'cnt']
correlation = day_df[weather_factors].corr()

# Plot heatmap korelasi
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
plt.title('Korelasi antara Faktor Cuaca dan Jumlah Penyewa')
st.pyplot(plt.gcf())

st.markdown("""
**Interpretasi:**
- Korelasi antara suhu (temperatur), kelembapan, dan kecepatan angin terhadap jumlah penyewa sepeda.
- Nilai korelasi antara -1 hingga 1, di mana nilai positif menunjukkan hubungan langsung dan nilai negatif menunjukkan hubungan terbalik.
""")

# 2. Pola Penyewaan Berdasarkan Waktu
st.header("Pola Penyewaan Sepeda Berdasarkan Waktu dan Hari")

# Pola Penyewaan Harian (Line Plot)
daily_pattern = hour_df.groupby('dteday')['cnt'].mean()

plt.figure(figsize=(12, 6))
daily_pattern.plot()
plt.title('Pola Penyewaan Sepeda Harian')
plt.xlabel('Tanggal')
plt.ylabel('Rata-rata Jumlah Penyewa')
st.pyplot(plt.gcf())

st.markdown("""
**Interpretasi:**
- Pola penyewaan harian menunjukkan bagaimana rata-rata jumlah penyewa sepeda berubah setiap hari.
""")

# Pola Mingguan Berdasarkan Jam dan Hari (Heatmap)
hourly_weekday = hour_df.pivot_table(values='cnt', index='hr', columns='weekday', aggfunc='mean')

plt.figure(figsize=(12, 8))
sns.heatmap(hourly_weekday, cmap='YlOrRd', annot=True)
plt.title('Pola Penyewaan Sepeda berdasarkan Jam dan Hari dalam Seminggu')
plt.xlabel('Hari (0 = Minggu, 6 = Sabtu)')
plt.ylabel('Jam')
st.pyplot(plt.gcf())

st.markdown("""
**Interpretasi:**
- Heatmap ini menunjukkan pola penyewaan sepeda berdasarkan jam dan hari. Warna yang lebih terang menunjukkan lebih banyak penyewa sepeda.
- Hari kerja (Senin - Jumat) cenderung memiliki pola penyewaan yang berbeda dengan akhir pekan (Sabtu dan Minggu).
""")

# Jalankan streamlit dengan perintah berikut di terminal:
# streamlit run nama_file.py

