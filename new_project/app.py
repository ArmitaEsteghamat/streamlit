import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# --- پیکربندی اولیه صفحه ---
st.set_page_config(page_title="فرم درخواست همکاری", layout="centered")

st.markdown("""
    <style>
        /* کلیت راست‌چین */
        body, .stApp {
            direction: rtl;
            text-align: right;
            font-family: IRANSans, Tahoma, sans-serif;
        }

        /* فاصله اطراف محتوای اصلی */
        .css-18e3th9 {
            padding: 2rem;
        }

        /* راست‌چین کردن ویجت‌ها */
        .st-dm, .st-bj, .st-af {
            direction: rtl !important;
            text-align: right !important;
        }

        /* فیلدهای ورودی */
        input, select, textarea {
            direction: rtl;
            text-align: right;
        }

        /* رادیو باتن */
        .row-widget.stRadio > div {
            flex-direction: row-reverse;
        }

        /* ---------- اصلاح اسلایدر ---------- */
        /* عنوان اسلایدر */
        .stSlider > label {
            direction: rtl;
            text-align: right;
            display: block;
        }

        /* مقدار عددی در کنار اسلایدر */
        .stSlider > div[data-baseweb="slider"] {
            direction: ltr !important;  /* اجباری: خود اسلایدر باید چپ‌به‌راست بماند */
            text-align: left;
        }

        /* نمایش اعداد روی اسلایدر */
        .stSlider span {
            direction: ltr !important;
            text-align: left !important;
        }

        /* محل قرارگیری مقدار انتخاب‌شده روی اسلایدر */
        .st-c3 {
            direction: ltr !important;
            text-align: left !important;
        }

    </style>
""", unsafe_allow_html=True)


st.title('فرم درخواست همکاری 📰')
st.markdown('''
برای بررسی درخواست همکاری فرم زیر را تکمیل نمایید، پس از تکمیل اطلاعات شما در داشبورد قابل مشاهده می باشد.
''')

st.image("https://cdn.tabnak.ir/files/fa/news/1402/5/10/1680471_663.jpg", caption='همکاری با ما',
         use_container_width=True)

with st.form("application-form"):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input('نام و نام خانوادگی')
        email = st.text_input('ایمیل')
        age = st.slider('سن', 18, 25, 60)

    with col2:
        education = st.selectbox('مدرک تحصیلی', ['دیپلم', 'کاردانی', 'کارشناسی', 'کارشناسی ارشد', 'دکترا'])
        gender = st.radio('جنسیت', ['مرد', 'زن'])
        experience = st.slider('تجربه کاری (سال)', 0, 3, 30)

    skills = st.multiselect('مهارت ها', ['python', 'SQL', 'Streamlit', 'Django', 'ML', 'Html/css', 'Js'])
    cv_file = st.file_uploader('رزومه خود را آپلود کنید(PDF)', type='pdf')
    submitted = st.form_submit_button('ارسال فرم')

if 'applications' not in st.session_state:
    st.session_state.applications = []

if submitted:
    if not (name and email and skills and cv_file):
        st.warning('لطفا همه فیلدها را تکمیل کنید!')
    else:
        new_data = {
            'نام': name,
            'ایمیل': email,
            'سن': age,
            'مدرک': education,
            'جنسیت': gender,
            'تجربه': experience,
            'مهارت ها': ', '.join(skills)
        }

        st.session_state.applications.append(new_data)
        st.success('فرم شما با موفقیت ثبت شد...')

st.markdown('---')
st.header('داشبورد اطلاعات ثبت شده📰')

if len(st.session_state.applications) == 0:
    st.info('هنوز اطلاعاتی ثبت نشده است.')
else:
    df = pd.DataFrame(st.session_state.applications)
    st.dataframe(df)

    st.subheader('توزیع سن متقاضیان')
    fig, ax = plt.subplots()

    ax.hist(df['سن'], bins=5, color='skyblue', edgecolor='black')
    ax.set_xlabel('سن')
    ax.set_ylabel('تعداد')
    st.pyplot(fig)

    st.subheader('تعداد مهارت ها')
    skill_list = ', '.join(df['مهارت ها'].tolist()).split(', ')
    skill_counts = pd.Series(skill_list).value_counts()

    st.bar_chart(skill_counts)
