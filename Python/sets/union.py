# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
student_n = set(input().split())
b = int(input())
student_b = set(input().split())
print(len(student_b.union(student_n)))