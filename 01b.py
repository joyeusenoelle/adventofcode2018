# Advent of Code 2018
# December 01, puzzle 1

import sys

def main(args):
    freqlist = [0]
    found = False
    cycles = 0
    arglist = args.split(",")
    arglist = [x.strip() for x in arglist]
    freq = 0
    while not found:    
        cycles += 1
        for item in arglist:
            if item[0] == "+":
                freq += int(item[1:])
            elif item[0] == "-":
                freq -= int(item[1:])
            if freq in freqlist:
                return freq
            freqlist.append(freq)
        if cycles == 1000000:
            return "I haven't found a duplicate after a million cycles."

if __name__ == "__main__":
    args = input("Paste the modulations here: ")
    print(main(args))
