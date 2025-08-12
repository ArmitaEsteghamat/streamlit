import streamlit as st

st.title("📡 فرم واکنش‌گرا با نمایش لحظه‌ای")

# فیلد عددی برای قیمت
price = st.slider("قیمت واحد (تومان)", 1000, 100000, 10000, step=1000)

# فیلد عددی برای تعداد
quantity = st.number_input("تعداد:", min_value=1, value=1)

# محاسبه لحظه‌ای کل
total = price * quantity
st.success(f"💰 مبلغ نهایی: {total:,} تومان")
