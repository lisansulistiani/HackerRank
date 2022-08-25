# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
student_n = set(input().split())
b = int(input())
for i in range(b):
    command = input().split()
    temp = set(input().split())    
    if(command[0]=="intersection_update"):
        student_n.intersection_update(temp)
    elif(command[0]=="update"):
        student_n.update(temp)
    elif(command[0]=="symmetric_difference_update"):
        student_n.symmetric_difference_update(temp)
    elif(command[0]=="difference_update"):
        student_n.difference_update(temp)
    # print(student_n)
print(sum(set(map(int,student_n))))
