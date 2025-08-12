import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title='نمودار با matplotlib',layout='centered')

st.title('نمودار با استفاده از matplotlib📊')

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig , ax = plt.subplots()
ax.plot(x, y , color='green',label='sin(x)')
ax.set_title('نمودار سینوسی')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

st.pyplot(fig)