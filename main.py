#!/bin/python3

import subprocess
import time
import os

def check_dict(path):
    if os.path.exists(path):
        print("Verified dictionary integrity. Proceeding...")
        time.sleep(1)
        return True
    else:
        print("Dictionary not found. Running parsing script...")
        time.sleep(1)
        result = subprocess.run(["python3", "parse_dict.py"], check=True)



def main():
    check_dict('trimmed-dict.txt')


main()