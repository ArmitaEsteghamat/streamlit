import pandas as pd
import streamlit as st
from PIL import Image
import base64

st.set_page_config(page_title='آپلود و نمایش فایل ها', layout='centered')

# --- استایل راست‌چین و فونت فارسی ---
st.markdown("""
    <style>
        body, .stApp {
            direction: rtl;
            text-align: right;
            font-family: IRANSans, Tahoma, sans-serif;
        }
        input, select, textarea {
            direction: rtl;
            text-align: right;
        }
        .row-widget.stRadio > div {
            flex-direction: row-reverse;
        }
        .css-18e3th9 {
            padding: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

st.title('آپلود و نمایش فایل ها در streamlit 📂')

tab1, tab2, tab3 = st.tabs(['فایل csv📊', 'فایل تصویر 🖼️', 'فایل pdf 🗃️'])

# tab1 --> csv

with tab1:
    st.subheader('نمایش و آپلود فایل csv')
    csv_file = st.file_uploader('فایل csv خود را انتخاب کنید', type=['csv'], key='csv')

    if csv_file is not None:
        try:
            df = pd.read_csv(csv_file)
            st.success('فایل با موفقیت بارگزاری شد✅')
            st.dataframe(df)
            st.write('خلاصه آماری 🔍')
            st.write(df.describe())
        except Exception as e:
            st.error(f'خطا در خواندن فایل :❌ {e} ')

# tab2 --> image

with tab2:
    st.subheader('نمایش و آپلود فایل تصویر')
    image_file = st.file_uploader('تصویر را انتخاب کنید', type=['jpg', 'jpeg', 'png'], key='img')

    if image_file is not None:
        try:
            image = Image.open(image_file)
            st.success('تصویر با موفقیت بارگزاری شد✅')
            st.image(image, caption='تصویر آپلود شده', use_container_width=True)


        except Exception as e:
            st.error(f'خطا در خواندن فایل :❌ {e} ')

# tab3 --> pdf
with tab3:
    st.subheader('نمایش و آپلود فایل PDF')
    pdf_file = st.file_uploader('فایل pdf را انتخاب کنید', type=['pdf'], key='pdf')

    if pdf_file is not None:
        try:
            base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
            pdf_display = f"""
                <iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>
            """

            st.success('فایل pdf با موفقیت بارگزاری شد✅')
            st.markdown(pdf_display,unsafe_allow_html=True)
        except Exception as e:
            st.error(f'خطا در خواندن فایل :❌ {e} ')
