""" Advent of Code

December 3, puzzle B
"""

import re

def main(lines):
	""" Find the one claim that DOESN'T overlap in an NxN square.

		Given a list of claims in the format
		  #123 @ 4,5: 6x7
		where the first number is the claim number, the second number
		group is the x, y coordinates of the upper left corner, and
		the third number group is the x, y size of the rectanglular claim,
		find the number of cells in the square that have more than one
		claim attached to them.

		So: Generate a 1000x1000 table, one value for each cell.
		For each claim:
		  * If the cell is unoccupied, mark with "c"
		  * If the cell is occupied, mark with "X"
		Then cycle through the claims AGAIN. For each claim:
		  * If any of its cells are marked "X", continue.
		  * If ALL its cells are marked "c", that's my claim; report it!

	"""

	#                       grp 1      grp 2    grp 3     grp 4    grp 5
	pattern = re.compile("#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)")

	# Generate a 1000x1000 list of empty ("") cells using list comprehensions
	fabric = [["" for y in range(1000)] for x in range(1000)] # fabric[y][x] (it's backwards!)

	# first cycle, to mark claims
	for line in lines:
		m = pattern.match(line)
		claim = int(m.group(1))
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

	# second cycle, to check claims
	for line in lines:
		m = pattern.match(line)
		claim = int(m.group(1))
		xleft, ytop, xwidth, yheight = int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))
		xright = xleft + xwidth
		ybottom = ytop + yheight
		contested = False
		for j in range(ytop, ybottom): # ranges include the first value but not the second
			for i in range(xleft, xright):
				if fabric[j][i] == "X": # if the cell is contested
					contested = True    # oh well
					break			    # break out
										# otherwise continue

		if contested == False:
			print("Claim {} does not overlap!".format(claim))
			return

# (I don't need isX anymore.)

if __name__ == "__main__":
	lines = []
	with open("03in.txt","r") as f:
		for line in f:
			lines.append(line.strip())
	main(lines)