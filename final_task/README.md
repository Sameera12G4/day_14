# AI Assistant API

A basic LLM-powered AI Assistant API built using Python, FastAPI and Ollama.

## Technologies

- Python
- FastAPI
- Uvicorn
- Ollama
- Llama 3.2

## Features

- Ask questions
- Summarize text
- Classify text sentiment
- Extract information from text

## Endpoints

### POST /ask

Accepts a question and returns an AI-generated answer.

### POST /summarize

Accepts text and generates a summary.

### POST /classify

Classifies text as Positive, Negative or Neutral.

### POST /extract

Extracts structured information from text.

## Run

```bash
uvicorn main:app --reload