#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: zhanjunkai

import os
import sys
import time

from progress.bar import IncrementalBar
from progress.bar import ChargingBar
from progress.bar import FillingCirclesBar
from progress.bar import ShadyBar
from alive_progress import alive_bar
from tqdm import tqdm


# Plot process bar using different method -------------------
def plot_bar():

    # Method 0: Using \r to print
    def view_bar(num, sum, bar_title = "Processing", bar_word = "▓"):
        rate = num / sum
        rate_num = round(rate * 100)
        rest_num = 100 - rate_num
        print(("\r\033[1;32m" + bar_title + " \033[0m\033[1;35m|" + bar_word *  rate_num 
            + " " * rest_num + "| \033[0m\033[1;33m%3d%%\033[0m") % (rate_num), end = "")
        if rate_num == 100: print("\n", end = "")
    
    with open("plot_statistic.py", 'r') as file:
        lines = file.readlines()
        for _ in range(len(lines)):
            time.sleep(0.02)
            view_bar(_, len(lines) - 1)

    # Method 1: Using alive_progress <<<
    with alive_bar(100) as bar:
        for _ in range(100):
            bar()
            time.sleep(0.02)

    # Method 2: Using tqdm <<<
    with open("plot_statistic.py", 'r') as file:
        lines = file.readlines()
        for _ in tqdm(lines):
            time.sleep(0.02)

    # Methods 3: Using Progress <<<
    with open("plot_statistic.py", "r") as file:
        lines = file.readlines()
        # bar   = IncrementalBar('BarName', max = len(lines))
        # bar   = ChargingBar('BarName', max = len(lines))
        bar   = FillingCirclesBar('BarName', max = len(lines))
        # bar   = ShadyBar('BarName', max = len(lines))
        for _ in lines:
            bar.next()
            time.sleep(0.02)
        bar.finish()
    
    with open("plot_statistic.py", "r") as file:
        lines = file.readlines()
        bar   = ChargingBar('BarName', max = len(lines))
        for _ in lines:
            bar.next()
            time.sleep(0.02)
        bar.finish()

    with open("plot_statistic.py", "r") as file:
        lines = file.readlines()
        bar   = ShadyBar('BarName', max = len(lines))
        for _ in lines:
            bar.next()
            time.sleep(0.02)
        bar.finish()


# Program entry ---------------------------------------------
if __name__ == "__main__":
    plot_bar()
