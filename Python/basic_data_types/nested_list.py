if __name__ == '__main__':
    ns = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ns[name]=score
    ns = dict(sorted(ns.items(), key=lambda item: (-item[1], item[0])))
    des = list(sorted(set(ns.values()),reverse=True))[-2]
    for item in ns:
        if(ns[item]==des):
            print(item)
