#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: zhanjunkai

import sys
import os
import logging
import re
import getopt


#----------------------------------------------
# Function: macro_fix_diff()
# Description: 
#----------------------------------------------
def macro_fix_diff(in_file, temp_file, out_file):
    
    toggle = False

    infile = open(in_file, "r")
    tefile = open(temp_file, "r")
    oufile = open(out_file, "w")

    inlines = infile.readlines()
    telines = tefile.readlines()

    for _ in inlines:
        toggle = False
        if "`define" in _:
            temp = re.search(r'`define\s+(\w+)\s+(\d+)', _, re.I|re.M)
            macro_name = temp.group(1)
            macro_index = temp.group(2)
            logging.debug("Macro_name: " + macro_name + ", its index: " + str(macro_index))
            for te in telines:
                if "`define" in te:
                    temp_2   = re.search(r'`define\s+(\w+)\s+(\d+)', te, re.I|re.M)
                    te_index = temp_2.group(2)
                    if macro_index == te_index:
                        logging.debug("Update macro name with index: " + str(te_index))
                        oufile.write(te)
                        toggle = True
            if toggle == False:
                oufile.write(_)
                logging.warning("I find one new macro: " + macro_name + ", id: " + str(macro_index))  

    infile.close()
    oufile.close()
    tefile.close()


#----------------------------------------------
# Function: main()
# Description: run the main program
#----------------------------------------------
def main(argv):

    IN_FILE = ""
    TEMPLATE_FILE = ""
    OUT_FILE = ""

    logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
    logging.disable(logging.DEBUG)

    try:
        opts, args = getopt.getopt(argv, "hi:t:", ["help", "input=", "template="])
    except getopt.GetoptError:
        print("Usage 1: macro_fix_diff.py -i <file_name> -t <template_file>")
        sys.exit(1)
    
    logging.debug(opts)
    logging.debug(args)

    if (not "-i" in str(opts)) or (not "-t" in str(opts)):
        print("Usage 2: macro_fix_diff.py -i <file_name> -t <template_file>")
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("Usage 3: macro_fix_diff.pyt -i <file_name> -t <template_file>")
            sys.exit(0)
        elif opt in ("-i", "--input"):
            IN_FILE = arg
            temp = re.search(r'(\w+)\.(\w+)', IN_FILE, re.I|re.M)
            if temp:
                OUT_FILE = temp.group(1) + "_new." + temp.group(2)
            else:
                print("Please check the input file path with the whole file name ...")
                sys.exit(1)
        elif opt in ("-t", "--template"):
            TEMPLATE_FILE = arg

    
    logging.debug("macro_fix_diff is performing ...")
    logging.info("INPUT_FILE IS " + IN_FILE)
    logging.info("TEMPLATE_FILE IS " + TEMPLATE_FILE)
    logging.info("OUTPUT_FILE IS " + OUT_FILE)
    macro_fix_diff(IN_FILE, TEMPLATE_FILE, OUT_FILE)

if __name__ == "__main__":
    main(sys.argv[1:])
