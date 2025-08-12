import streamlit as st

st.title('به سایت من خوش آمدید')

st.header('عنوان فرعی')
st.subheader('زیرعنوان')

st.markdown('# این یک عنوان markdown می باشد')
st.markdown('این یک متن **Bold** و *Italic* است')

st.write('این اولین اپلیکیشن ما می باشد.')

st.image('assets/images/webapp.jpg', width=500, caption='تست', use_container_width=True)

st.video('assets/videos/cool.mp4')
st.video('https://www.aparat.com/v/yavr49k')

# name = st.text_input('نام خود را وارد کنید :')
#
# if name:
#     st.success(f', سلام {name}')


st.audio('assets/audio/01 - Ba Tou.mp3')

name = st.text_input('نام خود را وارد کنید :')

if name:
    st.write(f', سلام {name}')

agree = st.checkbox("با شرایط موافق هستم")

if agree:
    st.write("شما قوانین را پذیرفتید")

if st.button("کلیک کن!"):
    st.write("دکمه کلیک شد")

age = st.slider("سن خود را انتخاب کنید", 18, 100)
st.write(f'سن شما : {age}')

option = st.selectbox("انتخاب کنید" , ["python" , "django" ,"streamlit"])
st.write(f'گزینه انتخابی : {option}')
