# This file will be used to define the model for the application.

import random
import json
import os
from typing import List, Optional

class Agent:
    def __init__(self, q_table="q_table.json", epsilon=0.2, alpha=0.1, gamma=0.9):
        self.q_table = q_table
        self.epsilon = epsilon # How often to pick a random action
        self.alpha = alpha # Learning rate
        self.gamma = gamma # How important the future reward is

        def load_q_table(self):
            if os.path.exists(self.q_table):
                with open(self.q_table, "r") as f:
                    return json.load(f)
            else:
                return {}
            
        def save_q_table(self):
            with open(self.q_table, "w") as f:
                json.dump(q_table, f)