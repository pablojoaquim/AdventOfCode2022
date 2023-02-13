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
import signal
from ast import literal_eval

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
# * @brief Helper function to print a matrix nicely
# ******************************************************************************
def printMatrix (title, matrix):
    print(title)
    print('\n'.join([''.join(['{:1}'.format(item) for item in row]) 
      for row in matrix]))

# ******************************************************************************
# * @brief Calculate the destination of a falling dust of sand, applying these rules:
# * A unit of sand always falls down one step if possible. If the tile immediately 
# * below is blocked (by rock or sand), the unit of sand attempts to instead move 
# * diagonally one step down and to the left. If that tile is blocked, the unit of 
# * sand attempts to instead move diagonally one step down and to the right. Sand 
# * keeps moving as long as it is able to do so, at each step trying to move down, 
# * then down-left, then down-right. If all three possible destinations are blocked, 
# * the unit of sand comes to rest and no longer moves, at which point the next unit 
# * of sand is created back at the source.
# * Return True if the dust of sand is still in the cave, and False if fallen out
# ******************************************************************************
def calcSandFalling(cave, entryPoint):
    falling = True
    sandPosition = entryPoint
    cave[sandPosition[1]-y_offset][sandPosition[0]-x_offset] = '+'
    while(falling):

        below = cave[sandPosition[1]-y_offset + 1][sandPosition[0]-x_offset]
        diagLeft = cave[sandPosition[1]-y_offset + 1][sandPosition[0]-x_offset-1]
        diagRight = cave[sandPosition[1]-y_offset + 1][sandPosition[0]-x_offset+1]
        
        if (below != '#' and below != 'o'):
            sandPosition = (sandPosition[0], sandPosition[1] + 1)
        elif (diagLeft != '#' and diagLeft != 'o'):
            sandPosition = (sandPosition[0]-1, sandPosition[1] + 1)
        elif (diagRight != '#' and diagRight != 'o'):
            sandPosition = (sandPosition[0]+1, sandPosition[1] + 1)
        else:
            falling = False
        
        if (len(cave) <= sandPosition[1] + 1):
            return False
            
    cave[sandPosition[1]-y_offset][sandPosition[0]-x_offset] = 'o'
    return True
        


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
        paths = []
        entryPoint = (500,0)
        print("Initializing...", flush=True)

        # Open the file with the inputs
        with open('tst/tst_input.txt') as f:
            while (True):
                line = f.readline()
                
                # Check for EOF
                if not line:
                    break
                if (line != "\n"):
                    line = line.replace('\n', '').lstrip()
                    line = line.split(" -> ")
                    elems = []
                    for x in line:
                        elems.append(eval(x))
                    paths.append(elems)
                
        print(paths)
        
        # Find the limits of the path on every direction
        min_x = 1000
        for path in paths:
            for elem in path:
               if min_x > elem[0]:
                   min_x = elem[0]
        max_x = 0
        for path in paths:
            for elem in path:
               if max_x < elem[0]:
                   max_x = elem[0]    
        
        max_y = 0
        for path in paths:
            for elem in path:
               if max_y < elem[1]:
                   max_y = elem[1]
                   
        # Draw the cave considering all the paths fits in it
        x_extra_size = 2
        y_extra_size = 2
        x_size = max_x - min_x + x_extra_size
        y_size = max_y + y_extra_size
        
        # cave = []
        # for i in range(y_size):
        #     row = ['.' for col in range(x_size)]
        #     cave.append(row)
        
        cave = [['.' for col in range(x_size)] for row in range(y_size)]
        # Add an offset in x to let us work with a small matrix
        x_offset = min_x - int(x_extra_size/2)
        y_offset = 0
           
        # Add the sand entry point
        cave[entryPoint[1]-y_offset][entryPoint[0]-x_offset] = 'o'
        
        # Draw the path
        for path in paths:
            for i in range(len(path)-1):
                x1 = path[i][0]
                x2 = path[i+1][0]
                y1 = path[i][1]
                y2 = path[i+1][1]
                
                if y1 == y2:
                    # Horizontal line
                    # print ("horizontal ", path[i]," -> ", path[i+1])
                    # print ("range " , x2, x1)
                    if x1<x2:
                        for i in range(x1,x2+1):
                            # print (i)
                            cave[y1-y_offset][i-x_offset] = '#'
                    else:
                        for i in range(x2,x1+1):
                            # print (i)
                            cave[y1-y_offset][i-x_offset] = '#'

                else:
                    # Vertical line
                    # print ("vertical ", path[i]," -> ", path[i+1])
                    # print ("range " , y2, y1)
                    if y1<y2:
                        for i in range(y1,y2+1):
                            # print (i)
                            cave[i-y_offset][x1-x_offset] = '#'
                    else:
                        for i in range(y2,y1+1):
                            # print (i)
                            cave[i-y_offset][x1-x_offset] = '#'
      
        # for i in range(25):
        cnt = 0
        while(calcSandFalling(cave, entryPoint)):
            cnt = cnt + 1
        
        printMatrix("cave", cave)
        print(cnt, "units of sand come to rest before sand starts flowing into the abyss below")
        
    except RuntimeError:
        print("Finishing...", flush=True)
