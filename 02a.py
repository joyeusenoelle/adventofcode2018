""" Advent of Code 2018

December 02, puzzle 1
"""

def main(lines):
	""" For each line, count characters.

		If any character appears exactly twice, increment x2.
		If any character appears exactly three times, increment x3.
		Ignore any doubles or triples past the first set.
		At the end, multiply x2 by x3 to get the checksum.
	"""
	x2, x3 = 0, 0 # independent counters. Count how many lines had at least one pair/triplet
	for line in lines: # iterate over each line in the input file
		chars = {} # dictionary to hold character: count values (e.g. a:1, b:2) for the current line

		for char in line: # iterate over characters in each line
			if char in chars.keys(): # if we've seen the character before in this line
				chars[char] += 1 	 # increment its count in the dictionary by 1
			else:					 # but if we haven't
				chars[char] = 1		 # then add it to the dictionary

		gota2, gota3 = False, False  # Do we have at least one pair/triplet in the line?
		for k,v in chars.items():    # iterate over the dictionary
			if v == 2 and not gota2: # if the count is 2, we have a pair; if we didn't already have one, then
				x2 += 1				 # increment the "pair" counter by 1, and
				gota2 = True		 # track that we've seen one so we don't accidentally add any more
			if v == 3 and not gota3: # if the count is 3, we have a triplet; if we didn't already have one, then
				x3 += 1				 # increment the triplet counter by 1, and
				gota3 = True		 # track that we've seen one so we don't accidentally add any more

			if gota2 and gota3:		 # if at this point we've seen both a pair and a triplet,
				break				 # we don't need to check any more characters, so break the loop

	print("Totals: x2 {}, x3 {}".format(x2, x3)) # print our totals
	print("Checksum: {}".format(x2 * x3)) # print the totals multiplied, which is our checksum


if __name__ == "__main__":
	lines = [] # an empty list for the lines in the input file
	with open("02in.txt","r") as f: # open the file. "with" means we don't have to close it
		for line in f: # iterate over the lines in the input file
			lines.append(line.strip()) # strip the newline character, then add it to the list
	main(lines) # and pass the list to our main function.