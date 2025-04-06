from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel


app = FastAPI()

origins = [
    "http://localhost:3000", 
    "http://localhost", 
    "https://your-react-app-domain.com", 
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MoveRequest(BaseModel):
    board: List[Optional[str]]
    player: str
    position: Optional[int] = None
    computerFirstMove: Optional[bool] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/move")
async def move(data: MoveRequest):
    computer_move = "X" if data.computerFirstMove else "O"
    
    if data.player != computer_move:
        board = data.board.copy()
        position = data.position
        player = data.player
        if position is not None and board[position] is None:
            board[position] = player
            player = "X" if player == "O" else "O"
        else:
            print("Invalid move. Position already occupied or out of bounds.")
    else: 
        print("Its the computer's turn.")


    print("Received data from frontend:", data.dict())

    return {
        "receivedData": data.dict(),
        "message": "Move command received",
        "board": board,
        "player": player
    }