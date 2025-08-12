import streamlit as st
import sqlite3
import pandas as pd


def create_table():
    conn = sqlite3.connect("people.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS people (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER,
                    email TEXT UNIQUE
                )''')
    conn.commit()
    conn.close()


def add_person(name, age, email):
    conn = sqlite3.connect('people.db')
    c = conn.cursor()
    c.execute("INSERT INTO people (name,age,email) VALUES (? , ? ,?)", (name, age, email))
    conn.commit()
    conn.close()


def get_people():
    conn = sqlite3.connect('people.db')
    df = pd.read_sql_query("SELECT * FROM people", conn)
    conn.close()
    return df


def delete_person(email):
    conn = sqlite3.connect('people.db')
    c = conn.cursor()
    c.execute("DELETE FROM people WHERE email = ?", (email,))
    conn.commit()
    conn.close()


st.set_page_config(page_title="مدیریت لیست افراد", layout="centered")
st.title("📋 اپلیکیشن مدیریت اطلاعات افراد (SQLite)")

create_table()
# --- فرم افزودن فرد جدید ---
st.subheader("➕ افزودن فرد جدید")

with st.form(key="add_form"):
    name = st.text_input('نام و نام خانوادگی')
    age = st.number_input('سن', min_value=0, max_value=100, step=1)
    email = st.text_input('ایمیل')
    submitted = st.form_submit_button('افزودن')

    if submitted:
        try:
            add_person(name, age, email)
            st.success(f'فرد با موفقیت اضافه شد {name}')
        except Exception as e:
            st.error(f'خطا در افزودن{e}')

st.subheader('لیست افراد:')
people_df = get_people()
st.dataframe(people_df)

st.subheader('حذف فرد!')
email_to_delete = st.selectbox('ایمیل فرد مورد نظر', people_df['email'] if not people_df.empty else [""])

if st.button('حذف'):
    delete_person(email_to_delete)
    st.success(f'فرد با ایمیل {email_to_delete} حذف شد')
    # st.experimental_dialog()
