from random import randint

class PinsHumanAgainstMachine:
    playAgain = True
    numberPins = 21
    takePins = 0
    computer = 2
    human = 1
    whoseTurn = 1
        
    '''
    Sets whether the player is going first or second
    '''
    def setPlayerOrder(self,humanNumber):
        self.human = humanNumber
        if self.human == 1:
            self.computer = 2
        else:
            self.computer = 1
        self.whoseTurn = 1
        
    '''
    Completes all the actions required for a turns
    '''
    def processTurn(self,takePins):
        if takePins < 1 or takePins > 3:
            print("Invalid number of pins!")
        elif takePins > int(self.numberPins):
            print("Too many pins selected!  Pins remaining: " + self.numberPins + ".")
        else:
            self.numberPins = int(self.numberPins) - takePins
      
        if self.whoseTurn == 1:
            self.whoseTurn = 2
        else:
            self.whoseTurn = 1
      
        if self.numberPins == 0:
            winner = ""
            if self.whoseTurn == self.human:
                winner = "Human"
            else:
                winner = "Machine"
            print("Game Over! " + winner + " wins!")
        else:
            print("Pins remaining: " + str(self.numberPins))

def playGame(gameObject):
    print("WELCOME TO PINS - GAME RULES\n");
    print("A machine and a human take it in turns to remove 1, 2 or 3 pins from a single pile.");
    print("Whoever takes the last pin loses the game.\n");
    
    gameObject.numberPins = input("How many pins do you want to have in the initial pile?\n")

    while int(gameObject.numberPins) <= 1:
        print("You need at least 2 pins, please try again!")
        gameObject.numberPins = input("How many pins do you want to have in the initial pile?\n")
        
    playerFirst = input("Do you wish to go first? Y/N\n")
    while playerFirst != "Y" and playerFirst != "y" and playerFirst != "N" and playerFirst != "n":
        print("Invalid input, please try again using only Y or N!")
        playerFirst = input("Do you wish to go first? Y/N\n")
    
    if playerFirst == "Y" or playerFirst == "y":
        gameObject.setPlayerOrder(1)
    else:
        gameObject.setPlayerOrder(2)
        
        
    while int(gameObject.numberPins) > 0:
        gameObject.takePins = 0;
        if gameObject.whoseTurn == gameObject.human:
            gameObject.takePins = input("Human: how many pins do you wish to take?\n")
    
            while gameObject.takePins.isdigit() == False:
                print("Not a valid input, please enter 1, 2 or 3!")
                gameObject.takePins = input("Human: how many pins do you wish to take?\n")
            gameObject.processTurn(int(gameObject.takePins))
        
        else:
            gameObject.takePins = (int(gameObject.numberPins) - 1) % 4;
        
            if gameObject.takePins == 0:
                print("I have no optimal move to make!")
         
                gameObject.takePins = randint(1, 3)
            
            print("Machine takes pins: " + str(gameObject.takePins))
        
            gameObject.processTurn(gameObject.takePins)

    
playGame(PinsHumanAgainstMachine())
    

    
    

    
    

