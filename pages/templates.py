import streamlit as st

def templates():
    st.title("Prompt Templates")

    with st.expander("AI Prompt Template"):
        st.write("### AI Prompt Template")
        st.write("This is a sample AI prompt template.")
    with st.expander("Data Science Prompt Template"):
        st.write("### Data Science Prompt Template")
        st.write("This is a sample Data Science prompt template.")
    with st.expander("Web Development Prompt Template"):
        st.write("### Web Development Prompt Template")
        st.write("This is a sample Web Development prompt template.")
    with st.expander("Machine Learning Prompt Template"):
        st.write("### Machine Learning Prompt Template")
        st.write("This is a sample Machine Learning prompt template.")
