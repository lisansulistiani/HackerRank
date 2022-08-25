# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b = int(input()), int(input())
dm = divmod(a,b)
print(f'{dm[0]}\n{dm[1]}\n{dm}')