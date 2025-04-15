# TIC-TAC-TOE
This project aims to enhance my machine learning skills by applying reinforcement learning to a simple Tic Tac Toe game, where the AI learns and improves through interactions with a human player.

## Features

- **Reinforcement Learning AI**: The AI uses Q-learning to adapt and improve its strategy over time.
- **Interactive Gameplay**: Play against the AI in a classic Tic Tac Toe game.
- **Customizable First Move**: Option to let the computer make the first move.
- **Frontend and Backend**: Built with React for the frontend and FastAPI for the backend.

## Project Structure

TIC-TAC-TOE/ ├── backend/ # Backend API and reinforcement learning logic │ ├── main.py # FastAPI server and game logic │ ├── model.py # Q-learning agent implementation │ ├── q_table.json # Q-table for storing AI's learned states │ ├── requirements.txt # Backend dependencies │ ├── Dockerfile # Dockerfile for backend │ └── .dockerignore # Docker ignore file for backend ├── frontend/ # React-based frontend │ ├── src/ # Source code for the React app │ ├── public/ # Public assets │ ├── Dockerfile # Dockerfile for frontend │ ├── .dockerignore # Docker ignore file for frontend │ └── package.json # Frontend dependencies ├── docker-compose.yml # Docker Compose configuration └── README.md # Project documentation

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your system.

### Running the Project

1. Clone the repository:
    ```
    git clone https://github.com/your-username/TIC-TAC-TOE.git
    cd TIC-TAC-TOE
    ```
2. Start the application using Docker Compose:
    ```
    docker-compose up
    ```
3. Access the frontend at http://localhost:3000
4. The backend API is available at http://localhost:8000

### How It Works
- The backend uses a Q-learning agent to make decisions. The agent's state-action values are stored in q_table.json.
- The frontend communicates with the backend to send moves and receive the updated game state.
- The AI learns from each game by updating its Q-table based on rewards and penalties.

### Technology Used
- Frontend: React
- Backend: FastAPI
- Reinforcement Learning: Q-learning
- Docker: For containerization

### Future Improvements
- Add a user interface to visualize the AI's learning process.
- Implement additional difficulty levels for the AI.
- Allow saving and loading different Q-tables for training.
- Improve on Q-Learning model, update how rewards are given to the Agent.