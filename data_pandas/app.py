import streamlit as st
import pandas as pd

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

# عنوان صفحه
st.title("📊 پردازش داده‌ها با Pandas در Streamlit")

# آپلود فایل CSV
uploaded_file = st.file_uploader("فایل فروش خود را آپلود کنید", type=["csv"])

if uploaded_file is not None:
    # خواندن فایل CSV با Pandas
    df = pd.read_csv(uploaded_file)

    # نمایش داده‌ها
    st.subheader("🔍 نمایش اولیه داده‌ها")
    st.dataframe(df)

    # -------------------------
    # پردازش‌های متداول با Pandas
    # -------------------------

    st.subheader("📌 آمار کلی فروش")

    # محاسبه مجموع فروش
    total_sales = df["کل_فروش"].sum()
    total_quantity = df["تعداد"].sum()

    col1, col2 = st.columns(2)
    col1.metric('مجموع فروش', f'{total_sales:,.0f} تومان')
    col2.metric('تعداد کل اقلام فروخته شده', total_quantity)

    # فیلتر بر اساس نام محصول
    st.subheader("🔎 فیلتر بر اساس محصول")
    products = df['محصول'].unique()
    selected_product = st.selectbox('محصول مورد نظر را انتخاب کنید',products)

    filtered = df[df['محصول']==selected_product]
    st.write(f'اطلاعات فروش مربوط به محصول ©️:{selected_product}')
    st.dataframe(filtered)


    # گروه‌بندی بر اساس تاریخ
    st.subheader("📅 فروش روزانه محصول انتخاب‌ شده")
    df['تاریخ'] = pd.to_datetime(filtered['تاریخ'])
    daily = filtered.groupby('تاریخ')['کل_فروش'].sum().reset_index()

    st.write('جدول فروش روزانه :')
    st.dataframe(daily)

    st.line_chart(daily.rename(columns={'تاریخ':'index'}).set_index('index'))

    # مرتب‌سازی و استخراج بیشترین فروش‌ها
    st.subheader("🏆 ۵ فروش برتر (بر اساس مبلغ)")
    top5 = df.sort_values('کل_فروش',ascending=False).head(5)
    st.dataframe(top5)

else:
    st.info("📤 لطفاً یک فایل CSV آپلود کنید تا داده‌ها پردازش شوند.")
