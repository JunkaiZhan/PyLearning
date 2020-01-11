#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: zhanjunkai

import argparse
import logging
import math
import re

# CONFIG OPT NUM --------------------------------------------------------
options_num = 3

# Get the line number of the file_path ----------------------------------
def get_line_num (file_path):
    with open(file_path, 'r') as f:
        return len(f.readlines()) 


# Get file name from the file path --------------------------------------
def get_file_name(file_path):
    return re.search(r"\w+(?=\.)", file_path, re.I|re.M).group()


# Plot the percentage on terminal ---------------------------------------
def plot_percentage(name, cover, all):
    
    perc   = cover / all
    cperc  = int(round(100.0 * perc))
    ncperc = 100 - cperc

    # print("-" * 130)
    print("\033[1;32m" + name + "\033[0m"+ " \033[1;33m[" + "#" * cperc + " " * ncperc + "]\033[0m" + 
        "\033[1;32m  %.2f %%  " % (perc * 100.0) + " FROM %d/%d\033[0m" % (cover, all))
    # print("-" * 130)


# Plot and show the MISC checking result --------------------------------
def plot_statistic(kwargv):

    # Calculate the option number
    opts_num    = math.ceil(len(kwargv) / 2)

    # Create the cover to linenum dict and all to linenum dict
    cover_dict = {}
    all_dict   = {}
    file_name_dict = {}
    for i in range(opts_num):
        cover_dict["cover" + str(i)] = get_line_num( kwargv["cover" + str(i)] )
        all_dict["all" + str(i)] = get_line_num( kwargv["all" + str(i)] )
        file_name_dict["name" + str(i)] = get_file_name( kwargv["all" + str(i)] )

    # Print the dict content
    for key, value in cover_dict.items():
        logging.debug("File: {0} has {1} lines".format(key, value))
    for key, value in all_dict.items():
        logging.debug("File: {0} has {1} lines".format(key, value))

    # Plot percentage on terminal
    for i in range(opts_num):
        plot_percentage(file_name_dict["name" + str(i)], cover_dict["cover" + str(i)], all_dict["all" + str(i)])

if __name__ == "__main__": # ----------------------------------------------------------------------

    logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
    logging.disable(logging.DEBUG)
    
    options = argparse.ArgumentParser()

    # Get arguments from command
    for i in range(options_num):
        stri = str(i)
        options.add_argument("-c" + stri, "--cover" + stri, type = str, required = True)
        options.add_argument("-a" + stri, "--all" + stri, type = str, required = True)

    # Transform the args from Namespace object to dict
    args = options.parse_args()
    opts_dict = vars(args)

    # Print the arguments we get 
    for key, value in opts_dict.items():
        logging.debug("Argument: {0} 's value is {1}".format(key, value))    

    plot_misc(opts_dict)
    