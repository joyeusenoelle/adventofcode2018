""" Advent of Code 2018

December 02, puzzle 2
"""

def main(lines):
	""" For each line, check to see if another line varies by only one character.

		There's an easy but expensive way to do this. I'll start with that
		and see if I can refine it later.
	"""
	# Testing a new implementation (should be O(n log n))
	#
	# lines.sort()
	# for i, line in enumerate(lines):
	# 	if i + 1 != len(lines):
	# 		word = lines[i+1]
	# 		diffs = 0
	# 		idx = 0
	# 		for j in range(len(line)):
	# 			if line[j] != word[j]:
	# 				diffs += 1
	# 				idx = j
	# 		if diffs == 1:
	# 			print("Found a match: {} and {}".format(line, word))
	# 			print("Matched value: {}".format("".join([word[:idx],word[(idx+1):]])))
	# 			return

	# Original implementation kept for reference (O(n^2))
	#
	for i, line in enumerate(lines): # enumerate gives us an index and the value at that index
		if i + 1 != len(lines): # don't overflow the list
			for word in lines[(i+1):]: # only check lines further down the list
				diffs = 0 # track the number of differences between lines
				idx = 0 # track the index of the most recent difference
				for j in range(len(line)): # iterate over the length of a word (they're all the same length)
					if line[j] != word[j]: # if this character in the first word is different from the same character in the second
						diffs += 1 # increment the number of differences by 1
						idx = j # set the difference index equal to the current iteration index
				if diffs == 1: # if we only found one difference
					print("Found a match: {} and {}".format(line, word)) # print the matched words
					print("Matched value: {}".format("".join([word[:idx],word[(idx+1):]]))) # print the matching (NOT non-matching) letters
					return

if __name__ == "__main__":
	lines = [] # an empty list for the lines in the input file
	with open("02in.txt","r") as f: # open the file. "with" means we don't have to close it
		for line in f: # iterate over the lines in the input file
			lines.append(line.strip()) # strip the newline character, then add it to the list
	main(lines) # and pass the list to our main function.