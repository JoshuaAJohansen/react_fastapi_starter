from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from typing import List, Optional

from  model import Item

def create_application() -> FastAPI:
    app = FastAPI()

    origins = [
        # This is the frontend port - 3000
        "http://localhost:3000",
        "localhost:3000"
    ]

    # Allow communication between backend and frontend
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    # Array used as Database
    items = [
        { "id": 1, "name": "First item", "description": "Here is a description"},
        { "id": 2, "name": "Another item", "description": "Slow is smooth. Smooth is fast"},
    ]

    @app.get("/")
    async def main():
        print('hello')
        return {"message": "Hello World"}

    # localhost:3000/items
    @app.get("/items/", response_model=List[Item])
    async def get_items():
        return items

    return app


app = create_application()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)