""" Advent of Code Day 5b

"""

from collections import defaultdict

def comp(s1,s2):
	if (s1 != s2) and s1.lower() == s2.lower():
		return True
	return False

def main(polymer):
	opoly = polymer
	lens = defaultdict(int)
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for char in alphabet:
		polymer = "".join(opoly.split(char))
		polymer = "".join(polymer.split(char.upper()))
		do_it = True
		while do_it:
			olen = len(polymer)
#			print(olen)
			for acter in alphabet:
				if acter != char:
					polymer = "".join(polymer.split("{}{}".format(acter, acter.upper())))
					polymer = "".join(polymer.split("{}{}".format(acter.upper(), acter)))
					print("with {}, after {}, len(polymer) is {}".format(char, acter, len(polymer)))
#			for i in range(len(polymer)-1):
#				if comp(polymer[i], polymer[i+1]):
#					if i == 0: # the first two are a match
#						polymer = polymer[2:]
#					elif i == (olen - 2): # the last two are a match
#						polymer = polymer[:-2]
#					else: # the match is in the middle
#						polymer = polymer[:i] + polymer[i+2:]
#					break
			if olen == len(polymer): # we didn't reduce polymer's length at all
				do_it = False # no more matches, stop looping
		lens[char] = len(polymer)
		with open("05out.txt","a") as ofile:
			ofile.write("{}: {}\n".format(char, len(polymer)))
	for k,v in lens.items():
		print("{}: {}".format(k,v))


if __name__ == "__main__":
	inline = ""
	with open("05in.txt","r") as ofile:
		inline = ofile.read().strip()
	main(inline)