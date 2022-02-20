player1 = input("Player 1, please choose rock, paper, or scissors: ")
print("\n" * 100)
player2 = input("Player 2, please choose rock, paper, or scissors: ")


rock_beats_scissors = player1 == "rock" and player1 == "scissors"
scissors_beats_paper = player1 == "scissors" and player2 == "paper"
paper_beats_rock = player1 == "paper" and player2 == "rock"
player1_win = rock+beats_scissor or scissors_beats_paper or paper_beats_rock

if player1 == player2:
    print("Tie")

elif player1_win:
    print("Player 1 wins!")

else:
    print("player 2wins!")
