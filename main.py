from fastapi import FastAPI

import uvicorn 
from src.routes.chat_route import router as chat_route

app = FastAPI()

app.include_router(chat_route)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)