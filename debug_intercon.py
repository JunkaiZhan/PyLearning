#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: zhanjunkai

import sys
import re
import os
import logging

#----------------------------------------------
# Function: get_uvm_error_list()
# Description: 
#----------------------------------------------
def get_uvm_error_list(log_file, item):

    log_f = open(log_file, 'r')
    log_lines = log_f.readlines()

    return_list = []
    for _ in range(len(log_lines)):
        if "UVM_ERROR" in log_lines[_]:
            if item == "intercon":
                return_list.append(log_lines[_])
            else:
                return_list.append(log_lines[_] + log_lines[_ + 1])

    return return_list

#----------------------------------------------
# Function: get_failed_log_list()
# Description: 
#----------------------------------------------
def get_failed_log_list(status_file):
    
    status_f = open(status_file, 'r')
    status_lines = status_f.readlines()

    return_list = []
    for _ in status_lines:
        if "fail" in _ and "log" in _:
            temp = re.search(r'\w+\.log', _, re.I|re.M)
            if temp:
                log_file = temp.group()
                return_list.append(log_file)
    
    return return_list

#----------------------------------------------
# Function: debug_intercon()
# Description: 
#----------------------------------------------
def debug_intercon(item):

    status_file = "../../../../bin/ci/" + item + "/sim/regress_status.log"
    log_path    = "../../../../bin/ci/" + item + "/sim/pre_sim/log/"

    log_list = get_failed_log_list(status_file)
    for _ in log_list:
        logging.debug("\n>>>>>> Process log file: " + _)
        uvm_error_list = get_uvm_error_list(log_path + _, item)
        for error_message in uvm_error_list:
            if item == "intercon":
                print(error_message)
            else:
                print(error_message + "\n")


#----------------------------------------------
# Function: main()
# Description: run the main program
#----------------------------------------------
def main(item):

    logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
    logging.disable(logging.DEBUG)

    logging.debug("debug_intercon is performing ...")
    debug_intercon(item)

if __name__ == "__main__":
    main("intercon")
