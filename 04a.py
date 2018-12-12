import re

def main(lines):
	""" Sort the input by date/time, then find the best guard/minute combination

		Note: the example answer is WRONG!
	"""
	# [1518-09-25 00:28] falls asleep
	# Don't actually care about the year, since it's always the same
	#							   grp1	 grp2	 grp3	 grp4	   grp5
	pattern = re.compile("\[[0-9]+-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+)\] (.+)")
	guardptn = re.compile("Guard #([0-9]+) begins shift")

	entries = []
	guards = {}

	for line in lines:
		m = pattern.match(line)
		g = guardptn.match(m.group(5))
		guard = -1 if g == None else int(g.group(1))
#						guard 	   # month			# day			 # hour			  # minute	   # activity
		entries.append([guard, int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), m.group(5)])
	entries.sort(key = lambda x: (x[1], x[2], -x[3], x[4]))
	for i in range(1, len(entries)):
		if entries[i][0] == -1:
			entries[i][0] = entries[i-1][0]
	with open("04out.txt", "w") as ofile:
		for entry in entries:
			ofile.write("{}\n".format(entry))
	# so entries is
	#  [0,	     1,	     2,	   3,	  4,	   5]
	#  #guard  # month  #day  #hour  #minute  #activity
	stt = -1
	end = -1
	for i in range(1,len(entries)):
		sleeping = False
		cguard = entries[i][0]
		#print(cguard)
		if cguard == entries[i-1][0]:
			if entries[i][5] == "falls asleep":
				stt = entries[i][4]
				#print("{} fell asleep at {}".format(cguard, stt))
				sleeping = True
			elif entries[i][5] == "wakes up":
				end = entries[i][4]
				sleeping = False
				#print("{} woke up at {} (fell asleep at {})".format(cguard, end, stt))
				for q in range(stt, end):
					if cguard not in guards.keys():
						guards[cguard] = {}
						guards[cguard][q] = 1
					else:
						if q not in guards[cguard].keys():
							guards[cguard][q] = 1
						else:
							guards[cguard][q] = guards[cguard][q] + 1
		else:
			stt = -1
			end = -1

	gslp = {}
	for k,v in guards.items():
		maxsleeps = 0
		maxmin = 0
		for minute, sleeps in v.items():
			if sleeps > maxsleeps:
				maxsleeps = sleeps
				maxmin = minute
		print("{} slept the most times ({}) at minute {}".format(k, maxsleeps, maxmin))
		gslp[k] = [maxmin, maxsleeps]

	tguard, tmin, tsleeps = 0, 0, 0
	for k,v in gslp.items():
		if v[1] > tsleeps:
			tguard, tmin, tsleeps = k, v[0], v[1]

	print("Guard {} slept the most times ({}) at minute {}. ID * minute = {}!".format(tguard, tsleeps, tmin, tguard*tmin))

def add_sleeping(dct, mins):
	pass

if __name__ == "__main__":
	lines = []
	with open("04in.txt","r") as f:
		for line in f:
			lines.append(line.strip())
	main(lines)