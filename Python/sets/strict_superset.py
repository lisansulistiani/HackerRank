# Enter your code here. Read input from STDIN. Print output to STDOUT
set_a = set(input().split())
N = int(input())
super_set = True
for item in range(N):
    set_temp = set(input().split())
    if(not set_a.issuperset(set_temp)):
        super_set = False
        break
    else:
        if(len(set_a)==len(set_temp)):
            super_set=False
            break
if(super_set):
    print(super_set)
else:
    print(super_set)