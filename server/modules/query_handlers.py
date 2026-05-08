def query_chain(chain, question):
    retriever = chain["retriever"]
    llm = chain["llm"]

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs if doc.page_content
    )

    print("CONTEXT SENT TO LLM:", context[:1000])

    prompt = f"""
You are a helpful medical assistant. Answer the user's question using only the context below.

If the answer is not in the context, say:
"I don't know based on the uploaded documents."

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }