# Enter your code here. Read input from STDIN. Print output to STDOUT

N,M = map(int,input().split())
for i in range(N):
    if(i==N//2):
        print("WELCOME".center(M,"-"))
    else:
        if(i<(N//2)):
            print((".|."*(i*2+1)).center(M,"-"))
        elif(i>(N//2)):
            print((".|."*((N-i)*2-1)).center(M,"-"))