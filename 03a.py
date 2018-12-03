""" Advent of Code

December 3, puzzle A
"""

import re

def main(lines):
	""" Find the number of overlapped cells in an NxN square.

		Given a list of claims in the format
		  #123 @ 4,5: 6x7
		where the first number is the claim number, the second number
		group is the x, y coordinates of the upper left corner, and
		the third number group is the x, y size of the rectanglular claim,
		find the number of cells in the square that have more than one
		claim attached to them.

		The first task is to find out how big the total square is!
		This will also verify that the regular expression works.
		Result: This cloth is exactly 1000 inches to a side.

		So: Generate a 1000x1000 table, one value for each cell.
		For each claim:
		  * If the cell is unoccupied, mark with "c"
		  * If the cell is occupied, mark with "X"
		Then iterate through the table and count the number of Xes.
	"""

	#                       grp 1      grp 2    grp 3     grp 4    grp 5
	pattern = re.compile("#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)")
	# maxsize, claim = 0, 0 # only need this for determining cloth size
	# Generate a 1000x1000 list of empty ("") cells using list comprehensions
	fabric = [["" for y in range(1000)] for x in range(1000)] # fabric[y][x] (it's backwards!)

	for line in lines:
		m = pattern.match(line)
		# because xleft and ytop are "distance from the edge", they're zero-indexed
		xleft, ytop, xwidth, yheight = int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))
		xright = xleft + xwidth
		ybottom = ytop + yheight
		for j in range(ytop, ybottom): # ranges include the first value but not the second
			for i in range(xleft, xright):
				if fabric[j][i] == "": # if the cell is unclaimed
					fabric[j][i] = "c" # claim it
				else:                  # otherwise
					fabric[j][i] = "X" # mark it X so we know it's contested

	# a helper function, isX, will return 1 if a cell is "X" and 0 if it's not.
	contested = sum([sum([isX(cell) for cell in line]) for line in fabric])
	print("There are {} contested cells.".format(contested))

	# Commenting out the "find the size of the cloth" code, but leaving it in for historical purposes
	# 	if xright > maxsize:
	# 		maxsize = xright
	# 		claim = int(m.group(1))
	# 	if ybottom > maxsize:
	# 		maxsize = ybottom
	# 		claim = int(m.group(1))
	# print("Cloth is {} inches square, thanks to claim {}".format(maxsize, claim))

def isX(cell):
	""" Returns 1 if the cell passed in contains "X", 0 otherwise.
	"""
	return 1 if cell == "X" else 0

if __name__ == "__main__":
	lines = []
	with open("03in.txt","r") as f:
		for line in f:
			lines.append(line.strip())
	main(lines)