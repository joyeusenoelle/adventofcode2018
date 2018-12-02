""" Advent of Code 2018

December 02, puzzle 2
"""

def main(lines):
	""" For each line, check to see if another line varies by only one character.

		There's an easy but expensive way to do this. I'll start with that
		and see if I can refine it later.
	"""
	
	for i, line in enumerate(lines):
		if i + 1 != len(lines):
			for word in lines[(i+1):]:
				diffs = 0
				idx = 0
				for j in range(len(line)):
					if line[j] != word[j]:
						diffs += 1
						idx = j
				if diffs == 1:
					print("Found a match: {} and {}".format(line, word))
					print("Matched value: {}".format("".join([word[:idx],word[(idx+1):]])))
					return

if __name__ == "__main__":
	lines = []
	with open("02in.txt","r") as f:
		for line in f:
			lines.append(line.strip())
	main(lines)