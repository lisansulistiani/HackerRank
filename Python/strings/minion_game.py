import re
def minion_game(string):
    # your code goes here
    vowels = ['A','I','U','E','O']
    i=1
    stuart_score = 0
    kevin_score = 0
    temp = list(set([string[i: j] for i in range(len(string))
          for j in range(i + 1, len(string) + 1)]))
    # print(temp)
    # RESULTING TLE
    for item in temp:
        if(item[0] in vowels):
            kevin_score += len(re.findall(f'(?={item})',string))
        else:
            stuart_score += len(re.findall(f'(?={item})',string))
    # THE CORRECT ANSWER: https://www.chase2learn.com/the-minion-game-in-python-hackerrank-solution/
    # str_len = len(string)
    # for i in range(str_len):
    #     if s[i] in vowels:
    #         kevin_score += (str_len)-i
    #     else :
    #         stuart_score += (str_len)-i
    if(stuart_score==kevin_score):
        print("Draw")
    elif(stuart_score>kevin_score):
        print(f"Stuart {stuart_score}")
    else:
        print(f"Kevin {kevin_score}")

if __name__ == '__main__':
    s = input()
    minion_game(s)