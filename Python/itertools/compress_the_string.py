# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
for key, value in groupby(input()):
    print(f'({len(list(value))}, {key})',end=" ")
