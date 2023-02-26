import streamlit as st
from io import StringIO


st.title("Papers with Code")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    col1, col2 = st.columns(2)
    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    col1.header(len(string_data))

    col1.header("Paper Contents")
    col1.latex(rf"""{string_data} """)

    col2.header("Generated Code")
