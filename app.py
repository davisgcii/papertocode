import streamlit as st
from io import StringIO
import os
import time

from retrieval.single_prompt import generate_code, summarize_paper


st.title("Papers Without Code")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    col1, col2 = st.columns(2)
    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    # col1.header(len(string_data))

    with st.expander("Show LaTeX"):
        st.header("Paper Contents")
        st.code(rf"""{string_data} """, language="latex")


    summary = summarize_paper(string_data, model_name=os.environ["OPENAI_MODEL_NAME"])
    with st.expander("Paper Summary"):
        st.header("Summary")
        # print(summary)
        st.write(summary)


    bar = st.progress(0, "Generating Code")
    code = "import torch"
    for complete in range(5):
        code += generate_code(summary, code=code, model_name=os.environ["OPENAI_MODEL_NAME"])
        time.sleep(1)
        bar.progress((complete + 1) * 20)
        
    with st.expander("Show Generated Code"):
        st.header("Generated Code")
        st.code(code)