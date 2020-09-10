# Input: A DNA string Pattern.
# Output: The reverse complement of Pattern.
def ReverseComplement(Pattern):
	Pattern	= Complement(Pattern) #	complement each letter in a string	  
	Pattern	= Reverse(Pattern) #reverse all	letters in a string
	return Pattern
def Reverse(Pattern):
	reverse = “ “ # create an empty string
	for char in Pattern:
		reverse = char + reverse # the string is reversed
	return reverse
def Complement(Pattern):
	complement = “ “
	basepair = {“A”:”T”, “T”:”A”, “C”:”G”, “G”:”C”}
	for char in Pattern:
		complement += basepair.get(char) # return the value for	basepair
	return complement
Pattern = "AAAACCCGGT"
print(ReverseComplement(Pattern))
