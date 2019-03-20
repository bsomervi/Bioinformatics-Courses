def ClumpFinding(genome, k, L, t):
	“””Returns frequent k-mers of length K appearing t or more times in L length segment of genome”
    frequent_patterns = []
    clump= [0 for i in range(4**k)]
    text = genome[0:L] 
    frequency_array = computing_frequencies(text, k)
    
    for i in range(0, 4**k):
        if frequency_array[i] >= t:
            clump[i] = 1
    
    for i in range(1, len(genome)-L):
        first = genome[i-1:i+k-1]
        index = pattern_to_number(first)
        frequency_array[index] = frequency_array[index] - 1
        last = genome[i+L-k:i+L]
        index = pattern_to_number(last)
        frequency_array[index] = frequency_array[index] + 1
        if frequency_array[index] >= t:
            clump[index] =  1
    
    for i in range(0, 4**k):
        if clump[i] == 1:
            pattern = number_to_pattern(i, k)
            frequent_patterns.append(pattern)
    
    return frequent_patterns

def computing_frequencies(text, k):
	“””returns a frequency array of k-mers k long appearing in text”””
	frequency_array= [0 for i in range(4**k)]
	for i in range(0, len(text)-k+1):
		pattern = text[i:i+k]
		j = pattern_to_number(pattern)
		frequency_array[j] = frequency_array[j] + 1
	return frequency_array


def pattern_to_number(text):
	“””Converts nucleotide string to a number in base 10”””
	for x, y in {'A':'00','C':'01', 'G':'10', 'T':'11'}.items():
		text = text.replace(x,y)
	num= int(text, 2)
	return num

def number_to_pattern(index, k):
	“”””converts nucleotide number to string”””
	number_to_symbol = {0 : 'A', 1 : 'C', 2 : 'G', 3 : 'T'}
  if k==1:
		return number_to_symbol[index]
	prefixindex = index//4
	symbol =number_to_symbol[(index % 4)] 
	prefix_pattern = number_to_pattern(prefixindex, k-1)
	return prefix_pattern + symbol
