import sys
from collections import deque 
#list를 통해 pop(0) 하면 O(N)의 시간 복잡도를 갖고
#deque을 이용해 popleft()하면 O(1)의 시간복잡도를 갖는다.

M, N = map(int, sys.stdin.readline().split())
#N is Row, M is Col

Map = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

moveXaxis = [-1, 1, 0, 0]
moveYaxis = [0, 0, -1, 1]

queue = deque([])

#Map의 element 하나하나 [i][j] index를 일종의 Vertex로 생각하는 접근 방식

for i in range(N):
    for j in range(M):
        if Map[i][j] == 1: #When tomato exists in the box, Append coordinate in queue
            queue.append([i,j])
    
def BFS():
    global queue
    
    while queue:
        
        r, c = queue.popleft() #row column
        
        for i in range(4):
            Adjr = r + moveXaxis[i]
            Adjc = c + moveYaxis[i]
            
            if 0<=Adjc<M and 0<=Adjr<N and Map[Adjr][Adjc] == 0:
                #Map[Adjr][Adjc] == 0에 의해 토마토가 담기지 않은 -1은 조회하지도 않고
                #queue에 append 되지도 않음
                Map[Adjr][Adjc] = Map[r][c] + 1
                queue.append([Adjr,Adjc])
BFS()

ans = 0

for coord in Map:
    for tomato in coord:
        if tomato == 0:
            print(-1)
            sys.exit(0)
    ans = max(ans, max(coord))

print(ans - 1)