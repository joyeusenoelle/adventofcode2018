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
	x2, x3 = 0, 0
	for line in lines:
		chars = {}
		gota2, gota3 = False, False
		for char in line:
			if char in chars.keys():
				chars[char] += 1
			else:
				chars[char] = 1
		for k,v in chars.items():
			if v == 2 and not gota2:
				x2 += 1
				gota2 = True
			if v == 3 and not gota3:
				x3 += 1
				gota3 = True
			if gota2 and gota3:
				break
	print("Totals: x2 {}, x3 {}".format(x2, x3))
	print("Checksum: {}".format(x2 * x3))


if __name__ == "__main__":
	lines = []
	with open("02in.txt","r") as f:
		for line in f:
			lines.append(line.strip())
	main(lines)