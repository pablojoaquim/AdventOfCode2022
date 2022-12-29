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

# ******************************************************************************
# * Function Definitions
# ******************************************************************************

# ******************************************************************************
# * @brief Calc the length of the vector between two points
# ******************************************************************************
def calcDistance(p1, p2):
    dist = math.sqrt((p2[1]-p1[1])*(p2[1]-p1[1])+(p2[0]-p1[0])*(p2[0]-p1[0]))
    return dist

# ******************************************************************************
# * @brief Calc the length of the vector between two points
# ******************************************************************************
def updateRopePosition(places, head, tail, direction, steps):
    for x in range(steps):
        prevHeadPosition = list(head)
        if(direction == 'R'):
            head[0] = head[0] + 1
        elif(direction == 'L'):
            head[0] = head[0] - 1
        elif(direction == 'U'):
            head[1] = head[1] + 1
        elif(direction == 'D'):
            head[1] = head[1] - 1                   
        
        dist = calcDistance(head, tail)
        if(dist >= 2):
            tail[0] = prevHeadPosition[0]
            tail[1] = prevHeadPosition[1]
            if places.count(tail) == 0:
                places.append(list(tail))
        print("dist:" + str(dist), flush=True)
        print("headPosition:" + str(head), flush=True)
        print("tailPosition:" + str(tail), flush=True)      

    
    
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
        startPosition = list([0,0])
        headPosition = list(startPosition)
        tailPosition = list(startPosition)
        placesVisited = []
        
        # Add the initial point to the places
        placesVisited.append(list(tailPosition))
        
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
                    direction = values[0]
                    steps = int(values[1])
                    print("direction:" + str(direction), flush=True)
                    print("steps:" + str(steps), flush=True)

                    updateRopePosition(placesVisited, headPosition, tailPosition, direction, steps)
                    # print("headPosition:" + str(headPosition), flush=True)
                    # print("tailPosition:" + str(tailPosition), flush=True)               
                    # print("route:" + str(placesVisited), flush=True)
    
            
        print("route length:" + str(len(placesVisited)), flush=True)
        
             
        
        
    except RuntimeError:
        print("Finishing...", flush=True)
