#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: zhanjunkai

import sys
import os
import getopt
import logging
import subprocess
import re
import csv
import openpyxl
import math
import pandas as pd

# GLOBAL VARIABLE CONFIG
src_cols = ['A', 'B', 'C', 'D']
dst_cols = ['O', 'P', 'Q', 'R']

# ====================================================================
# Function    : excel_letter2int(letter)
# Description : transform the letter to int number for column of excel
# ====================================================================
def excel_letter2int(letter):
    return openpyxl.utils.cell.column_index_from_string(letter)

# =============================================
# Function    : get_file_name(file_path)
# Description :
# =============================================
def get_file_name(file_path):
    
    temp = re.search(r'(\/*)(\w+)(?=\.)', file_path, re.I|re.M)
    if temp:
        logging.debug("The file_name is >>> " + temp.group(2))
        return temp.group(2)
    else:
        print("The file_name is in a wrong format. Please check it and try again")
        return "None"

# =============================================
# Function    : sh(cmd)
# Description : do cmd with bash shell
# ============================================= 
def sh(cmd):

    subprocess.call(cmd, shell=True)

# =============================================
# Function    : check_file(file_name)
# Description : check if the file exists
# ============================================= 
def check_file (file_name):

    if os.path.exists(file_name):
        return True
    else:
        print("The file: " + file_name + " is not found !!")
        sys.exit(0)

#---------------------------------------------------
# Function: excel_to_csv(excel_file)
# Description: Convert the excel file into csv file
#---------------------------------------------------
def excel_to_csv(excel_file, sheet_name, csv_name):

    data = pd.read_excel(excel_file, sheet_name, index_col = 0)
    data.to_csv(csv_name, encoding = 'utf-8')

#----------------------------------------------
# Function: auto_feedthrough()
# Description: 
#----------------------------------------------
def ft_first_blood(ft_cfg_file):

    global src_cols
    global dst_cols

    src_indexs = []
    for _ in src_cols:
        src_indexs.append(excel_letter2int(_) - 1)
    
    dst_indexs = []
    for _ in dst_cols:
        dst_indexs.append(excel_letter2int(_) - 1)

    all_focus_indexs = src_indexs + dst_indexs

    logging.debug(">>>>> SRC_INDEXS AS BELOW >>>>")
    logging.debug(src_indexs)
    logging.debug(">>>>> DST_INDEXS AS BELOW >>>>")
    logging.debug(dst_indexs)

    if check_file(ft_cfg_file):

        file_name   = get_file_name(ft_cfg_file)
        csv_name    = file_name + '.csv'
        ft_name     = file_name + '_FT.csv'
        excel_to_csv(ft_cfg_file, "Sheet1", csv_name)
        csv_content = csv.reader(open(csv_name, 'r'))

        # Generate the FT csv with real feedthrough signals
        with open(ft_name, 'w', newline = '') as ft_file:
            writer = csv.writer(ft_file)
            for csv_line in csv_content:
                find_toggle = False
                for i in range(len(all_focus_indexs)):
                    if csv_line[all_focus_indexs[i]] == '': break
                    if 'Unnamed' in csv_line[all_focus_indexs[i]]: break
                    if i == (len(all_focus_indexs) - 1): find_toggle = True
                if find_toggle:
                    writer.writerow(csv_line)

        # Extract the FT signal pairs from CSV to txt
        # sh('perl xxxxxxxx.pl ' + ft_name)

        # Replace the DUT hierarchy
        with open("signal_pair.txt", 'r') as infile:
            infile_lines = infile.readlines()
        with open("signal_pair.txt", 'w') as outfile:
            for _ in infile_lines:
                newline = re.sub(r'old', 'TBplatform.U_DUT_TOP.U_', _, count = 0)
                outfile.write(newline)

#----------------------------------------------
# Function: main()
# Description: run the main program
#----------------------------------------------
def main(argv):

    ft_cfg_file = ""

    logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
    # logging.disable(logging.DEBUG)

    try:
        opts, args = getopt.getopt(argv, "hf:", ["help", "cfg_file="])
        #? The opts is a list of the (option, value) tuple
        #? The args is the list of all the arguments including option and value
    except getopt.GetoptError:
        print("Hint1: auto_feedthrough.py -f <feedthrough_config_file>")
        sys.exit(2)

    logging.debug(opts)
    logging.debug(args)

    if len(opts) == 0 and len(args) == 0:
        print("Hint2: auto_feedthrough.py -f <feedthrough_config_file>")
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("Usage: auto_feedthrough.py -f <feedthrough_config_file>")
            sys.exit(0)
        elif opt in ("-f", "--cfg_file"):
            ft_cfg_file = arg

    logging.debug("auto_feedthrough is performing ...")
    ft_first_blood(ft_cfg_file)

    subenv_num = 4
    sp_num     = 2234
    split_size = int(math.ceil(sp_num / 4))
    for sp_index in range(sp_num):
        if sp_index < split_size: pass
        elif sp_index < 1 * split_size: pass
        elif sp_index < 2 * split_size: pass
        elif sp_index < 3 * split_size: pass
        else: pass



    #for sp_index in range(len(sp_num)):
    #    for subenv_index in range(subenv_num):
    #        pass



if __name__ == "__main__":
    main(sys.argv[1:]) # Pass the argument list to main function
