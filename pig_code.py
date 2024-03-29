import random

#Function for rolling the dice
def roll_number():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

#User input for starting game
while True:
    players = input("Enter the number of players participating (2-4):\n")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Number must be between 2 and 4.")
    elif players.isalpha(): #Looks if input = a letter, not a number
        print("Letters are an invalid entry, please input a number and try again.")
    else:
        print("Invalid entry, please try again.")

#Max score and creating the players' scores
max_score = 50
player_scores = [0 for _ in range(players)]
print(player_scores)

#Creating each player's turn
while max(player_scores) < max_score:
    for player_index in range(players):
        print(f"Player {player_index + 1}'s turn has just started!\n")

        current_score = 0

        while True:
            roll = input("Would you like to roll (y)?")
            if roll.lower() != "y":
                break

            value = roll_number()
            if value == 1:
                print("You rolled a 1!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}!")

            print(f"Your score is: {current_score}!")

        player_scores[player_index] += current_score
        print(f"Your final score was: {player_scores[player_index]}!")

#End game results
max_score = max(player_scores)
winning_index = player_scores.index(max_score)
print(f"Player {winning_index + 1} is the winner with a score of {max_score}! \nThanks for playing!")