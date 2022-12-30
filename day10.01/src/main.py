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
import math

# ******************************************************************************
# * Objects Declarations
# ******************************************************************************
class TheControl:
    def __init__(self):
        self.xRegister = 1
        self.cycles = 0
        self.cycleToCheck = 20
        self.signalStrength = 0

    # ******************************************************************************
    # * @brief Calculate the signal strength every 40 cycles, from the 20th cycle
    # ******************************************************************************
    def checkAndCalcSignalStrength(self):   
        strength = 0
        if(self.cycles >= self.cycleToCheck):
            strength = self.cycleToCheck * self.xRegister
            
            print("----------", flush=True)
            print("xRegister:" + str(self.xRegister), flush=True)
            print("strength:" + str(strength), flush=True)
            print("cycles:" + str(self.cycles), flush=True)
            print("cycleToCheck:" + str(self.cycleToCheck), flush=True)
            
            self.cycleToCheck = self.cycleToCheck + 40
            
        self.signalStrength = self.signalStrength + strength

    # ******************************************************************************
    # * @brief Verify if the 220 cycles of operation has been elapsed
    # ******************************************************************************
    def checkFinishOperation(self):
        if(self.cycles>220):
            return True
        return False
    
    # ******************************************************************************
    # * @brief Increment the cycles counter
    # ******************************************************************************
    def incrementCycleCounter(self):
        self.cycles = self.cycles + 1
        self.checkAndCalcSignalStrength()

    # ******************************************************************************
    # * @brief Process the noop command
    # ******************************************************************************
    def noop(self):
        self.incrementCycleCounter()
                
    # ******************************************************************************
    # * @brief Process the addx command
    # ******************************************************************************
    def addx(self, sum):
        self.incrementCycleCounter()
        self.incrementCycleCounter()
        self.xRegister = self.xRegister + sum
    
    # ******************************************************************************
    # * @brief Get the Signal Strength value
    # ******************************************************************************
    def getSignalStrength(self):
        return self.signalStrength
        
# ******************************************************************************
# * Object and variables Definitions
# ******************************************************************************
running = True
        
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
        theControl = TheControl()
        
        print("Initializing...", flush=True)

        # Open the file with the inputs
        with open('tst/input.txt') as f:
            # Move along the lines of the input file
            for line in f:
                # The separator is an EOL character
                if(line != "\n"):
                    # Remove the EOL character of every line
                    line = line.replace('\n', '')
                    values = line.split(" ")
                    
                    if(values[0] == "noop"):
                        theControl.noop()
       
                    elif(values[0] == "addx"):
                        theControl.addx(int(values[1]))
                        
                    if(theControl.checkFinishOperation()):
                        break
                        
        print("signalStrength:" + str(theControl.getSignalStrength()), flush=True)
        
    except RuntimeError:
        print("Finishing...", flush=True)
