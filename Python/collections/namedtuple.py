# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
# id, marks, class, name
# average marks (sum marks/total student)
N =int(input())
column_name = input().split()
Student = namedtuple('SAT',column_name)
total_sum = 0
for i in range(N):
    data = input().split()
    temp = Student(*data)
    total_sum += int(temp.MARKS)
print(total_sum/N)
    
