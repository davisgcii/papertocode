from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import VectorDBQA
from langchain.document_loaders import TextLoader
from langchain.document_loaders import OnlinePDFLoader

def get_context(arxiv_link: str, prompt: str) -> str:

    # Load the document
    loader = OnlinePDFLoader(arxiv_link)
    doc = loader.load()

    # Split the document into sentences
    splitter = RecursiveCharacterTextSplitter()
    sentences = splitter.split(doc)

    # Embed the sentences
    embeddings = OpenAIEmbeddings()
    embedded_sentences = embeddings.embed(sentences)

    # Create a vector store
    store = Chroma()

    # Create a language model
    lm = OpenAI()

    # Create a QA chain
    chain = VectorDBQA(store, lm)

    # Add the embedded sentences to the vector store
    for sentence, embedding in zip(sentences, embedded_sentences):
        store.add(sentence, embedding)

    # Ask the QA chain a question
    return chain.ask(prompt)

