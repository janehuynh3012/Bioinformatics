# Input: Strings Pattern and Genome.
# Output: All starting positions in Genome where Pattern appears as a substring.
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)    
    return positions
    
Pattern = "ATAT"
Genome = "GATATATGCATATACTT"
print(PatternMatching(Pattern, Genome))
