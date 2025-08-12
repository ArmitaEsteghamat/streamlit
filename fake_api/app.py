import streamlit as st
import requests
import pandas as pd

# تنظیمات اولیه صفحه
st.set_page_config(page_title="خواندن API فیک", layout="centered")

st.title("📡 خواندن داده از API  و نمایش در Streamlit")

st.markdown("در این مثال، اطلاعات کاربران را از یک API  می‌خوانیم و در قالب جدول و متن نمایش می‌دهیم.")

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    with st.expander('نمایش داده ها به صورت خام'):
        st.json(data)

    df = pd.DataFrame(data)
    st.subheader('جدول اطلاعات کاربران 🗓️')
    st.dataframe(df[['id','name','email','phone','website']])

    selected_user = st.selectbox('انتخاب کاربر :',df['name'])
    user_info = df[df['name'] == selected_user].iloc[0]

    st.markdown(f"""
    ### 👤اطلاعات کاربر انتخاب شده:
    - **نام کامل:** {user_info['name']}
    - **ایمیل:** {user_info['email']}
    - **تلفن:** {user_info['phone']}
    - **وب سایت:** {user_info['website']}
    """)

else:
    st.error('دریافت داده با خطا مواجه شد❌')
