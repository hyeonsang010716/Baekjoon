import sys
from collections import deque
input = sys.stdin.readline

def check(number):
    l = set(list(str(number))) - {'1' , '0'}
    if l : return False
    else: return True



for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
        continue
    d = deque()
    temp_list = []
    visited = [set() for _ in range(100)]
    for i in range(1 , 10):
        temp = n * i
        temp_list.append(temp)
        if temp % 10 == 0 and temp // 10 not in visited[0]:
            d.append([temp // 10 , '0'])
            visited[0].add(temp // 10)
        elif temp % 10 == 1 and temp // 10 not in visited[0]:
            d.append([temp // 10 , '1'])
            visited[0].add(temp//10)
    stat = False
    while d:
        number , word = d.popleft()
        if len(str(number)) + len(word) > 100: continue
        if check(number):
            stat = True
            answer = str(number) + word
            break
        else:
            for i in range(1,10):
                temp = temp_list[i-1]
                temp += number
                if temp % 10 == 0 and temp // 10 not in visited[len(word)]:
                    d.append([temp // 10, '0' + word])
                    visited[len(word)].add(temp//10)
                elif temp % 10 == 1 and temp // 10 not in visited[len(word)]:
                    d.append([temp // 10, '1' + word])
                    visited[len(word)].add(temp // 10)
    if stat: print(answer)
    else : print("BRAK")