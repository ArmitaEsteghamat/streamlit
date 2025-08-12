import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt
from io import StringIO

st.set_page_config(page_title='داشبورد تحلیل فروش', layout='wide')

st.markdown('''
    <style>
        body ,stApp{
            direction:rtl;
            text-align:right;
            font-family:IranSans,sans-serif;
        }
    
    </style>
''', unsafe_allow_html=True)

st.title('📊 داشبورد تحلیل فروش ')

uploaded_file = st.file_uploader('لطفا فایل csv فروش را بارگزاری کنید!', type=['csv'])

if uploaded_file:
    # خواندن فایل CSV
    df = pd.read_csv(uploaded_file)

    # نمایش پیش‌نمایش از داده‌ها
    st.subheader("پیش‌نمایش داده‌ها")
    st.dataframe(df.head())

    # بررسی وجود ستون‌های کلیدی
    required_columns = ["تاریخ", "فروش", "سود"]
    if not all(col in df.columns for col in required_columns):
        st.error("فایل باید شامل ستون‌های: تاریخ، فروش، سود باشد")
    else:
        # تبدیل ستون تاریخ به datetime
        df["تاریخ"] = pd.to_datetime(df["تاریخ"])

        # استخراج سال و ماه برای فیلتر
        df["سال"] = df["تاریخ"].dt.year
        df["ماه"] = df["تاریخ"].dt.strftime("%B")

        # --- فیلتر بازه زمانی ---
        st.sidebar.header("📅 فیلتر بازه تاریخی")
        min_year, max_year = df["سال"].min(), df["سال"].max()
        selected_year = st.sidebar.slider("سال", min_year, max_year, max_year)

        # فیلتر بر اساس سال انتخابی
        filtered_df = df[df["سال"] == selected_year]

        # نمایش آمار به صورت کلی
        st.subheader('📌آمار کلی')
        col1, col2 = st.columns(2)
        col1.metric('مجموع فروش', f'{filtered_df['فروش'].sum():,.0f} تومان')
        col2.metric('مجموع سود', f'{filtered_df['سود'].sum():,.0f} تومان')

        # نمودار خطی فروش با Matplotlib
        st.subheader('📈 روند فروش(Matplotlib)')
        daily_sales = filtered_df.groupby('تاریخ')['فروش'].sum()

        fig, ax = plt.subplots()
        ax.plot(daily_sales.index, daily_sales.values, color='blue', marker='o')
        ax.set_title('روند فروش روزانه')
        ax.set_xlabel('تاریخ')
        ax.set_ylabel('فروش')

        st.pyplot(fig)

        # --- نمودار ۲: نمودار ستونی با Plotly ---
        st.subheader('📊 فروش ماهانه')
        monthly_data = filtered_df.groupby('ماه')[['سود', 'فروش']].sum().reset_index()

        months_order = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن',
                        'اسفند']

        # monthly_data['ماه'] = pd.Categorical(monthly_data['ماه'], categories=months_order, ordered=True)
        # monthly_data = monthly_data.sort_values('ماه')

        fig2 = px.bar(monthly_data, x='ماه', y=['سود', 'فروش'],
                      barmode='group',
                      labels={'value': 'مقدار', 'variable': 'نوع'},
                      title='مقایسه فروش و سود ماهیانه')

        st.plotly_chart(fig2, use_container_width=True)

        # --- نمودار ۳: نمودار پراکندگی سود با Altair ---
        st.subheader("📉 پراکندگی سود (Altair)")
        alt_chart = alt.Chart(filtered_df).mark_circle(size=60).encode(
            x='تاریخ:T',
            y='سود:Q',
            tooltip=['سود', 'تاریخ']
        ).properties(
            width=700,
            height=400,
            title='پراکندگی سود در روزهای مختلف'
        )
        st.altair_chart(alt_chart, use_container_width=True)

else:
    st.info('برای شروع ، یک فایل فروش را بارگزاری کنید!')
