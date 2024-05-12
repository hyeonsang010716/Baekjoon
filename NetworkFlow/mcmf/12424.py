import sys
from collections import deque
from sys import maxsize
input = sys.stdin.readline

def solve(case):
    power = list(map(int,input().split()))
    table = [list(map(int,input().split())) for _ in range(3)]
    source = 0
    sink = 7
    length = 8
    capacity = [[0] * length for _ in range(length)]
    connect = [[] for _ in range(length)]
    dist = [[0] * length for _ in range(length)]
    for i in range(1 , 4):
        connect[source].append(i)
        connect[i].append(source)
        capacity[source][i] = power[i]

        connect[i + 3].append(sink)
        connect[sink].append(i+3)
        capacity[i+3][sink] = power[i + 3]

        for j in range(3):
            dist[i][j+4] = -table[i-1][j]
            dist[j+4][i] = table[i-1][j]
            connect[i].append(j+4)
            connect[j+4].append(i)
            capacity[i][j+4] = maxsize

    ans = 0

    while True:
        cost = [maxsize] * length
        visited = [-1] * length
        check = [False] * length
        d = deque([source])
        cost[source] = 0
        while d:
            cur = d.popleft()
            check[cur] = False
            for next in connect[cur]:
                if capacity[cur][next] and cost[next] > cost[cur] + dist[cur][next]:
                    cost[next] = cost[cur] + dist[cur][next]
                    visited[next] = cur
                    if check[next] == False:
                        check[next] = True
                        d.append(next)
        if visited[sink] == -1 : break

        temp = sink
        Max = maxsize
        while temp != source:
            Max = min(Max , capacity[visited[temp]][temp])
            temp = visited[temp]
        temp = sink
        while temp != source:
            capacity[visited[temp]][temp] -= Max
            capacity[temp][visited[temp]] += Max
            ans += dist[visited[temp]][temp] * Max
            temp = visited[temp]

    print("Case #{}: {}".format(case , -ans))



for case in range(1 , int(input()) + 1):
    solve(case)
