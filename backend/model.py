# This file will be used to define the model for the application.

import random
import json
import os
from typing import List, Optional

class Agent:
    def __init__(self, q_table="q_table.json", epsilon=0.9, alpha=0.2, gamma=0.9):
        self.q_table = self.load_q_table(q_table)
        self.epsilon = epsilon # How often to pick a random action
        self.alpha = alpha # Learning rate
        self.gamma = gamma # How important the future reward is
        self.q_table_file = q_table

    def load_q_table(self, q_table_file):
        if os.path.exists(q_table_file):
            with open(q_table_file, "r") as f:
                return json.load(f)
        else:
            return {}
        
    def save_q_table(self):
        with open(self.q_table_file, "w") as f:
            json.dump(self.q_table, f)

    def get_state(self, board: List[Optional[str]]) -> str:
        # Convert the board to a string representation (e.g. X--OXO--)
        return "".join([cell if cell is not None else "-" for cell in board])
    
    def choose_action(self, board: List[Optional[str]]) -> int:
        state = self.get_state(board)
        possible_actions = []
        for i in range(len(board)):  #Get all possible actions by checking for None values in the board
            if board[i] is None:
                possible_actions.append(i)
        
        
        if random.random() < self.epsilon:  # We pick a random action with probability epsilon
            return random.choice(possible_actions)
        else:
            q_values = self.q_table.get(state, {})
            if not q_values:  # If there are no Q-values for this state, pick a random action
                return random.choice(possible_actions)
            return max(possible_actions, key=lambda x: q_values.get(x, 0))  # Pick the action with the highest Q-value
    
    def update_q_table(self, state: str, action: int, reward: float, next_state: str):
        state = self.get_state(state)
        next_state = self.get_state(next_state)

        if state not in self.q_table:
            self.q_table[state] = {}
        if action not in self.q_table[state]:
            self.q_table[state][action] = 0

        next_max = max(self.q_table.get(next_state, {}).values(), default=0) # Get the max Q-value for the next state

        # Update the Q-value using the Q-learning formula
        self.q_table[state][action] += self.alpha * (reward + self.gamma * next_max - self.q_table[state][action])

    
    def reset(self):
        self.q_table = {}
        self.save_q_table()



