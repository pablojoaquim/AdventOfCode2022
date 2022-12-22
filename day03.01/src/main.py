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
        priorities = 0
        print("Initializing...", flush=True)

        # Open the file with the inputs
        with open('tst/input.txt') as f:
            # Move along the lines of the input file
            for line in f:
                # The separator is an EOL character
                if(line != "\n"):
                    rucksackSize = len(line) - 1
                    compartmentSize = rucksackSize//2
                    compartment1 = line[0:compartmentSize]
                    compartment2 = line[compartmentSize:]
                    print("compartment1 found:" + str(compartment1), flush=True)
                    print("compartment2 found:" + str(compartment2), flush=True)
                    
                    for w in set(compartment1):
                        if w in compartment2:
                            print("Match found:" + str(w), flush=True)
                            cmp = ord(w)
                            limLowLowercase=ord('a')
                            limHighLowercase=ord('z')
                            limLowUppercase=ord('A')
                            limHighUppercase=ord('Z')
                            if (cmp>=limLowLowercase and cmp<=limHighLowercase):
                                priorities = priorities + cmp-limLowLowercase + 1
                            elif (cmp>=limLowUppercase and cmp<=limHighUppercase):
                                priorities = priorities + cmp-limLowUppercase + 27
                    
                    # # Obtain the calories string and convert it to integer
                    # currCalories = int(line)
                    # # If the entry in the list is not available create a new one
                    # if(len(calories) <= dwarfIdx):
                    #     calories.append(Dwarf(0))
                    # # Add the calories to the current dwarf calories counter
                    # calories[dwarfIdx].addCalories(currCalories)
                # else:
                #     # Increment the dwarf index
                #     dwarfIdx += 1

        # dwarfWinnerCalories = 0
        
        # for dwarfIdx in range(len(calories)):
        #     if(dwarfWinnerCalories <= calories[dwarfIdx].getCalories()):
        #         dwarfWinnerCalories = calories[dwarfIdx].getCalories()
        #     print(calories[dwarfIdx].getCalories(), flush=True)
            
        # print("And the winner is:" + str(dwarfWinnerCalories), flush=True)
        print("Priorities sum:" + str(priorities), flush=True)
        
    except RuntimeError:
        print("Finishing...", flush=True)
