#!/usr/bin/python3

# Author: zhanjunkai

import traceback
import logging

# ----------------------------------------------
# Function: add(op_A, op_B)
# Description: adder for operands > 0
# ----------------------------------------------
def add(op_A, op_B):
    if not isinstance(op_A, int):
        raise Exception("The operand A is not int type. ")
    elif not isinstance(op_B, int):
        raise Exception("The operand B is not int type. ")
    elif op_A < 0:
        raise Exception("The operand A is a negative number. ")
    elif op_B < 0:
        raise Exception("The operand B is a negative number. ")
    else:
        return op_A + op_B

# ----------------------------------------------
# Function: debug_demo()
# Description: a debug demo without print
# ----------------------------------------------
def debug_demo():

    # 1. use try and except and raise -------------------------------------------
    print("-------------------- 1. use try and except and raise ---------------")
    try:
        sum = add(op_A = 2, op_B = "Hello")
        print("The sum is " + str(sum))
    except Exception as err:
        print("An exception happend: " + str(err) + "\n") # Just print the error message

    # 2. use traceback ----------------------------------------------------------
    print("------------------- 2. use traceback for error trace ---------------")
    try:
        sum = add(op_A = -2, op_B = 3)
    except:
        print(traceback.format_exc()) # Print the error trace for debug

    # 3. use assertion which can kill the program right away --------------------
    # The developer can turn off assertion by option -O, e.g. python3 -O debug.py
    print("--------- 3. use assertion which can kill the program --------------")
    sum = add(op_A = 1, op_B = 4)
    assert sum > 0, "The value of sum is active, but we need a negative value!"
    print("Last words of the program ... but ... \n")

    # 4. use logging 
    print("--------------- 4. use logging for debugging -----------------------")

    logging.basicConfig(level=logging.INFO, format=" %(asctime)s - %(levelname)s - %(message)s")
    # logging.basicConfig(filename = "log.txt",level=logging.INFO, format=" %(asctime)s - %(levelname)s - %(message)s")
    # logging.disable(logging.WARNING) # TODO: can also turn off the info and debug logs 
    
    logging.info("The levels supported by logging are: debug/info/warning/error/critical.")
    logging.info("And the level priority is : critical > error > warning > info > debug. ")
    logging.info("So, if disable the high level log, then the less important logs will be masked")
    logging.info("Or set level in basicConfig, then will show the logs which are more important than it")
    
    logging.debug("Start 4: use logging which can control the debug message level")
    sum = 0
    for i in range(5):
        sum = sum + i
        logging.debug('i is ' + str(i) + ", sum is " + str(sum))
    logging.debug("End 4: logging end \n")

# ----------------------------------------------
# Function: main()
# Description: run the main program
# ----------------------------------------------
def main():
    debug_demo()


if __name__ == '__main__':
    main()
