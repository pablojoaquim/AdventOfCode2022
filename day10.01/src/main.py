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

# ******************************************************************************
# * Object and variables Definitions
# ******************************************************************************
running = True

xRegister = 1
cycles = 0
cycleToCheck = 20
signalStrength = 0
        
# ******************************************************************************
# * Function Definitions
# ******************************************************************************
 
# ******************************************************************************
# * @brief The handler for the termination signal handler
# ******************************************************************************
def checkAndCalcSignalStrength():
    global xRegister
    global cycles
    global cycleToCheck
    
    strength = 0
    if(cycles >= cycleToCheck):
        strength = cycleToCheck * xRegister
        
        print("----------", flush=True)
        print("xRegister:" + str(xRegister), flush=True)
        print("signalStrength:" + str(strength), flush=True)
        print("cycles:" + str(cycles), flush=True)
        print("cycleToCheck:" + str(cycleToCheck), flush=True)
        
        cycleToCheck = cycleToCheck + 40
        # if(cycles>220):
        #     break
    return strength
 
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
                        cycles = cycles + 1
                        signalStrength = signalStrength + checkAndCalcSignalStrength()
                        # print("xRegister [" + str(cycles) + "]" + str(xRegister), flush=True)
                        
                    elif(values[0] == "addx"):
                        cycles = cycles + 1
                        signalStrength = signalStrength + checkAndCalcSignalStrength()
                        # print("xRegister [" + str(cycles) + "]" + str(xRegister), flush=True)
                        cycles = cycles + 1
                        signalStrength = signalStrength + checkAndCalcSignalStrength()
                        
                        xRegister = xRegister + int(values[1])
                        # print("xRegister [" + str(cycles) + "]" + str(xRegister), flush=True)
                    
                    
                    
                    # if(cycles >= cycleToCheck):
                    #     signalStrength = cycleToCheck * xRegister
                    #     print("registerX:" + str(xRegister), flush=True)
                    #     print("signalStrength:" + str(signalStrength), flush=True)
                    #     print("cycles:" + str(cycles), flush=True)
                    #     print("cycleToCheck:" + str(cycleToCheck), flush=True)
                        
                    #     cycleToCheck = cycleToCheck + 40
                    if(cycles>220):
                        break

                        
        print("signalStrength:" + str(signalStrength), flush=True)
        
    except RuntimeError:
        print("Finishing...", flush=True)
