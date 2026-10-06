from fastapi import FastAPI
from pydantic import BaseModel
import ollama
app=FastAPI(title="AI Assistant API")
class Question(BaseModel):
    question:str
class TextInput(BaseModel):
    text:str
@app.post("/ask")
def ask(data:Question):
    try:
        response=ollama.chat(model="llama3.2",messages=[{"role":"user","content":data.question}])
        return {"answer":response["message"]["content"]}
    except Exception as e:
        return {"error":str(e)}

@app.post("/summarize")
def summarize(data:TextInput):
    try:
        prompt=f"Summarize the following text concisely:\n{data.text}"
        response=ollama.chat(model="llama3.2",messages=[{"role":"user","content":prompt}])
        return {"summary":response["message"]["content"]}
    except Exception as e:
        return {"error":str(e)}

@app.post("/classify")
def classify(data:TextInput):
    try:
        prompt=f"Classify the following text as Positive, Negative or Neutral. Return only the category.\n{data.text}"
        response=ollama.chat(model="llama3.2",messages=[{"role":"user","content":prompt}])
        return {"classification":response["message"]["content"]}
    except Exception as e:
        return {"error":str(e)}

@app.post("/extract")
def extract(data:TextInput):
    try:
        prompt=f"""Extract the important information from the following text and return JSON with these fields:
name, skills, experience, education, projects

Text:
{data.text}"""
        response=ollama.chat(model="llama3.2",messages=[{"role":"user","content":prompt}])
        return {"extracted_data":response["message"]["content"]}
    except Exception as e:
        return {"error":str(e)}