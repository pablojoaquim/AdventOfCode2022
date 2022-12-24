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
# * @brief Matrix transpose function
# ******************************************************************************
def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    matrix_T = []
    for j in range(columns):
        row = []
        for i in range(rows):
           row.append(matrix[i][j])
        matrix_T.append(row)

    return matrix_T

# ******************************************************************************
# * @brief Revert the elements on each row of the matrix
# ******************************************************************************
def revertRows(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    matrix_T = []
    for i in range(rows):
        row = []
        for j in range(columns-1, -1, -1):
           row.append(matrix[i][j])
        matrix_T.append(row)

    return matrix_T

# ******************************************************************************
# * @brief Remove unnecesary elements of the matrix
# ******************************************************************************
def removeElems(matrix, e):
    rows = len(matrix)
    columns = len(matrix[0])

    matrix_T = []
    for i in range(rows):
        row = []
        for j in range(columns):
            if(matrix[i][j] != e):
                row.append(matrix[i][j])
        matrix_T.append(row)

    return matrix_T

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
                            # We want the columns instead of the rows
                            stacks = transpose(stacks)
                            print("stacks transpose:" + str(stacks), flush=True)
                            # The rows should be reverted to have the first elements to remove at the end of each row
                            stacks = revertRows(stacks)
                            print("stacks reverted:" + str(stacks), flush=True)
                            # Clean the unnecesary elements created during the parsing process
                            stacks = removeElems(stacks,' ')
                            print("stacks cleaned:" + str(stacks), flush=True)
                    else:
                        # Remove unnecesary words
                        line = line.replace("move ", '')
                        line = line.replace("from ", '')
                        line = line.replace("to ", '')
                        # Parse the instructions
                        instructions = line.split(" ")
                        print("Instructions found:" + str(instructions), flush=True)                        
                        
                        # print("Instructions found:" + str(stacks[1][0:2]), flush=True)
                        dest = 2
                        orig = 1
                        
                        # stacks[dest].
                        # # Check if there's available free space in the column
                        # if(stacks[dest][0] != " "):
                            
                        # else:
                        #     #Find the first available position in the destiny
                        #     for i in range(len(stacks[dest])):
                        #         if(stacks[dest][i] != " "):        
                        #             stacks[dest][i-1] = stacks[orig][0]
                        #             stacks[orig][0] = ''
                        # # stacks[dest][0] = stacks[orig][1]
                        # # stacks[orig][1] = ''
                        # print("Instructions found:" + str(stacks), flush=True)
                        break



        # print("sectionOverlap sum:" + str(sectionOverlap), flush=True)
        
    except RuntimeError:
        print("Finishing...", flush=True)
