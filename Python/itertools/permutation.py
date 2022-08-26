# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
inp = input().split()
list_permutation = sorted(["".join(item) for item in permutations(inp[0],int(inp[1]))])
print("\n".join(list_permutation))