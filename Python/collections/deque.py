# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
op = int(input())
for i in range(op):
    command = input().split()
    if(command[0]=="append"):
        d.append(command[-1])
    elif(command[0]=="appendleft"):
        d.appendleft(command[-1])
    elif(command[0]=="clear"):
        d.clear()
    elif(command[0]=="extend"):
        d.extend(command[-1])
    elif(command[0]=="extendleft"):
        d.extendleft(command[-1])
    elif(command[0]=="count"):
        d.count(command[-1])
    elif(command[0]=="pop"):
        d.pop()
    elif(command[0]=="popleft"):
        d.popleft()
    elif(command[0]=="remove"):
        d.remove(command[-1])
    elif(command[0]=="reverse"):
        d.reverse()
    elif(command[0]=="rotate"):
        d.rotate(command[-1])
print(*d)