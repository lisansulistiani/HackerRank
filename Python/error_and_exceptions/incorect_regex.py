# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
tc = int(input())
for i in range(0,tc):
    pattern = input()
    try:
        re.match(pattern,pattern)
        print(True)
    except Exception as e:
        print(False)
