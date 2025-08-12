import streamlit as st
import pandas as pd

st.title('آپلود فایل CSV')

csv_file = st.file_uploader('لطفا فایل csv خود را انتخاب کنید',type=['csv'])

if csv_file is not None:
    df = pd.read_csv(csv_file)

    st.subheader('پیش نمایش دیتا')
    st.dataframe(df)

    st.subheader('خلاصه آماری')
    st.write(df.describe())