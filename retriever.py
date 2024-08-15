
def create_retriever(vector_store):
    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 3}
    )
    return retriever

def merge_docs(docs):
    return "\n\n".join([d.page_content for d in docs])