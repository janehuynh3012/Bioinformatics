# Input: A Pattern and a Text
# Output: The number of occurences of the Pattern

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

Pattern = "AAA"
Text = "GACCATCAAAACTGATAAACTACTTAAAAATCAGT"

print(PatternCount(Text, Pattern))