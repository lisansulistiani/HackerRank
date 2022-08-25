# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
k = int(input())
rooms = input().split()
room = Counter(rooms)
print([item for item in room if(room[item]==1)][0])