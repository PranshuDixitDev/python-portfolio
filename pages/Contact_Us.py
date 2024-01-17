import streamlit as st
from send_email import send_email
st.header("Contact Me")

with st.form(key="email_forms"):
	user_email = st.text_input("Your email address: ")
	option = st.selectbox(
		"Which services do you need?",
		("Web development", "Web App", "E-commerce", "Web scrapping"),
		index=None,
		placeholder="Select contact method...",
	)

	st.write('You selected:', option)
	raw_message = st.text_area("Your message here")
	message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic: {option}
{raw_message}
"""
	button = st.form_submit_button("Submit")
	if button:
		print("button pressed")
		send_email(message)
		st.info("Your email was sent successfully,\n We will get back to you ")


