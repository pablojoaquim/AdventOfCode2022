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
import numpy as np

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
        stacks = list()
        print("Initializing...", flush=True)

        # Open the file with the inputs
        with open('tst/tst_input.txt') as f:
            # Move along the lines of the input file
            for line in f:
                # The separator is an EOL character
                if(line != "\n"):
                    # Remove the EOL character of every line
                    line = line.replace('\n', '')               

                    # Check if there's no instructions in the row
                    if("move" not in line):
                        # Check if there's no column indexes in the row
                        if ("1" not in line):                            
                            # Parse the rows
                            row = list() 
                            for i in range(1, len(line), 4):
                                row.append(line[i])
                                print("row found:" + str(row), flush=True)
                            # Add the new row to the stack
                            stacks.append(row)
                        else:   # The end of the matrix
                            # We want the columns instead of the rows, 
                            # so, using numpy we traspose the matrix
                            stacks = np.transpose(stacks)
                            print("stacks:" + str(stacks), flush=True)
                    else:
                        # Remove unnecesary words
                        line = line.replace("move ", '')
                        line = line.replace("from ", '')
                        line = line.replace("to ", '')
                        # Parse the instructions
                        instructions = line.split(" ")
                        print("Instructions found:" + str(instructions), flush=True)


        # print("sectionOverlap sum:" + str(sectionOverlap), flush=True)
        
    except RuntimeError:
        print("Finishing...", flush=True)
