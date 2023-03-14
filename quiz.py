class Question:
    option_set = set()
    def __init__(self, question, options, answer):
        self.question = question
        for option in options:
            self.option_set.add(option)
        self.answer = answer
        self.option_set.add(answer)
    # no set functions, you want init values finalized and prevent quiz taker from changing answers
    def get_question(self):
        return self.question
    def get_answer(self):
        return self.answer
    def get_options(self):
        return self.option_set
    
    
class Player:
    player_score = 0
    def __init__(self, name):
        self.name = name
        

class Game:
    question_counter = 0
    question_set = list()
    def __init__(self, questions, Player1, Player2):
        for question in questions:
            self.question_set.append(question)
        self.player1 = Player1
        self.player2 = Player2
    def introduction(self):
        print("welcome!")
        print("this quiz will ask 20 question to alternating players, the player with the most right wins!")
        print("GOOD LUCK!!")
    def turn(self, Player):
        current_question = self.question_set[self.question_counter]
        print(f"{Player.name}'s turn!")
        print(f"your question is: {current_question.get_question()}")
        print(f"your options are: \n")
        for option in current_question.get_options():
            print(f"{option}")
        answer = input("enter the answer: ")
        if answer in current_question.get_answer():
            Player.player_score += 1
        self.question_counter += 1
        print(f"{Player.player_score}")
        
questions = list()  
for x in range(21):
    question = input("question to be asked: ")
    option1 = input("possible answer 1: ")
    option2 = input("possible answer 2: ")
    option3 = input("possible answer 3: ")
    answer = input("enter the correct answer:")
    options = [option1, option2, option3]
    questions.append(Question(question, options, answer))

player1 = Player(input("enter player one name: "))
player2 = Player(input("enter player two name: "))


game1 = Game(questions,player1, player2)

while(game1.question_counter < 20):
    game1.turn(player1)
    game1.turn(player2)
if player1.player_score > player2.player_score:
    print(f"{player1.name} wins")
else: print(f"{player2.name} wins")
playagain = input("to play again press 'y' ")
if "y" in playagain:
    game1.question_counter = 0
else: exit