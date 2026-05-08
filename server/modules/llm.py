from langchain_groq import ChatGroq
import os


def get_llm_chain(retriever):
    llm = ChatGroq(
        groq_api_key=os.environ["GROQ_API_KEY"],
        model_name="llama-3.3-70b-versatile",
        temperature=0.3
    )

    return {
        "llm": llm,
        "retriever": retriever
    }