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

LOOSE_P2 = 'X'
DRAW_P2 = 'Y'
WIN_P2 = 'Z'

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'

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
                    strategy_player2 = line[2] # This is my strategy
                    player2 = ''
                    
                    if (strategy_player2 == LOOSE_P2):
                        if (player1 == ROCK):
                            player2 = SCISSORS
                        elif (player1 == PAPER):
                            player2 = ROCK
                        elif (player1 == SCISSORS):
                            player2 = PAPER
                        print("Loose", flush=True)
                        score = score + 0
                            
                    elif (strategy_player2 == WIN_P2):
                        if (player1 == SCISSORS):
                            player2 = ROCK
                        elif (player1 == ROCK):
                            player2 = PAPER
                        elif (player1 == PAPER):
                            player2 = SCISSORS
                        print("Win", flush=True)
                        score = score + 6
                        
                    else:
                        player2 = player1
                        score = score + 3
                        print("Draw", flush=True)

                    if (player2 == ROCK):
                        score = score + 1
                    elif (player2 == PAPER):
                        score = score + 2
                    elif (player2 == SCISSORS):
                        score = score + 3
                                            
                    print("The score is:" + str(score), flush=True)
                                  
        print("The score is:" + str(score), flush=True)

    except RuntimeError:
        print("Finishing...", flush=True)
