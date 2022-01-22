"""
LESSON: 2.3 - Booleans
EXERCISE: Rock Paper Scissors
"""

#### ---- PLAYER INPUT ---- ####

# Ask player 1 to input rock, paper, or scissors, and
# assign to a variable called player1
# ---> TEST AFTER THIS LINE <--- #
player1 = input("Player 1, please choose rock, paper, or scissors: ")

# BONUS: "\n" is a string that represents a "new line"
# character ("enter" key on the keyboard). Knowing
# that, can you guess what this line does?
print("\n" * 100)

# Ask player 2 to input rock, paper, or scissors, and
# assign to a variable called player2
# ---> TEST AFTER THIS LINE <--- #
player2 = input("Player 2, please choose rock, paper, or scissors: ")


#### ---- CHECK FOR PLAYER 1 WINS ---- ####

# Check whether player1 is EQUAL TO "rock" AND player2
# is EQUAL TO "scissors". Assign result to a variable
# rock_beats_scissors.
# ---> TEST AFTER THIS LINE <--- #
rock_beats_scissors = player1 == "rock" and player1 == "scissors"

# Check whether player1 is EQUAL TO "scissors" AND
# player2 is EQUAL TO "paper". Assign result to a
# variable scissors_beats_paper.
scissors_beats_paper = player1 == "scissors" and player2 == "paper"

# Check whether player1 is EQUAL TO "paper" AND
# player2 is EQUAL TO "rock". Assign result to a
# variable paper_beats_rock.
paper_beats_rock = player1 == "paper" and player2 == "rock"

# Check whether rock_beats_scissors OR
# scissors_beats_paper OR paper_beats_rock. Assign
# result to a variable player1_win.
# ---> TEST AFTER THIS LINE <--- #
player1_win = rock+beats_scissor or scissors_beats_paper or paper_beats_rock


#### ---- OUTPUT WINNER ---- ####

# IF player1 is EQUAL TO player2
if player1 == player2:

    # Print message saying the result was a tie
    # ---> TEST AFTER THIS LINE <--- #
    print("Tie")

# ELIF player1_win
elif player1_win:

    # Print message saying that player 1 won the game
    # ---> TEST AFTER THIS LINE <--- #
    print("Player 1 wins!")

# ELSE
else:

    # Print message saying that player 2 won the game
    # ---> TEST AFTER THIS LINE <--- #
    print("player 2wins!")


# Turn in your Coding Exercise.

