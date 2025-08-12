import streamlit as st
st.set_page_config(page_title="اپلیکیشن چندصفحه‌ای", layout="centered")

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


st.sidebar.title("صفحات 📂")
page = st.sidebar.selectbox('انتخاب صفحه:',['خانه','فرم ثبت نام','آمار فروش'])

if page == 'خانه':
    st.header('خوش آمدید🏡')
    st.write('این صفحه اصلی اپ می باشد.')

elif page=='فرم ثبت نام':
    st.header('فرم ثبت نام ✅')
    name = st.text_input("نام:")
    email = st.text_input("ایمیل:")
    if st.button('ارسال'):
        st.success('اطلاعات شما ثبت شد')

elif page=="آمار فروش":
    st.header('آمار فروش 📊')
    st.write('در این نمودار آمار فروش مشاهده میشود')