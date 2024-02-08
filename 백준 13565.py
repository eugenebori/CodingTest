from collections import deque
import sys

N, M = map(int, input().split())
graph = [list(map(int,input().rstrip())) for _ in range(N)]

dr = [(1,0), (0,1), (-1,0), (0,-1)]

def bfs(x,y):
    q = deque()
    q.append([x,y])
    while q:
        X, Y = q.popleft()
        if X == N-1:
            print('YES')
            exit(0)
        for a,b in dr:
            mx, my = X+a, Y+b
            if 0<=mx<N and 0<=my<M:
                if graph[mx][my] == 0:
                    graph[mx][my] = 1
                    q.append([mx,my])

for i in range(M):
    if graph[0][i] == 0:
        bfs(0,i)

print('NO')