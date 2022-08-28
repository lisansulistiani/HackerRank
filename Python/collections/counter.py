# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x = int(input())
shoes = list(map(int,input().split()))
shoes_counter = Counter(shoes)
n = int(input())
total_price = 0
for i in range(n):
    shoe_size,price = input().split()
    if(int(shoe_size) in shoes_counter and shoes_counter[int(shoe_size)]!=0):
        shoes_counter[int(shoe_size)]-=1
        total_price+=int(price)
print(total_price)

## ALTERNATIVE
# n = int(input())
# total_price = 0
# for i in range(n):
#     shoe_size,price = input().split()
#     if(int(shoe_size) in shoes):
#         shoes.remove(int(shoe_size))
#         total_price+=int(price)
# print(total_price)