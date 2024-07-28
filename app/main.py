from fastapi import FastAPI, HTTPException
import google.generativeai as genai

app = FastAPI()

GEMINI_API_KEY = ""
MODEL_NAME = "gemini-1.5-pro-001"

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(MODEL_NAME)

@app.get("/")
async def root():
    return {"message": "Welcome!"}

@app.get("/gemini")
async def gemini(query: str):
    try:
        print(query)
        response = model.generate_content(query)
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))