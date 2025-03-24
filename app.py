import streamlit as st
import pyarrow.dataset as ds
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

# 페이지 제목
st.title("2024 KOBIS Daily Box Office 데이터 분석")

@st.cache_data 
def load_data():
    # path = "/home/tom/data/movie_after/dailyboxoffice"
    path = "data/movie_after_2024.parquet"
    dataset = ds.dataset(path, format="parquet", partitioning="hive")
    df = dataset.to_table().to_pandas()
     # dt를 datetime으로 변환 후 YYYY-MM-DD 문자열로 포맷
    df['dt'] = pd.to_datetime(df['dt'], format='%Y%m%d', errors='coerce')
    return df

df = load_data()
