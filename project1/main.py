import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

st.set_page_config(page_title="فرم استخدام", layout="centered")


# --- تنظیمات راست‌چین (RTL) ---
st.markdown(
    """
    <style>
    body {
        direction: rtl;
        text-align: right;
    }

    /* برچسب‌های ورودی */
    .stTextInput label, .stSelectbox label, .stSlider label, 
    .stRadio label, .stFileUploader label, .stMultiselect label {
        text-align: right !important;
        display: block;
    }

    /* چرخاندن خود اسلایدر */
    .stSlider > div[data-baseweb="slider"] {
        direction: ltr !important; /* برای عملکرد درست */

    }

    /* چرخاندن مقدار نمایش داده‌شده اسلایدر به حالت صحیح */
    .stSlider .css-1emrehy {
        transform: scaleX(-1);
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --- عنوان و توضیح ---
st.title("📝 فرم درخواست همکاری")
st.markdown("""
برای بررسی درخواست همکاری خود، لطفاً فرم زیر را تکمیل نمایید. پس از ارسال، اطلاعات در داشبورد قابل مشاهده خواهد بود.
""")

# --- تصویر معرفی ---
st.image("https://cdn.tabnak.ir/files/fa/news/1402/5/10/1680471_663.jpg", caption="همکاری با ما", use_container_width=True)

# --- فرم ثبت اطلاعات ---
with st.form("application_form"):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("نام و نام خانوادگی")
        email = st.text_input("ایمیل")
        age = st.slider("سن", 18, 60, 25)

    with col2:
        education = st.selectbox("مدرک تحصیلی", ["دیپلم", "کاردانی", "کارشناسی", "کارشناسی ارشد", "دکترا"])
        gender = st.radio("جنسیت", ["مرد", "زن", "سایر"])
        experience = st.slider("تجربه کاری (سال)", 0, 30, 3)

    skills = st.multiselect("مهارت‌ها", ["Python", "SQL", "Streamlit", "Pandas", "HTML/CSS", "Machine Learning"])

    cv_file = st.file_uploader("رزومه خود را آپلود کنید (PDF)", type="pdf")

    submitted = st.form_submit_button("ارسال فرم")

# --- ذخیره داده‌ها در حافظه موقت (Session State) ---
if 'applicants' not in st.session_state:
    st.session_state.applicants = []

if submitted:
    if not (name and email and skills and cv_file):
        st.warning("لطفاً همه فیلدهای ضروری را پر کنید.")
    else:
        new_data = {
            "نام": name,
            "ایمیل": email,
            "سن": age,
            "مدرک": education,
            "جنسیت": gender,
            "تجربه": experience,
            "مهارت‌ها": ", ".join(skills)
        }
        st.session_state.applicants.append(new_data)
        st.success("فرم با موفقیت ثبت شد ✅")

# --- داشبورد تحلیلی ---
st.markdown("---")
st.header("📊 داشبورد اطلاعات ثبت‌شده")

if len(st.session_state.applicants) == 0:
    st.info("هنوز اطلاعاتی ثبت نشده است.")
else:
    df = pd.DataFrame(st.session_state.applicants)

    st.dataframe(df)

    # --- نمودار توزیع سن ---
    st.subheader("توزیع سنی متقاضیان")
    fig, ax = plt.subplots()
    ax.hist(df["سن"], bins=5, color="skyblue", edgecolor="black")
    ax.set_xlabel("سن")
    ax.set_ylabel("تعداد")
    st.pyplot(fig)

    # --- تعداد مهارت‌ها ---
    st.subheader("تعداد مهارت‌ها")
    skill_list = ", ".join(df["مهارت‌ها"].tolist()).split(", ")
    skill_counts = pd.Series(skill_list).value_counts()

    st.bar_chart(skill_counts)

