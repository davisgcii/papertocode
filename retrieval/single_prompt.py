# %%
import openai
import os
from langchain import OpenAI

from parse import split_sections

from langchain.chains import LLMChain, MapReduceChain
from langchain import PromptTemplate
from langchain import *
from langchain.text_splitter import RecursiveCharacterTextSplitter


# %%
prompt_template = """

Given the LaTeX source of a machine learning paper from Arxiv and some existing code, please generate a Jupyter notebook that implements and replicates the results from the paper EXACTLY WITH NO ERRORS. Start from the provided code and modify it as necessary to incorporate the new ideas from the paper. The notebook should be organized in a logical and coherent way, with sections and sub-sections that reflect the paper's organization. Assume that the notebook will be used by someone who is familiar with the general field of AI, but may not be familiar with the specific topic of the paper. Please include code, explanations, and visualizations where appropriate. The notebook should be written in Python using the PyTorch machine learning framework and should be easy to run on a Jupyter server.

######################
LaTeX Source for paper
######################
    {paper}

######################
Previous Code
######################

    {code}

######################
Your Code Here
######################
"""

def generate_code(paper_str: str):

    llm = OpenAI()
    code = "import torch"

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["paper", "code"]
    )

    chain = LLMChain(llm=llm, prompt=PROMPT)
    # chain = MapReduceChain.from_params(llm=llm, prompt=PROMPT, text_splitter=RecursiveCharacterTextSplitter())

    return chain.apply([{"paper": paper_str, "code": code}])
