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
        visibleTrees = 0
        forest = []
        print("Initializing...", flush=True)

        # Open the file with the inputs
        with open('tst/input.txt') as f:
            # Move along the lines of the input file
            for line in f:
                # The separator is an EOL character
                if(line != "\n"):
                    # Remove the EOL character of every line
                    line = line.replace('\n', '')
                    forest.append(list(line))

        
        rows = len(forest)
        columns = len(forest[0])
        print("rows qty:" + str(rows), flush=True)
        print("columns qty:" + str(columns), flush=True)

        
        for y in range(1, rows-1):
            for x in range(1,columns-1):
                # print(str(forest[y][x]), flush=True)
                print("(" + str(x) + "," + str(y) + ")", flush=True)
                
                visibleTree = True
                for xLeft in reversed(range(0,x)):
                    if(forest[y][x]<=forest[y][xLeft]):
                        visibleTree = False
                        print("hiddenTree cond 1:" + str(forest[y][xLeft]), flush=True)
                        break
                    else:
                        visibleTree = True
                        print("visibleTree cond 1:" + str(forest[y][xLeft]), flush=True)
                if(visibleTree == False):
                    for xRight in range(x+1,columns):
                        if(forest[y][x]<=forest[y][xRight]):
                            visibleTree = False
                            print("hiddenTree cond 2:" + str(forest[y][xRight]), flush=True)
                            break
                        else:
                            visibleTree = True
                            print("visibleTree cond 2:" + str(forest[y][xRight]), flush=True)
                if(visibleTree == False):
                    for yUp in reversed(range(0,y)):
                        if(forest[y][x]<=forest[yUp][x]):
                            visibleTree = False
                            print("hiddenTree cond 3:" + str(forest[yUp][x]), flush=True)
                            break
                        else:
                            visibleTree = True
                            print("visibleTree cond 3:" + str(forest[yUp][x]), flush=True)
                if(visibleTree == False):
                    for yDown in range(y+1,rows):
                        if(forest[y][x]<=forest[yDown][x]):
                            visibleTree = False
                            print("hiddenTree cond 4:" + str(forest[yDown][x]), flush=True)
                            break
                        else:
                            visibleTree = True
                            print("visibleTree cond 4:" + str(forest[yDown][x]), flush=True)                            
                
                if(visibleTree == True):
                    visibleTrees = visibleTrees + 1
                        
                    

                
            

        visibleTrees = visibleTrees + columns*2 + (rows-2)*2       
        print("Hidden trees:" + str(visibleTrees), flush=True)
        
    except RuntimeError:
        print("Finishing...", flush=True)
