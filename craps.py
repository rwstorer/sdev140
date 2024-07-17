"""
File: craps.py

This module studies and plays the 
game of craps.
"""

from die import Die

class Player(object):

    def __init__(self):
        """Has a pair of dice and an empty rolls list."""
        self.die1 = Die()
        self.die2 = Die()
        self.roll: str = ''
        self.roll_cnt: int = 0
        self.winner: bool = False
        self.loser: bool = False
        self.first_roll: int = 0
        
    def rollDice(self) -> None:
        self.die1.roll()
        self.die2.roll()
        self.roll = self.__str__()
        self.roll_cnt += 1
        cur_roll: int = self.die1.getValue() + self.die2.getValue()
        if self.roll_cnt == 1:
            self.first_roll = self.die1.getValue() + self.die2.getValue()
            if self.first_roll in (7,11):
                self.winner = True
                self.loser = False
            elif self.first_roll in (2,3,12):
                self.loser = True
                self.winner = False
        elif self.first_roll == cur_roll:
            self.winner = True
            self.loser = False
        elif cur_roll in (2,3,7,12):
            self.winner = False
            self.loser = True
    
    def isWinner(self) -> bool:
        return self.winner
    
    def isLoser(self) -> bool:
        return self.loser

    def __str__(self):
        """Returns string of the roll."""
        result = 'Die 1: ' + str(self.die1.getValue())
        result += 'Die 2: ' + str(self.die2.getValue())
        result += ('Total: ' +
            str(self.die1.getValue() + self.die2.getValue()))
        
        return result

    def getNumberOfRolls(self) -> int:
        """Returns the number of the rolls."""
        return self.roll_cnt

    def play(self):
        """user can make individual rolls of the dice 
        and view the results after each roll. Saves the string
        representation of each roll after it is made."""

        self.rollDice()

def playOneGame():
    """Plays a single game and prints the results."""
    player = Player()
    player.play()
    print(player)
    youWin: bool = player.isWinner()
    if youWin:
        print("You win!")
    else:
        print("You lose!")

def playManyGames(number):
    """Plays a number of games and prints statistics."""
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    player = Player()
    for count in range(number):
        player.play()
        hasWon = player.isWinner()
        rolls = player.getNumberOfRolls()
        if hasWon:
            wins += 1
            winRolls += rolls
        else:
            losses += 1
            lossRolls += rolls
        print(player)
        
    print("The total number of wins is", wins)
    print("The total number of losses is", losses)
    if wins > 0:
        print("The average number of rolls per win is %0.2f" % \
          (winRolls / wins))
    if losses > 0:
        print("The average number of rolls per loss is %0.2f" % \
          (lossRolls / losses))
    print("The winning percentage is %0.3f" % (wins / number))

def main():
    """Plays a number of games and prints statistics."""
    number = int(input("Enter the number of games: "))
    playManyGames(number)

if __name__ == "__main__":
    main()