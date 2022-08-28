# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N = int(input())
od = OrderedDict()
for i in range(N):
    item = input().split()
    item_name = " ".join(item[0:-1])
    price = item[-1]
    if(item_name in od):
        od[item_name] += int(price)
    else:
        od[item_name] = int(price)
print("\n".join([item+" "+str(od[item]) for item in od]))