import streamlit as st

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

st.title("🔁 شمارنده با استفاده از session_state")

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button('افزایش'):
    st.session_state.counter += 1

if st.button('کاهش'):
    st.session_state.counter -= 1

st.info(f'مقدار فعلی شمارنده:{st.session_state.counter}')
