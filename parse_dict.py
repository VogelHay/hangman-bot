#!/bin/bash


from ast import Global
import platform
import time
import os

start = time.perf_counter()

def check_os():
    global operating_system
    operating_system = platform.system()
    print(operating_system)


def trim_dict(file_in, file_out):
    with open(file_out, 'w') as f:
        pass
    with open(file_in) as f:
        for line in f:
            word = line
            if len(word) < 18:
                with open(file_out, 'a') as file:
                    file.write(word)
    min_int = 4
    min_str = ''
    max_int = 0
    max_str = ''
    with open(file_out, 'r') as f:
        for line in f:
            word_len = len(line) - 1
            if word_len > max_int:
                max_int = word_len
                max_str = line
            if word_len <= min_int:
                min_int = word_len
                min_str = line

    end = time.perf_counter()
    print(f"Complete in {round(end - start, 4)} seconds.\nLongest string ({max_int}): {max_str}Shortest string ({min_int}): {min_str} ")

def divy_dict(dict):
    word_length = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen']
    word_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    len_dict = dict(zip(word_int, word_length))   

    with open(dict) as f:
        for w in len_dict:
            word_len = len(w) - 1
            if word_len == w:
                pass

def dict_init(trim):
    if os.path.exists(trim):
        if os.path.getsize(trim) == 0:
            print("Formatting dictionary...")
            trim_dict("dict.txt", "trimmed-dict.txt")
        else:
            print("Dictionary previously formatted. Continuing...")
            time.sleep(2)
    else:
        print("File not found. Creating now...")
        f = open("trimmed-dict.txt", 'x')

def main():
    check_os()
    dict_init("trimmed-dict.txt")
    divy_dict("trimmed-dict.txt")

main()

