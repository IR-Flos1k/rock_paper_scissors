import os
import random
import google.generativeai as genai
from dotenv import load_dotenv

#import API
load_dotenv()
key = os.getenv("KEY")
if not key:
    print("Немає API ключа!")
genai.configure(api_key=key)
class AIBot:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        self.history = []
        self.valid_moves = ["rock", "paper", "scissors"]

    def predict_move(self):
        if len(self.history) < 3:
            return random.choice(self.valid_moves)
        recent_history = self.history[-10:]
        
        prompt = f"""
        Ти граєш у гру Камінь-Ножиці-Папір проти людини. 
        Ось історія її останніх ходів (від старіших до найновіших): {recent_history}.
        Проаналізуй психологію та патерни людини, передбач її НАСТУПНИЙ хід і обери жест, 
        який ПЕРЕМОЖЕ її (Камінь б'є Ножиці, Ножиці б'ють Папір, Папір б'є Камінь).
        
        Твоя відповідь має містити ТІЛЬКИ ОДНЕ СЛОВО з даного переліку: {self.valid_moves}.
        Жодних інших символів, пояснень чи крапок.
        """
        try:
            response = self.model.generate_content(prompt)
            
            bot_move = response.text.strip().lower()

            if bot_move in self.valid_moves:
                return bot_move
            else:
                print(f"Error in bot's answer. Return random choice")
                return random.choice(self.valid_moves)
                
        except Exception as e:
            print(f"Error: no connection with internet|AI {e}. Return random choice")
            return random.choice(self.valid_moves)

    def update_memory(self, player_move):
        self.history.append(player_move)
        