
import streamlit as st
from send_email import send_email

#st.set_page_config(layout="wide")
st.header("Contact Me")

with st.form(key='email_forms'):
    user_email= st.text_input("Your email address")
    message = st.text_area("Your message")
    message ='Subject: Portfolio Website Contact Me Page'+'\n'+message+'\n'+'My email is : '+user_email
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully!")