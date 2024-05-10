import sys
input = sys.stdin.readline
def distance(point1, point2):
    return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2]) ** 2
n = 3
points = [list(map(int,input().split())) for _ in range(n)]
current_point = [0,0,0]
for a ,b , c in points:
    current_point[0] += a
    current_point[1] += b
    current_point[2] += c
current_point[0] /= n
current_point[1] /= n
current_point[2] /= n

lr = (distance(points[0] , current_point) + 1e-8) ** 0.5
for _ in range(100000):
    temp = [0,0,0]
    for a, b, c in points:
        dd = 1 / ((a - current_point[0]) ** 2 + (b - current_point[1]) ** 2 + (c - current_point[2]) ** 2 + 1e-8) ** 0.5
        temp[0] += (current_point[0] - a) * dd
        temp[1] += (current_point[1] - b) * dd
        temp[2] += (current_point[2] - c) * dd
    current_point[0] -= lr * temp[0]
    current_point[1] -= lr * temp[1]
    current_point[2] -= lr * temp[2]
    lr *= 0.991
d = 0
for p in points:
    d += distance(p, current_point) ** 0.5
print(d)
