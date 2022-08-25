# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
nm = input().split()
arr = input().split()
a = set(input().split())
b = set(input().split())

happiness = 0
happy = a.intersection(arr)
sad = b.intersection(arr)
for item in arr:
    if item in happy: happiness+=1
    elif(item in sad): happiness-=1
print(happiness)
