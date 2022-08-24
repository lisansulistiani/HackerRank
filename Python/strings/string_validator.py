if __name__ == '__main__':
    s = input()
    print(any(char.isalnum() for char in list(s)))
    print(any(char.isalpha() for char in list(s)))
    print(any(char.isdigit() for char in list(s)))
    print(any(char.islower() for char in list(s)))
    print(any(char.isupper() for char in list(s)))
