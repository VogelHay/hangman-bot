#!/bin/bash


import platform
import time
import os

start = time.perf_counter()

def check_os():
    global operating_system
    operating_system = platform.system()
    #print(operating_system)


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

def dict_init(trim):
    if os.path.exists(trim):
        if os.path.getsize(trim) == 0:
            print("Formatting dictionary...")
            trim_dict("dict.txt", "trimmed-dict.txt")
        else:
            print("Dictionary previously formatted. Continuing...")
            time.sleep(1)
    else:
        print("File not found. Creating now...")
        f = open("trimmed-dict.txt", 'x')

def subdict_init():
    print('Starting subdictionary config!')
    os.makedirs('subdicts', exist_ok=True)
    subdicts = ('three.txt', 'four.txt', 'five.txt', 'six.txt', 'seven.txt', 'eight.txt', 'nine.txt', 'ten.txt', 'eleven.txt', 'twelve.txt', 'thirteen.txt', 'fourteen.txt', 'fifteen.txt', 'sixteen.txt')
    for x in subdicts:
        path = f"subdicts/{x}"
        if os.path.exists(path):
            pass
        else:
            print("File not found. Creating now...")
            #f = open(x, "x")
            with open(path, "w", encoding="utf-8"):
                pass
            print(f"The following file has been created: {x}")
            time.sleep(1)

# Function that takes the selected word and its length and appends it to the appropriately lettered dict
def num_dict(length, word):
    file = f"subdicts/{length}.txt"
    with open(file, 'r') as f:
        if word in file:
            print(f"{word} found!")
            return
    with open(file, "a") as f:
        f.write(word)
        print(f"{word} added!")
    pass


# Determines length of str and directs towards specific dict
def divy_dict(trim):
    print("Sorting library...")
    word_length = ['three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen']
    word_int = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    len_dict = dict(zip(word_int, word_length))   

    with open(trim) as f:
        for line in f:
            length = len(line) - 1
            #print(length)
            for x in len_dict:
                if length == x:
                    num_dict(len_dict[x], line)
                pass
            '''word = line
            for x in len_dict:
                #print(line)
                if len(word) == len_dict.get(x):
                    num_dict(len_dict.get(x), word)
                    print("written to file")
                else:
                    pass'''


            
def main():
    check_os()
    dict_init("trimmed-dict.txt")
    subdict_init()
    divy_dict("trimmed-dict.txt")

main()

