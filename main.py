import streamlit as st
import pandas

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
	st.info(content)

content2 = """Below you can find the apps I have built in Python. Feel free to contact me!"""
st.write(content2)

col3, empty_col,col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
	for index, row in df[:10].iterrows():
		st.header(row["title"])
		st.write(row["description"])
		st.image("images/" + row["image"])
		# st.write(f"[Source Code]({row['url']})")

with col4:
	for index, row in df[10:].iterrows():
		st.header(row["title"])
		st.write(row["description"])
		st.image("images/" + row["image"])
		# st.write(f"[Source Code]({row['url']})")
