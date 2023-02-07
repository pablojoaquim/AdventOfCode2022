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
        packets = []
        
        print("Initializing...", flush=True)

        # Open the file with the inputs
        with open('tst/tst_input.txt') as f:
            while (True):
                packet1 = f.readline()
                packet2 = f.readline()
                delimiter = f.readline()
                
                # Check for EOF
                if not packet1:
                    break
                if not packet2:
                    break
                if (packet1 != "\n" and packet2 != "\n"):
                    packet1 = packet1.replace('\n', '').lstrip()
                    packet2 = packet2.replace('\n', '').lstrip()
                    
                    packets.append((packet1,packet2))
                     
                    # heights = []
                    # heights[:0] = line
                    # # heights = [ord(x) for x in line]
                    # print("heights:" + str(heights), flush=True)
                    # mazemap.append(heights)
        # printMatrix("Maze", mazemap)
        
        # # Look for the Starting position
        # start = 0
        # for rowIdx,row in enumerate(mazemap):
        #     for colIdx,elems in enumerate(row):
        #         if (elems == 'S'):
        #             start = (rowIdx, colIdx)
        #             break
        #     if(start != 0):
        #         break
        
        # # Look for the Ending position
        # end = 0
        # for rowIdx,row in enumerate(mazemap):
        #     for colIdx,elems in enumerate(row):
        #         if (elems == 'E'):
        #             end = (rowIdx, colIdx)
        #             break
        #     if(end != 0):
        #         break

        # # The input file is made by characters, so I change it by numbers
        # new_mazemap = []
        # for row in mazemap:
        #     conv = [ord(x) for x in row]
        #     new_mazemap.append(conv)
        # printMatrix("new_mazemap", new_mazemap)
        
        # # Now find the path
        # path = findShortestPath(new_mazemap, start, end, ord('a'), ord('z'))
        # print(len(path)-1)
        print(packets)
        
    except RuntimeError:
        print("Finishing...", flush=True)
