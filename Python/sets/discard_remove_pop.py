n = int(input())
s = set(map(int, input().split()))
com = int(input())
for i in range(com):
    stat = input().split()
    command, value = stat[0], stat[-1]
    if(command=="pop"):         
        s.pop()         
    elif(command=="remove"):
        s.remove(int(value))
    elif(command=="discard"):
        s.discard(int(value))
print(sum(s))