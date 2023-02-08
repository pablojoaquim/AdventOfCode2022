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
        sand_entering_point = (500,0)
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
                   
        min_y = 1000
        for path in paths:
            for elem in path:
               if min_y > elem[1]:
                   min_y = elem[1]
        max_y = 0
        for path in paths:
            for elem in path:
               if max_y < elem[1]:
                   max_y = elem[1]
                    
        print(min_x, min_y, max_x, max_y)
        
        # Draw the cave considering all the paths fits in it
        x_extra_size = 2
        y_extra_size = 2
        x_size = max_x - min_x + x_extra_size
        y_size = max_y - min_y + y_extra_size
        # cave = [['.'] * x_size] * y_size
        cave = [['.' for col in range(x_size)] for row in range(y_size)]

        
        x_offset = min_x - int(x_extra_size/2)
        y_offset = min_y - int(y_extra_size/2)
        print(sand_entering_point[0]-x_offset)
        print(sand_entering_point[1])
        
        # cave[sand_entering_point[1]][sand_entering_point[0]-x_offset] = 'o'
        cave[0][7] = 'o'
                     
        # print(packets)
        # cnt = 0
        # total = 0
        # for x in packets:
        #     cnt = cnt+1
        #     print ("\n== Pair ", str(cnt), " ==")
        #     if (comparePackets(x[0], x[1]) == "ok"):
        #         total = total + cnt
            
        # print(literal_eval(packets[1][0]))
        printMatrix("cave", cave)
        
    except RuntimeError:
        print("Finishing...", flush=True)
