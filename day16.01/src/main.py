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
        scanData = []
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
                    line = line.replace(',', '').lstrip()
                    line = line.replace(';', '').lstrip()
                    line = line.replace('=', ' ').lstrip()
                    line = line.split(" ")
                    
                    valvesList = []
                    for i in range(10, len(line)):
                        valvesList.append(line[i])
                        
                    data = (line[1], int(line[5]), valvesList)
                    scanData.append(data)
                    # print(data)
                    

        for data in scanData:
            print(data)
        
    except RuntimeError:
        print("Finishing...", flush=True)
