import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of mangoes")

col1, col2 = st.columns(2)
with col1:
  st.subheader("mongoes")
  st.image("WhatsApp Image 2024-01-06 at 3.28.35 PM.jpeg", caption="mangoes", width=300,use_column_width=True)
  st.write("mangoes")
with col2:
  st.subheader("mango")
  st.image("WhatsApp Image 2024-01-06 at 3.28.36 PM.jpeg", caption="mango", width=300,use_column_width=True)
  st.write("Rawmango")
