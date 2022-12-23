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
        sectionFullyContained = 0
        print("Initializing...", flush=True)

        # Open the file with the inputs
        with open('tst/input.txt') as f:
            # Move along the lines of the input file
            for line in f:
                # The separator is an EOL character
                if(line != "\n"):
                    line = line.replace('\n', '')   # Remove the EOL character of every line
                    line = line.replace('-', ',')   # Replace the "-" to have only one kind of separator
                    sections = line.split(",")
                    # print("InitSectionElf1 found:" + str(line.split(",")), flush=True)
                    
                    initSectionElf1 = int(sections[0])
                    endSectionElf1 = int(sections[1])
                    initSectionElf2 = int(sections[2])
                    endSectionElf2 = int(sections[3])
                    
                    print("InitSectionElf1 found:" + str(initSectionElf1), flush=True)
                    print("EndSectionElf1 found:" + str(endSectionElf1), flush=True)
                    print("InitSectionElf2 found:" + str(initSectionElf2), flush=True)
                    print("EndSectionElf2 found:" + str(endSectionElf2), flush=True)
                    
                    if(initSectionElf2>=initSectionElf1 and endSectionElf2<=endSectionElf1):
                        sectionFullyContained = sectionFullyContained + 1
                        print("sectionFullyContained found 1", flush=True)
                    elif(initSectionElf1>=initSectionElf2 and endSectionElf1<=endSectionElf2):
                        sectionFullyContained = sectionFullyContained + 1
                        print("sectionFullyContained found 2", flush=True)
                        
                    


        print("sectionFullyContained sum:" + str(sectionFullyContained), flush=True)
        
    except RuntimeError:
        print("Finishing...", flush=True)
