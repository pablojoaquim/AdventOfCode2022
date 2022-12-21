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

ROCK_P2 = 'X'
PAPER_P2 = 'Y'
SCISSORS_P2 = 'Z'

ROCK_P1 = 'A'
PAPER_P1 = 'B'
SCISSORS_P1 = 'C'

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

    try:
        score = 0
        print("Initializing...", flush=True)

        # Open the file with the inputs
        with open('tst/input.txt') as f:
            # Move along the lines of the input file
            for line in f:
                # The separator is an EOL character
                if(line != "\n"):
                    # Obtain the rock, paper scissors
                    player1 = line[0] # This is the opponent
                    player2 = line[2] # This is me
                    
                    if (player2 == ROCK_P2): # X for Rock (1 points)
                        score = score + 1
                    elif (player2 == PAPER_P2): # Y for Paper (2 points)
                        score = score + 2
                    elif (player2 == SCISSORS_P2): # Z for Scissors (3 points)
                        score = score + 3
                        
                    # Draw
                    if (player1 == ROCK_P1 and player2 == ROCK_P2) or (player1 == PAPER_P1 and player2 == PAPER_P2) or (player1 == SCISSORS_P1 and player2 == SCISSORS_P2):
                        print("Draw", flush=True)
                        score = score + 3
                    
                    # Loose
                    elif (player1 == ROCK_P1 and player2 == SCISSORS_P2) or (player1 == SCISSORS_P1 and player2 == PAPER_P2) or (player1 == PAPER_P1 and player2 == ROCK_P2):
                        print("Loose", flush=True)
                        score = score + 0
                    
                    # Win
                    elif (player1 == SCISSORS_P1 and player2 == ROCK_P2) or (player1 == PAPER_P1 and player2 == SCISSORS_P2) or (player1 == ROCK_P1 and player2 == PAPER_P2):
                        print("Win", flush=True)
                        score = score + 6
                    
                    print("The score is:" + str(score), flush=True)
                                  
        print("The score is:" + str(score), flush=True)

    except RuntimeError:
        print("Finishing...", flush=True)
