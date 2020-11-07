class bcolors(object):
    """
    Class to add colors to Terminal Output
    """
    # TEXT FORMATTING
    END_C   = '\033[0m'         # Used to close color formatting
    BOLDER  = '\033[1m'         # Used to make 'bold' text
    UNDERL  = '\033[4m'         # Used to 'underline' text
    
    # BASIC TEXT COLORING
    BLACK   = '\033[30m'        # Makes the text 'black'
    RED     = '\033[31m'        # Makes the text 'red'
    GREEN   = '\033[32m'        # Makes the text 'green'
    YELLOW  = '\033[33m'        # Makes the text 'yellow'
    BLUE    = '\033[34m'        # Makes the text 'blue'
    PURPLE  = '\033[35m'        # Makes the text 'purple'
    CYAN    = '\033[36m'        # Makes the text 'cyan'
    
    # BASIC TEXT BACKGROUND COLORING
    RED_BG     = '\033[41m'     # Makes the background of the text 'red'
    GREEN_BG   = '\033[42m'     # Makes the background of the text 'green'
    YELLOW_BG  = '\033[43m'     # Makes the background of the text 'yellow'
    BLUE_BG    = '\033[44m'     # Makes the background of the text 'blue'
    PURPLE_BG  = '\033[45m'     # Makes the background of the text 'purple'
    CYAN_BG    = '\033[46m'     # Makes the background of the text 'cyan'
    WHITE_BG   = '\033[47m'     # Makes the background of the text 'white'

    # COMMONLY USED COMBOS
    WARNING = BOLDER + BLACK + YELLOW_BG    # Used for 'Warnings'   -- Bold, Black Text with Yellow Background
    ERROR = BOLDER + RED_BG                 # Used for 'Errors'     -- Bold Text with Red Background

    
    
    
    