import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title='رسم نمودار با plotly', layout='centered')
st.title('نمودار تعاملی با استفاده از plotly 📊')

# data = {
#     ['فروردین', 'اردیبهشت', 'خرداد', 'تیر']: 'ماه',
#     [250, 300, 200, 150]: 'فروش',
#     [160, 180, 120, 100]: 'هزینه'
# }

data = {
    "ماه": ["فروردین", "اردیبهشت", "خرداد", "تیر"],
    "فروش": [150, 200, 300, 250],
    "هزینه": [100, 120, 180, 160]
}

df = pd.DataFrame(data)

fig = px.bar(df, x='ماه', y=['هزینه', 'فروش'], barmode='group', title='مقایسه فروش و هزینه',
             labels={'value': 'مقدار', 'variable': 'نوع'})

st.plotly_chart(fig,use_container_width=True)
