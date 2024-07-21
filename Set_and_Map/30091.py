import sys
input = sys.stdin.readline
n = int(input())
l = sorted(list(map(int,input().split())))
number = dict()
for x in l:
    if x in number: number[x] += 1
    else: number[x] = 1
l = list(set(l))
n = len(l)

d = dict()
for i in range(n):
    for j in range(i + 1 , n):
        k = l[i] + l[j]
        if k not in d:
            d[k] = l[i] * l[j] * min(number[l[i]] , number[l[j]])
        else:
            d[k] += l[i] * l[j] * min(number[l[i]] , number[l[j]])

answer = -1
for x in number.keys():
    if number[x] >= 2:
        if x * 2 in d:
            d[x * 2] += x * x * number[x] // 2
        else:
            d[x * 2] = x * x * number[x] // 2
for x in d.keys():
    answer = max(answer , d[x])
print(answer)


