# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
inp = input().split()
for i in range(int(inp[1])):
    for combination in sorted(combinations(sorted(inp[0]), i+1)):
        print("".join(combination))
