import streamlit as st
import altair as alt
import pandas as pd

st.set_page_config(page_title='نمودار با altair', layout='centered')

st.title('نمودار با استفاده از altair📊')

df = pd.DataFrame({
    'روز': ['شنبه', 'یکشنبه', 'دوشنبه', 'سه شنبه', 'چهارشنبه'],
    'فروش': [130, 170, 100, 150, 1500]
})

chart = alt.Chart(df).mark_line(point=True).encode(x='روز', y='فروش').properties(title='روند فروش روزانه')


st.altair_chart(chart, use_container_width=True)