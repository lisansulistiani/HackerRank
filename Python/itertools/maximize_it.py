
from itertools import product
k, m = input().split()
s = 0
n = list()
for i in range(int(k)):
    n.append(list(map(int,input().split()[1:])))

s = []
for item in product(*n):
    temp = 0
    for i in item:
      temp+=pow(i,2)
    s.append(temp%int(m))

smax = max(s)
print(smax)