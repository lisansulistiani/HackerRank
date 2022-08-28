# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n,m = input().split()
d = defaultdict(list)
for i in range(0,int(n)):
    d[input()].append(str(i+1))
for i in range(0,int(m)):
    x = input()
    if(x in d):
        print(" ".join(d[x]))
    else:
        print(-1)

