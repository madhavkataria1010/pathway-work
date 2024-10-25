import pathway as pw
import fitz  
from sentence_transformers import SentenceTransformer
from google.generativeai import configure, GenerativeModel

with open('api.txt', 'r') as file:
    api_key = file.read().strip()
configure(api_key=api_key)

def parse_pdf_to_text_chunks(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.split("\n\n")  

pdf_path = "alphabet.pdf"
passages = parse_pdf_to_text_chunks(pdf_path)

embedding_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
embedded_passages = [(passage, embedding_model.encode(passage)) for passage in passages]

passage_table = pw.Table.from_records(embedded_passages, schema=['passage', 'embedding'])

def retrieve_relevant_context(user_query, top_k=5):
    query_embedding = embedding_model.encode(user_query)
    passage_table = passage_table.with_column('similarity', pw.cosine_similarity(query_embedding, passage_table.embedding))
    relevant_passages = passage_table.sort(descending=['similarity']).take(top_k).passage.collect()
    return relevant_passages

def generate_answer_with_gemini(user_query):
    relevant_context = retrieve_relevant_context(user_query)
    prompt = f"Question: {user_query}\nContext: {' '.join(relevant_context)}"
    gemini_model = GenerativeModel('gemini-1.5-flash')
    response = gemini_model.generate_content(prompt)
    return response.text

user_question = input("Enter your question: ")
answer = generate_answer_with_gemini(user_question)
print("Answer:", answer)