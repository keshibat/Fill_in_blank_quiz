# Fill in blank quiz
# coding:utf-8

# A list of replacement words to be passed in to the play game function.
blanks  = ["___1___", "___2___" , "___3___", "___4___"]

# The following are quizes to madlib function.
# easy:quiz1   medium:quiz2   hard:quiz3

quiz1 = """\n\
        Agent: I'm sorry, we have no mid-size available at the moment.\n
        Jerry: I don't understand, I made a reservation, do you have my reservation?\n
        Agent: Yes, we do, unfortunately we ran out of cars.\n
        Jerry: But the ___1___ keeps the car here. That's why you have the reservation.\n
        Agent: I know why we have reservations.\n
        Jerry: I don't think you do. If you did, I'd have a car. See, you know how to
        ___2___ the reservation, you just don't know how to ___3___ the reservation and
        that's really the most important part of the reservation, the ___4___. Anybody
        can just take them.
        """

quiz2 = """\n\
        Telemarketer: Hi, would you be interested in switching over to TMI long distance service?\n
        Jerry: Oh, gee, I can't talk right now. Why don't you give me your home ___1___\n
               and I'll call you later?\n
        Telemarketer: Uh, well I'm sorry, we're not ___2___ to do that.\n
        Jerry: Oh, I guess you don't want people calling you at ___3___.\n
        Telemarketer: No.\n
        Jerry: Well, now you know how I ___4___. [Jerry hangs up phone]
        """

quiz3 = """\n\
        MRS.SOKOL: Can you be specific about any of these companies?\n
        GEORGE: Specific, Ah, lets see. I've walked in and out of so many buildings\n 
                they all. blend in together, I uh\n
        MRS.SOKOL: Well just give me one name.\n
        GEORGE: Absolutely, uh, lets see there's, uh, ___1___ Industries, I just saw\n 
                them. I got very close there. very close.\n
        MRS.SOKOL: And what type of company is that?\n
        GEORGE: ___2___, latex manufacturing\n
        MRS.SOKOL: And you interviewed there?\n
        GEORGE: Yes, for a ___3___ position. Latex ___4___, the selling of latex, and\n 
                latex related products. They just wouldn't give me a chance.
        """


# answers for quiz1, quiz2, and quiz3
answer1 = ["reservation", "take", "hold", "holding"]
answer2 = ["number", "allowed", "home", "feel"]
answer3 = ["Vandaley", "Latex", "sales", "salesman"]


#Calls upon the function play_game and matches the level and answer to the level based on a players response to the intitial user_response
def madlib_answers():
    print ("Welcome to Seinfeld Quiz!!")
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
        player_answers = raw_input("What is answer to" "\n"+ blanks[player_blank] + "?" "\n")
        if player_answers == chosen_answer[player_blank]:
            print ("Correct! Keep going!" + blanks[player_blank] + ".")
            chosen_level = chosen_level.replace(blanks[player_blank], player_answers)
            player_blank += 1
            if player_blank == len(blanks):
                print chosen_level
                print ("Congrats!! You've completed the quiz!!")
                exit ()
        else:
            attempts -= 1
            print ("Wrong answer. Try again. You have" + " "+ str(attempts) + " " + "Chances left.")
            if attempts == 0:
                print ("Sorry, max number of attempts reached. Program closed......")
                quit()
madlib_answers()

