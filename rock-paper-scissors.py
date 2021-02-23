import random


#function for user input against computer
def play():
  #gets user input and computer will choose
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

#we know the choice now
#conditionals to see who won
    if user == computer:
        return 'It\'s a tie'


#go define a function first
    # r > s, s > p, p > r
    #the player is you and opponent is computer
    if is_win(user, computer):
        return 'You won!'
#otherwise, if computer won, then we lost
#if we pass these cases just say you lost instead of else
#only way to get here is if we lose
    return 'You lost!'


def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        #returns true if player beats the opponent
        return True

print(play())
