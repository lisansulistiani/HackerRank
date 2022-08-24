def merge_the_tools(string, k):
    # your code goes here
    list_subs = [string[i:i+k] for i in range(0,len(string),k)]
    for item in list_subs:
        print(''.join(sorted(set(item), key=item.index)))
    # print("\n".join(new_list_subs))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)