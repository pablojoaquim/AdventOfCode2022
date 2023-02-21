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
    if(title != None):
        print(title)
    print('\n'.join([''.join(['{:1}'.format(item) for item in row]) 
      for row in matrix]))

# ******************************************************************************
# * @brief Calculates the Manhattan distance, which is a distance metric between 
# * two points in a N dimensional vector space. It is the sum of the lengths of 
# * the projections of the line segment between the points onto the coordinate 
# * axes. In simple terms, it is the sum of absolute difference between the 
# * measures in all dimensions of two points.
# ******************************************************************************
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# ******************************************************************************
# * @brief Return a list of the points with a Manhattan distance from a center point
# ******************************************************************************
def find_points_with_distance(x, y, distance):
    points = set()
    for i in range(-distance, distance+1):
        j = distance - abs(i)
        points.add((x+i, y+j))
        points.add((x+i, y-j))
    return list(points)

# # ******************************************************************************
# # * @brief Read all the sensors and obtain the positions in a row without beacons
# # ******************************************************************************
# def getPositionsWithoutBeacons(dataset, x_min, x_max, y):
#     positions_without_beacons = set()
#     graph = ['.']*(x_max-x_min)
        
#     for data in dataset:
#         sensor = data[0]
#         beacon = data[1]
#         distance = data[2]
        
#         for x in range(x_min,x_max):
#             point = (x,y)
#             if (point == sensor):
#                 graph[x] = 'S'
#             elif (point == beacon):
#                 graph[x] = 'B'
#             elif (graph[x] == '.'):
#                 distance_to_point = calcManhattanDistance(sensor, point)
#                 if (distance_to_point <= distance):
#                     positions_without_beacons.add(point)
#                     graph[x] = '#'
#                 elif(distance_to_point == distance+1):
#                     graph[x] = '+'
                
#     return (positions_without_beacons, graph)
                            
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
        reports = []
        print("Initializing...", flush=True)

        # Open the file with the inputs
        with open('tst/input.txt') as f:
            while (True):
                line = f.readline()
                
                # Check for EOF
                if not line:
                    break
                if (line != "\n"):
                    line = line.replace('\n', '').lstrip()
                    line = line.replace(',', '').lstrip()
                    line = line.replace(':', '').lstrip()
                    line = line.split(" ")
                    
                    sensor_x = line[2].replace('x=', '').lstrip()
                    sensor_y = line[3].replace('y=', '').lstrip()
                    sensor = (int(sensor_x), int(sensor_y))
                    
                    beacon_x = line[8].replace('x=', '').lstrip()
                    beacon_y = line[9].replace('y=', '').lstrip()
                    beacon = (int(beacon_x), int(beacon_y))

                    distance = calcManhattanDistance(sensor, beacon)
                    
                    # Add the new sensor:beacon values to the reports
                    reports.append([sensor, beacon, distance])
                    # reports[sensor] = (beacon, calcManhattanDistance(sensor, beacon))
                    
        print(reports)
        # print(len(reports))
        
        # x_min = 0
        # x_max = 0
        # max_distance = 0
        # for report in reports:
        #     if (report[0][0]<x_min):
        #         x_min = report[0][0]
        #     if (report[0][0]>x_max):
        #         x_max = report[0][0]
        #     if (report[2]>max_distance):
        #         max_distance = report[2]

        # print(x_min)
        # print(x_max)
        # print(max_distance)
        
        
        # x_min = x_min - max_distance
        # x_max = x_max + max_distance
        # y = 2000000
        # print(x_min)
        # print(x_max)
        # y=10
        
        # x_min=0
        # x_max=4000000
        # y_min=0
        # y_max=4000000
        
        # x_min=0
        # x_max=20
        # y_min=0
        # y_max=20
         
        # graph = []        
        # for y in range(y_min,y_max):
        #     positionsWithoutBeacon, rowGraph = getPositionsWithoutBeacons(reports, x_min, x_max, y)
        #     graph.append(rowGraph)
        # #     # if ('.' in rowGraph):
        # #     #     break
        # #     # print(graph)
        # #     # print (len(getPositionsWithoutBeacons(reports, x_min, x_max, y)))
        # #     # print (len(positionsWithoutBeacon))
        
        # printMatrix(None, graph)
        
        # # Look for the distress signal
        # for y in range(len(graph)):
        #     for x in range(len(graph[y])):
        #         if (graph[y][x] == '.'):
        #             print("x =", x," y =", y)
        #             distress_signal = 4000000 * x + y
        #             print("distress signal =", distress_signal)
        
        for report in reports:
            sensor = report[0]
            distance = report[2]
            points = find_points_with_distance(sensor[0], sensor[1], distance)
            print(f"Puntos: {points}")
            
            # dataset = []
            # dataset.append(report)
            # graph = []
            # for y in range(y_min,y_max):
            #     positionsWithoutBeacon, rowGraph = getPositionsWithoutBeacons(dataset, x_min, x_max, y)
            #     graph.append(rowGraph)        
            # printMatrix(None, graph)
            # print('\n')
            # print('\n')
        
        
    except RuntimeError:
        print("Finishing...", flush=True)
