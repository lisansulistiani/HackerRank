# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
inp = input().split()
print("\n".join(["".join(item) for item in sorted(combinations_with_replacement(sorted(inp[0]),int(inp[1])))]))
