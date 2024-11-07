import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Deepak Pawal")
    content="""
    Hi Deepak Pawal! You are a Python developer, actively involved 
    in helping clients with various issues and continuously learning
    about the functionalities of your company's product, Voyager.
    Your work likely involves troubleshooting, problem-solving, and
    possibly even contributing to improving the product,making you 
    a key resource for both technical support and development.
    """
    st.info(content)

content2="""
Below are some of the apps I have created. Feel free to contact me!
"""
st.write(content2)

col3,empty_col,col4 = st.columns([1.5,0.5,1.5])

df=pd.read_csv('data.csv',sep=';')


with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")