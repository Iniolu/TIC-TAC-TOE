import {useState, useEffect } from 'react';
import './App.css';

let computerFirstMove = null;


function LetComputerFirstMove({squares, setSquares, currentPlayer, setCurrentPlayer}) {
  const [isDisabled, setIsDisabled] = useState(false);

  useEffect(() => {
    if (squares.some((square) => square === "X" || square === "O")) {
      setIsDisabled(true);
    }
  }, [squares]);

  async function handleClick(){
    computerFirstMove = true;
    setIsDisabled(true);

    try{
      const response = await fetch('http://localhost:8000/move', {
        method: 'POST',
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          board: squares,
          player: currentPlayer,
          position: null,
          computerFirstMove: computerFirstMove,
        })
      });

      if (!response.ok){
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      setSquares(data.board);
      setCurrentPlayer(data.player);

    }catch (error) {
      console.error('Error:', error);
    }

  }
  return(
    <button className='computer-first-move' onClick={handleClick} disabled={isDisabled}>
      Let Computer Make the First Move
      </button>
  )
}

function Square({value, onSquareClick}) {
  return(
    <button className="square" onClick={onSquareClick}>{value}</button>
  )
}

function Winner({winner}) {
  return(
    <p className="winner">{winner} WINS</p>
  )
}


function TicTacToeBoard({squares, setSquares, currentPlayer, setCurrentPlayer, setWinner}) {  
  async function handleClick(i){
    if (squares[i] !== null) return;

    try{
      const response = await fetch('http://localhost:8000/move',  {
        method: 'POST',
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          board: squares,
          player: currentPlayer,
          position: i,
          computerFirstMove: computerFirstMove,
        })
      });

      if (!response.ok){
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      setSquares(data.board);
      setCurrentPlayer(data.player)
      setWinner(data.winner);

      if (data.winner) return;

      const agentResponse = await fetch('http://localhost:8000/move', {
        method: 'POST',
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          board: data.board,
          player: data.player,
          position: null,
          computerFirstMove: computerFirstMove,
        })
      });

      if (!agentResponse.ok){
        throw new Error('Network response was not ok');
      }
      const agentData = await agentResponse.json();
      setSquares(agentData.board);
      setCurrentPlayer(agentData.player);
      setWinner(agentData.winner);


    }catch (error) {
      console.error('Error:', error);
    }

    

  }
  

  return(
    <>
    <div className="board-row">
    <Square value={squares[0]} onSquareClick={() => handleClick(0)}/>
    <Square value={squares[1]} onSquareClick={() => handleClick(1)}/>
    <Square value={squares[2]} onSquareClick={() => handleClick(2)}/>
    </div>
    <div className="board-row">
    <Square value={squares[3]} onSquareClick={() => handleClick(3)}/>
    <Square value={squares[4]} onSquareClick={() => handleClick(4)}/>
    <Square value={squares[5]} onSquareClick={() => handleClick(5)}/>
    </div>
    <div className="board-row">
    <Square value={squares[6]} onSquareClick={() => handleClick(6)}/>
    <Square value={squares[7]} onSquareClick={() => handleClick(7)}/>
    <Square value={squares[8]} onSquareClick={() => handleClick(8)}/>
    </div>
    </>
  )
}




export default function App() {
  const [squares, setSquares] = useState(Array(9).fill(null)); // Track state of squares
  const [currentPlayer, setCurrentPlayer] = useState("X"); // Track whose turn it is
  const [winner, setWinner] = useState(null); // Track winner
  return (
    <div className="App"> 
      <TicTacToeBoard
        squares={squares}
        setSquares={setSquares}
        currentPlayer={currentPlayer}
        setCurrentPlayer={setCurrentPlayer}
        setWinner={setWinner}/>
      <LetComputerFirstMove 
        squares={squares}
        setSquares={setSquares}
        currentPlayer={currentPlayer}
        setCurrentPlayer={setCurrentPlayer}/>
      <Winner 
      winner={winner}/>
    </div>
  );
}
