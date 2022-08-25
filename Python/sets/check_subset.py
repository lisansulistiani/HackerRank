# Enter your code here. Read input from STDIN. Print output to STDOUT
tc = int(input())
for i in range(tc):
    a, set_a = int(input()), set(input().split())
    b, set_b = int(input()), set(input().split())
    if(set_b.intersection(set_a)==set_a):
        print(True)
    else:
        print(False)