# A Python program to print all 
# permutations using library function 
from itertools import permutations 

# Get all permutations of [1, 2, 3] 
perm = permutations([1, 2, 3]) 

# Print the obtained permutations 
print("permutations...")
for i in list(perm): 
	print(i)

from itertools import combinations

t=combinations([1,2,3])
print("combinations..")
for i in list(t):
    print(i)