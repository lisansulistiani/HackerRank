# Enter your code here. Read input from STDIN. Print output to STDOUT

tc = int(input())
country = set()
for i in range(tc):
    country.add(input())
print(len(country))