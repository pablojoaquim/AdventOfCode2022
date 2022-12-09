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

class Dwarfs:
    def __init__(self, calories):
        self.calories = calories
    
    def addCalories(self, calories):
        self.calories += calories
    
    def getCalories(self):
        return self.calories
    
calories = []
    
# ******************************************************************************
# * Function Definitions
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
        with open('tst/input.txt') as f:
            for line in f:           
                if(line != "\n"):
                    currCalories = int(line)
                    if(len(calories)<=dwarfIdx):
                        calories.append(0)
                    calories[dwarfIdx] += currCalories
                    # dwarf = Dwarfs(calories)
                else:
                    dwarfIdx += 1
                # print(dwarf.getCalories(), flush=True)
                print(calories, flush=True)
            
            
    except RuntimeError:
        print("Finishing...", flush=True)

