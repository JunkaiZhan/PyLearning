#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: zhanjunkai

import sys
import getopt
import logging

OUT_FILE_NAME = ""

# ----------------------------------------------
# Function: create_pydemo()
# Description: create the python demo file
# ----------------------------------------------
def create_pydemo():

    global OUT_FILE_NAME
    
    file = open(OUT_FILE_NAME + ".py", 'w')

    text = '#!/usr/bin/python3\n# -*- coding: UTF-8 -*-\n# Author: zhanjunkai\n\n'
    text += 'import sys\nimport os\nimport logging\n\n'
    text += '#----------------------------------------------\n'
    text += '# Function: ' + OUT_FILE_NAME + "()\n"
    text += '# Description: \n'
    text += '#----------------------------------------------\n'
    text += 'def ' + OUT_FILE_NAME + "():\n    pass\n\n"
    text += '#----------------------------------------------\n'
    text += '# Function: main()\n'
    text += '# Description: run the main program\n'
    text += '#----------------------------------------------\n'
    text += 'def main():\n'
    text += '\n    logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")\n'
    text += '    logging.disable(logging.DEBUG)\n\n'
    text += '    logging.debug(\"' + OUT_FILE_NAME + ' is performing ...\")\n'
    text += '    ' + OUT_FILE_NAME + "()\n\n"
    text += 'if __name__ == \"__main__\":\n'
    text += '    main()\n'

    file.write(text)
    file.close()

# ----------------------------------------------
# Function: main()
# Description: run the main program
# ----------------------------------------------
def main(argv):

    global OUT_FILE_NAME
    
    logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
    logging.disable(logging.DEBUG)

    try:
        opts, args = getopt.getopt(argv, "hn:", ["help", "name="])
        #? The opts is a list of the (option, value) tuple
        #? The args is the list of all the arguments including option and value
    except getopt.GetoptError:
        print("pylearning.py -n <file_name>")
        sys.exit(2)

    logging.debug(opts)
    logging.debug(args)

    if len(opts) == 0 and len(args) == 0:
        print("Usage: ./pylearning.py -n <file_name>")
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("Usage: ./pylearning.py -n <file_name>")
            sys.exit(0)
        elif opt in ("-n", "--name"):
            OUT_FILE_NAME = arg
    
    print("The OUT_FILE_NAME is ", OUT_FILE_NAME)
    create_pydemo()

if __name__ == "__main__":
    main(sys.argv[1:]) # Pass the argument list to main

