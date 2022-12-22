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
            for rucksackSizeA in f:
                # Move along the lines of the input file
                rucksackSizeA = rucksackSizeA.strip()
                rucksackSizeB = f.readline().strip()
                rucksackSizeC = f.readline().strip()
                
                print("rucksackSizeA:" + str(rucksackSizeA), flush=True)
                print("rucksackSizeB:" + str(rucksackSizeB), flush=True)
                print("rucksackSizeC:" + str(rucksackSizeC), flush=True)

                # The separator is an EOL character
                if(rucksackSizeA != "\n" and rucksackSizeB != "\n" and rucksackSizeC != "\n"):                
                    for w in set(rucksackSizeA):
                        if (w in rucksackSizeB and w in rucksackSizeC):
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
            
        # print("And the winner is:" + str(dwarfWinnerCalories), flush=True)
        print("Priorities sum:" + str(priorities), flush=True)
        
    except RuntimeError:
        print("Finishing...", flush=True)
