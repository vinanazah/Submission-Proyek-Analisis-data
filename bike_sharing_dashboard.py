import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Load datasets
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

# Set page config untuk tampilan lebih profesional
st.set_page_config(page_title="Dashboard Sepeda ", page_icon="🚴", layout="wide")

# Sidebar untuk filter
st.sidebar.title("Filter Data")
date_range = st.sidebar.date_input("Rentang Tanggal", [])
weather_filter = st.sidebar.selectbox("Filter Berdasarkan Cuaca", day_df['weathersit'].unique())

# Load logo
logo = Image.open("sepeda.jpeg")
st.sidebar.image(logo, width=150)

# Header utama
st.markdown("<h1 style='text-align: center; color: blue;'>Dashboard Sepeda </h1>", unsafe_allow_html=True)

# KPI Utama
st.markdown("### Statistik Kinerja Utama")
col1, col2, col3 = st.columns(3)

total_rides = day_df['cnt'].sum()
avg_rides = day_df['cnt'].mean()
max_rides = day_df['cnt'].max()

with col1:
    st.metric(label="🚴 Total Perjalanan", value=f"{total_rides:,}")
with col2:
    st.metric(label="📊 Rata-rata Harian", value=f"{avg_rides:.2f}")
with col3:
    st.metric(label="🌟 Hari Terbaik", value=f"{max_rides:,}")

# Grafik Performa Harian dengan Altair
st.markdown("### Grafik Performa Harian")
line_chart = alt.Chart(day_df).mark_line(color='blue').encode(
    x='dteday:T',
    y='cnt:Q',
    tooltip=['dteday:T', 'cnt:Q']
).properties(
    title='Total Perjalanan Harian',
    width=800,
    height=400
)

st.altair_chart(line_chart, use_container_width=True)

# Filter tambahan untuk menampilkan data berdasarkan rentang tanggal
if len(date_range) == 2:
    start_date, end_date = date_range
    filtered_data = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & (day_df['dteday'] <= pd.to_datetime(end_date))]
    
    st.markdown("### Data Perjalanan Berdasarkan Rentang Tanggal")
    st.dataframe(filtered_data)

# Grafik cuaca dengan Altair
st.markdown("### Pengaruh Cuaca Terhadap Jumlah Perjalanan")
weather_data = day_df[day_df['weathersit'] == weather_filter]
bar_chart = alt.Chart(weather_data).mark_bar(color='orange').encode(
    x='dteday:T',
    y='cnt:Q',
    tooltip=['dteday:T', 'cnt:Q']
).properties(
    title='Jumlah Perjalanan Berdasarkan Cuaca',
    width=800,
    height=400
)

st.altair_chart(bar_chart, use_container_width=True)

# Data Hourly Analysis
st.markdown("## Analisis Perjalanan Per Jam")

# Grafik Jumlah Perjalanan Per Jam
hourly_rides = alt.Chart(hour_df).mark_line(color='green').encode(
    x='hr:O',  # hr column should represent hours
    y='cnt:Q',
    tooltip=['hr:O', 'cnt:Q']
).properties(
    title='Jumlah Perjalanan Per Jam',
    width=800,
    height=400
)

st.altair_chart(hourly_rides, use_container_width=True)

