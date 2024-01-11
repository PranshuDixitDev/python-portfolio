import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
	st.image("images/my-pic.png")

with col2:
	st.title("Pranshu Dixit")
	content = """Hello I am Pranshu Dixit! I am a Python programmer, old school gamer,I graduated in 2017 ,
	I had my own business of crypto mining rigs , I know web scraping and we development,
	I have worked a both product base and client base company
	"""
	st.write(content)
