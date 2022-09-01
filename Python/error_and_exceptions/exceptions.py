# Enter your code here. Read input from STDIN. Print output to STDOUT
tc = int(input())
for i in range(tc):
    a,b = input().split()
    try:
        print(int(a)//int(b))
    except Exception as e:
        print(f'Error Code: {e}')
    ### or
    # except ZeroDivisionError as e:
        # print(f'Error Code: {e}')
    # except ValueError as e:
        # print(f'Error Code: {e}')