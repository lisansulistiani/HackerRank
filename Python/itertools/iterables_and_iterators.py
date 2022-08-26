# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
n = int(input())
arr = input().split()
k = int(input())
c = combinations(arr,k)
atas = 0
bawah = 0
for item in c:
    if('a' in item):
        atas+=1
    bawah+=1
print(f'{atas/bawah}')
