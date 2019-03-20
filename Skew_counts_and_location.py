def skew_count(genome):
	“””Return the skew counts of k-mers from 1 to length of genome”””
	skew = []
	if genome[0] ==  'G':
		skew.append(1)
	elif genome[0] =='C':
		skew.append(-1)
	else:
		skew.append(0)
	for j in range(1, len(genome)):
		if genome[j] ==  'G':
			skew.append(skew[j-1]+1)
		elif genome[j] == 'C':
			skew.append(skew[j-1]-1)
		else:
			skew.append(skew[j-1])
	return skew

def skew_min_local(genome):
	“””returns a list of starting points of minimum skew counts in genome”””
	x=skew_count(genome)
	y = min(x)
	local =[]
	for key, value in enumerate(x):
		if value == y:
			local.append(key+1)
	return local
