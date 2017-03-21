# IPND Stage 2 Final Project

# A list of replacement words to be passed in to the play game function.
blanks  = ["___1___", "___2___" , "___3___", "___4___"]


# The following are quizes to madlib function. easy:quiz1    medium:quiz2        hard:quiz3
quiz1 = """Straight outta ___1___, crazy ___2___ named ___3___ , from the gang called Niggas Wit ___4___"""
quiz2 = """Niggas I used to run with is rich or doing years in the hundreds I switched my ___1___;instead of saying fuck ___2___ That ___3___ that bought a bottle could've struck the ___4___"""
quiz3 = """My ___1___ fuck ___2___ I'll get 7 ___3___ from your mother for a dollar ___4___"""


# answers for quiz1, quiz2, and quiz3
answer1 = ["Compton", "motherfucker", "Ice Cube", "Attitude"]
answer2 = ["motto", "tomorrow", "buck", "lotto"]
answer3 = ["motto", "lotto", "digits", "tomorrow"]



#Calls upon the function play_game and matches the level and answer to the level based on a players response to the intitial user_response
def madlib_answers():
    print ("Welcome to Hip Hop Lyrics Quiz!!")
    player_level = raw_input("What level do you feel best at, easy, medium or hard?: ")
    if player_level == "easy":
        madlib_game(answer1, quiz1)
    elif player_level == "medium":
        madlib_game(answer2, quiz2)
    elif player_level == "hard":
        madlib_game(answer3, quiz3)
    else:
        print ("You only got three choise either easy, medium, or hard.")
        madlib_answers()



#This function takes a player's reponse to a question 1 - 4 and matches it tot he answer for the specific level. If a user fails to answer the question 3 times, the game will be over.
def madlib_game(chosen_answer, chosen_level):
    attempts = 3
    player_blank = 0
    while player_blank < len(blanks):
        print chosen_level
        player_answers = raw_input("What is answer to " + blanks[player_blank] + "?")
        if player_answers == chosen_answer[player_blank]:
            print ("Correct! Keep going!" + blanks[player_blank] + ".")
            chosen_level = chosen_level.replace(blanks[player_blank], player_answers)
            player_blank += 1
            if player_blank == len(blanks):
                print chosen_level
                print ("congrats!! You've completed the quiz!!")
                exit ()
        else:
            attempts -= 1
            print ("Wrong answer. Try again. You have" + str(attempts) + "Chances left.")
            if attempts == 0:
                print ("Sorry, max number of attempts reached. Program closed......")
                quit()
madlib_answers()



























