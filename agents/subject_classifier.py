import os
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

llm = GoogleGenerativeAI(model="models/gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)

prompt = PromptTemplate(
    input_variables=["question"],
    template=(
        "Classify the following question into one subject from this list: math, physics, chemistry. "
        "Return exactly one of: 'math', 'physics', 'chemistry', or 'unknown'. "
        "Do not explain or elaborate, just reply with the subject keyword.\n\n"
        "Question: {question}\nSubject:"
    ),
)

chain = LLMChain(llm=llm, prompt=prompt)

def classify_subject(question):
    result = chain.run(question=question)
    return result.strip().lower()
