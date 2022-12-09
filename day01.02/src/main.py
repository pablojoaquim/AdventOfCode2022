# ******************************************************************************
# * @file main.py
# * @author Pablo Joaquim
# * @brief The entry point
# *
# * @copyright NA
# *
# ******************************************************************************

# ******************************************************************************
# * import modules
# ******************************************************************************
import logging
import signal

# ******************************************************************************
# * Objects Declarations
# ******************************************************************************

# ******************************************************************************
# * Object and variables Definitions
# ******************************************************************************
running = True

class Dwarf:
    def __init__(self, calories):
        self.calories = calories

    def addCalories(self, calories):
        self.calories += calories

    def getCalories(self):
        return self.calories

class DwarfWinners:
    def __init__(self):
        self.winners = [0,0,0]

    def challenge(self, calories):
        if(calories>self.winners[0]):
            if(self.winners[0]>self.winners[1]):
                if(self.winners[1]>self.winners[2]):
                    self.winners[2] = self.winners[1]
                self.winners[1] = self.winners[0]
            self.winners[0] = calories
        else:
            if(calories>self.winners[1]):
                if(self.winners[1]>self.winners[2]):
                    self.winners[2] = self.winners[1]
                self.winners[1] = calories
            else:
                if(calories>self.winners[2]):
                    self.winners[2] = calories
                    
    def getWinners(self):
        return self.winners
    
    def getWinnersTotalCalories(self):
        return self.winners[0] + self.winners[1] + self.winners[2]
    
calories = []

# ******************************************************************************
# * Function Definitions
# ******************************************************************************

# ******************************************************************************
# * @brief The handler for the termination signal handler
# ******************************************************************************
def sigintHandler(signum, frame):
    global running
    running = False
    print('Signal handler called with signal', signum)
    raise RuntimeError("Terminating...")


# ******************************************************************************
# * @brief The main entry point
# ******************************************************************************
if __name__ == '__main__':
    signal.signal(signal.SIGINT, sigintHandler)

    # These parameters are for the werkzeug embedded web server of Flask
    # If we're using gunicorn (WSGI production web server) these parameters are not applied
    try:
        dwarfIdx = 0
        print("Initializing...", flush=True)

        # Open the file with the inputs
        with open('tst/input.txt') as f:
            # Move along the lines of the input file
            for line in f:
                # The separator is an EOL character
                if(line != "\n"):
                    # Obtain the calories string and convert it to integer
                    currCalories = int(line)
                    # If the entry in the list is not available create a new one
                    if(len(calories) <= dwarfIdx):
                        calories.append(Dwarf(0))
                    # Add the calories to the current dwarf calories counter
                    calories[dwarfIdx].addCalories(currCalories)
                else:
                    # Increment the dwarf index
                    dwarfIdx += 1

        dwarfWinners = DwarfWinners()
        
        for dwarfIdx in range(len(calories)):
            dwarfWinners.challenge(calories[dwarfIdx].getCalories())
        #     if(dwarfWinnerCalories <= calories[dwarfIdx].getCalories()):
        #         dwarfWinnerCalories = calories[dwarfIdx].getCalories()
        #     print(calories[dwarfIdx].getCalories(), flush=True)
            
        # print("And the winner is:" + str(dwarfWinnerCalories), flush=True)
        print(dwarfWinners.getWinners(), flush=True)
        
        print("And the winner is:" + str(dwarfWinners.getWinnersTotalCalories()), flush=True)
        

    except RuntimeError:
        print("Finishing...", flush=True)
