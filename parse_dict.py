import time

start = time.perf_counter()

def trim_dict():
    with open("trimmed-dictionary", 'w') as d:
        pass
    with open("dictionary.txt", 'r') as f:
        for line in f:
            print(line)
            if len(line) < 18:
                #print(line)
                with open("trimmed-dictionary.txt", 'a') as n:
                    n.write(line)

'''min_int = 4
min_str = ''
max_int = 0
max_str = ''

with open("dictionary.txt", 'r') as f:
    word_length = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen']
    word_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    len_dict = dict(zip(word_int, word_length))
    #print(len_dict)
    


    for line in f:
        word_len = len(line) - 1
        for w in len_dict:
            if word_len == w:
                print(word_len)

        if word_len > max_int:
            max_int = word_len
            max_str = line
        if word_len <= min_int:
            min_int = word_len
            min_str = line

end = time.perf_counter()
print(f"Complete in {round(end - start, 4)} seconds.\nLongest string ({max_int}): {max_str}Shortest string ({min_int}): {min_str} ")'''

def main():
    trim_dict()
    with open("trimmed-dictionary.txt", 'r') as f:
        print(f.read())