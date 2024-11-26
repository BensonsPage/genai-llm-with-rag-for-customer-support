import chromadb
from generateembeddings import GeminiEmbeddingFunction

# Read documents from company's customer support documents
DOCUMENT1 = (open('documents/banking-question-and-answers-generated-with-gemini-0.txt', 'r', encoding="utf-8")).read()
DOCUMENT2 = (open('documents/banking-question-and-answers-generated-with-gemini-1.txt', 'r', encoding="utf-8")).read()

documents = [DOCUMENT1, DOCUMENT2]
# Create the vector database.
DB_NAME = "llm_customer_support_rag_vector_db"
embed_fn = GeminiEmbeddingFunction()
embed_fn.document_mode = True

chroma_client = chromadb.Client()
db = chroma_client.get_or_create_collection(name=DB_NAME, embedding_function=embed_fn)

db.add(documents=documents, ids=[str(i) for i in range(len(documents))])

# Validate documents have been appended in the database.
print (db.count())