if __name__ == '__main__':
    N = int(input())
    lists = list()
    for _ in range(N):
        stat = input().split()
        command = stat[0]
        if(len(stat)!=1):
            idx = int(stat[1])
            val = int(stat[-1])
        if("insert" in command):
            lists.insert(idx,val)
        elif("print" in command):
            print(lists)
        elif("remove" in command):
            lists.remove(val)
        elif("append" in command):
            lists.append(val)
        elif("sort" in command):
            lists = sorted(lists)
        elif("pop" in command):
            lists.pop(-1)
        elif("reverse" in command):
            lists.reverse()
