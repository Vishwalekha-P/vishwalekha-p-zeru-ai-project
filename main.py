from fastapi import FastAPI, Request
from chatbot import get_bot_response

app = FastAPI()

@app.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    user_input = data["message"]
    reply = get_bot_response(user_input)
    return {"reply": reply}