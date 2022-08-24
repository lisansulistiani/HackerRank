def print_formatted(number):
    # your code goes here
    binary = bin(number)[2:]
    width = len(str(binary))
    
    for i in range(1,number+1):
        print(f'{str(i).rjust(width)} {str(oct(i)[2:]).rjust(width)} {hex(i)[2:].upper().rjust(width)} {bin(i)[2:].rjust(width)}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)