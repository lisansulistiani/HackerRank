def print_rangoli(size):
    # your code goes here
    list_pattern = list()
    for i in range(0,size*2-1):
        temp = size
        alph = chr(96+temp)
        pattern = ""
        if(i<size):
            uk = i*2+1
            for k in range(0,uk,1):
                pattern += alph
                if(k<uk//2):
                    temp-=1
                else:
                    temp+=1
                alph = chr(96+temp)
            list_pattern.append(pattern)
            print("-".join(list(pattern)).center((size*4)-3,"-"))
            if(len(list_pattern)==size):
                list_pattern.pop()
        else:
            pattern = list_pattern.pop()
            print("-".join(list(pattern)).center((size*4)-3,"-"))
            

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)