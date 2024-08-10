import streamlit as st
from pages.home import home
from pages.templates import templates

# Set up the navigation
pages = {
    "Simulator": [st.Page(home, title="Home")],
    "Templates": [st.Page(templates, title="Prompt Templates")]
}

# Set the page configuration
st.set_page_config(layout="wide", page_title="SparkPrompt", page_icon=":robot_face:")

# Load custom CSS for styling
with open("style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

# Run the navigation
pg = st.navigation(pages)
pg.run()