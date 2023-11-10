import random

# $$$$$ SOLLUTION 1 $$$$$
# class GuessingGame():
#     def __init__(self, answer_number):
#         self.answer_number = answer_number
#         self.solved = False

#     def guess(self, user_guess):
#         if user_guess > self.answer_number:
#             return 'High'
#         elif user_guess < self.answer_number:
#             # print('low')
#             return 'Low'
#         else:
#             self.solved = True
#             return 'Correct'
        
#     def solved(self):
#         return self.solved

# game = GuessingGame(10)
# print(game.guess(1))
# print(game.solved)

# $$$$$ SOLLUTION 2 $$$$$

class GuessingGame():
    def __init__(self, answer_number):
        self.answer_number = answer_number
        self.solved = False

    def guess(self, last_guess):
        if last_guess > self.answer_number:
            return 'High'
        elif last_guess < self.answer_number:
            return 'Low'
        else:
            self.solved = True
            return 'Correct'
        
    def solved(self):
        return self.solved


# ----- main.py -----
game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None

while game.solved == False:
    if last_guess != None: 
        print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
        print("")

    last_guess  = int(input("Enter your guess: ")) 
    last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")