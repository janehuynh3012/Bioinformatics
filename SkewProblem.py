# Problem: Find a position in a genome where the skew diagram attains a minimum.
# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values
# of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = [] # output variable 
    array = SkewArray(Genome) 
    m = min(array)  
    for i in range(len(array)): # range over the length of the skew array and add all positions achieving 
                                # the min to positions
        if array[i] == m:
            positions.append(i)
    return positions

# Input:  A String Genome
# Output: SkewArray(Genome)
def SkewArray(Genome):
    Skew = [0]
    for i in range(len(Genome)):
        if Genome[i] == 'C':
            Skew.append(Skew[i] - 1)
        elif Genome[i] == 'G':
            Skew.append(Skew[i] + 1)
        else:
            Skew.append(Skew[i])
    return Skew

Genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
print(MinimumSkew(Genome))