# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import atan2, degrees
ab = int(input())
bc = int(input())
print(f'{abs(round(degrees(atan2(ab,bc))))}\xb0')
