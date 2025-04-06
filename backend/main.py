from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel
from model import Agent

agent = Agent()


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
    board = data.board.copy()
    position = data.position
    player = data.player # current player


    if data.player != computer_move:
        if position is not None and board[position] is None:
            board[position] = player
            next_state = board.copy()
            agent.update_q_table(data.board, position, -0.1, next_state)  # Update Q-table with no immediate reward
            player = "X" if player == "O" else "O"
        else:
            print("Invalid move. Position already occupied or out of bounds.")
    else: 
        agent_move = agent.choose_action(board)
        board[agent_move] = player
        player = "X" if player == "O" else "O"
        reward = 0
        agent.update_q_table(data.board, agent_move, reward, board)
        agent.save_q_table()
        

    winner = check_winner(board)
    if winner:
        reward = 1 if winner == computer_move else -1
    else:
        reward = 0.1 if data.player == computer_move else -0.1  # Encourage good moves, discourage bad ones
    agent.update_q_table(data.board, position, reward, board)
    agent.save_q_table()

    return {
        "receivedData": data.dict(),
        "message": "Move command received",
        "board": board,
        "player": player,
        "winner": winner,
    }


def check_winner(board: List[Optional[str]]) -> Optional[str]:
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] is not None and board[combo[0]] == board[combo[1]] == board[combo[2]]:
            return board[combo[0]]
        
    if all(cell is not None for cell in board):
        return "Draw"
    
    return None