#!/usr/bin/python3

# Author: zhanjunkai

#----------------------------------------------
# Function: add(op_A, op_B)
# Description: adder for operands > 0
#----------------------------------------------
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

#----------------------------------------------
# Function: debug_demo()
# Description: a debug demo without print
#----------------------------------------------
def debug_demo():

    # 1. use try and except and raise -----------------
    try:
        sum = add(op_A = -2, op_B = 8)
        print("The sum is " + str(sum))
    except Exception as err:
        print("An exception happend: " + str(err))
    

#----------------------------------------------
# Function: main()
# Description: run the main program
#----------------------------------------------
def main():
    debug_demo()

if __name__ == '__main__':
    main()