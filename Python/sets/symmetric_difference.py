# Enter your code here. Read input from STDIN. Print output to STDOUT
tc_a = int(input())
a = set(map(int,input().split()))
tc_b = int(input())
b = set(map(int,input().split()))
diff = list()
for item in a.difference(b):
    diff.append(item)
for item in b.difference(a):
    diff.append(item)
diff = sorted(diff)
for item in diff:
    print(item)