def pattern_count(text,pattern):
	“””returns a count of occurrences of pattern in text string”””
	count = 0
	for i in range(0, len(text)-len(pattern)+1):
		if text[i:len(pattern)+i] == pattern:
			count += 1
	return count

def frequent_words(text, k):
	“””returns frequency array of k_mers in text”””
	frequent_patterns = []
	Count=[]
	for i in range(0, len(text)-k):
		pattern = text[i:(i+k)]
		Count.append((pattern_count(text,pattern),pattern))
	maxcount = max([i[0] for i in Count])
	for i in range(0, len(text)-k):
		frequent_patterns = [i[1] for i in Count if i[0] == maxcount] 
	return set(frequent_patterns)


def complement(seq):
	“””Returns the complement string of nucleotides in a sequence”””
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
    bases = list(seq) 
    bases = [complement[base] for base in bases] 
    return ''.join(bases)

def reverse_complement(s):
	“””returns the reverse complement of a nucleotide sequence”””
        return complement(s[::-1])

def pattern_local(text,pattern):
	“””returns the starting position(s) of pattern in text”””
	local = []
	for i in range(0, len(text)-len(pattern)+1):
		if text[i:len(pattern)+i] == pattern:
			local.append(i)
	locals = ' '.join(str(v) for v in local)
return locals

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
