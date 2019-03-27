## Algorithms and Design Thinking

Computers are becoming more capable all of the time. For example:

- IBM Watson wins the game show Jeopardy [[video]](https://www.youtube.com/watch?v=P18EdAKuC1U)
- IBM Deep Blue defeats grand master at chess [[video]](https://www.youtube.com/watch?v=NJarxpYyoFI)
- AlphaGo beats two professional Go champions [[video]](https://www.youtube.com/watch?v=8tq1C8spV_g)
- Libratus beats professional poker players [[video]](https://www.youtube.com/watch?v=Jgau2BKTHbk)

These computers use complex algorithms – sets of instructions – to solve highly complex problems. Spend a few minutes [reading this article about algorithms](https://blog.pandorafms.org/what-is-an-algorithm/) before working through the following activities.

---

### 1. Human Against Machine

We're going to explore the concept of algorithms further by looking at a game called _Pins_. 

- Your instructor will spend a few minutes showing a demo of the game.

![Image](img/robot.png)

Who would have thought that a computer could out-bluff a human? Let's fight back!

Follow these steps:
- [Download](docs/Pins.pdf) and read the rules of Pins.
- Find a partner to work with - two minds are better than one!
- Using the sticks your instructor has provided, play a few games against each other. One of you will be the human and the other will be the computer. You should alternate between who goes first in each game. Your goal is to determine if there is an algorithm you can use to win the game every time.
- Use the provided pens and paper to help find a solution and/or draw a visual model of your solution.

Spend around 25 minutes working on your solution before moving on to Activity 2.

---

### 2. Generalising Your Algorithm

Hopefully you managed to find a strategy to win every time with 21 pins, but what if we start the game using a different number of pins? Does your algorithm still guarantee you the win? 

The [Python](https://www.python.org/) script below will allow you to test your solution using any number of pins. Copy and paste the code into the editor section of this [Online Python Interpreter](https://repl.it/languages/python3) and click _Run_. 

You'll see some statements printed out to the console on the right side of the page. Use your keyboard to play the game by entering the values as requested. You can start the game again at any time by clicking _Run_ again.

```
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
```

After playing the game with different values, spend a few minutes reading the Python code and trying to determine what each part is doing. Can you find the line(s) of code that the computer is using to beat us? Feel free to change some values and run the program again to see how it changes the outcome. 

If something goes wrong, you can always copy and paste the original code in again.

---

### 3. Scratch Implementation

Now we will explore the code used to create the visual game of 21 Pins in Scratch.

Follow these steps to get started:
- Download this file to your computer: [21Pins.sb3](code/21Pins.sb3)
- Open the [Scratch website](https://scratch.mit.edu] and click the _Create_ link at the top of the page.
- Once the project editor has loaded, select _File_ > _Load from your computer_ and open the file that you downloaded earlier.

Once the project has loaded, you will see code blocks in the centre of the editor window and the robot in the visual stage. Click the green flag above the visual stage to start the program. 

Complete the following tasks:
1. Test your algorithm using this version of 21 Pins. Does everything still work as expected? 
2. Compare the code blocks in this Scratch version with the Python code from Activity 2. Can you see any similarities? Any major differences? 
3. Make some changes to code blocks, run the program again and note the results.

You should start to realise that when a developer creates a program, they are essentially creating a set of algorithms. A computer program is a set of commands given to the machine, written in a specific language, to perform a series of specific operations in order to obtain a result. Computers don't understand human language so the programming language is therefore the tool that serves as a bridge between the human language and the language that the machine can understand. 

---

### Conclusion
While we have only looked at some simple algorithms today, the algorithm is at the heart of many powerful technologies such as artificial intelligence. You may have also heard of other advanced topics such as machine learning and deep learning, which are being used to develop smart technologies such as self-driving cars. 

What do you think the future of algorithms holds? Will computers one day rule the Earth? If so, let's hope they are kind!

---

### Links

- [Information Technology at Federation University](https://federation.edu.au/schools/school-of-science-engineering-and-information-technology/areas-of-study/information-technology)

