from collections import deque

def eat_apple(head, apples):
    if head in apples:
        apples.remove(head)
        return True
    
    return False

def is_collision(body, N):
    head = body.popleft()

    if head in body:
        return True
    
    if ( (head[0] < 1) or (head[0] > N) ):
        return True
    
    if ( (head[1] < 1) or (head[1] > N) ):
        return True
    
    body.appendleft(head)
    return False

def move(body, direction, N, apples):
    if direction == "U":
        body.appendleft((body[0][0] - 1, body[0][1]))

    elif direction == "D":
        body.appendleft((body[0][0] + 1, body[0][1]))

    elif direction == "L":
        body.appendleft((body[0][0], body[0][1] - 1))

    else:
        body.appendleft((body[0][0], body[0][1] + 1))

    if is_collision(body, N):
        return False
    
    if eat_apple(body[0], apples):
        return True
    
    else:
        body.pop()
        return True
    
def changeDirection(curr_direction, command_T):
    directions = {
            "U" : { "L" : "L", "D" : "R", "F" : "U" }, 
            "D" : { "L" : "R", "D" : "L", "F" : "D" }, 
            "L" : { "L" : "D", "D" : "U", "F" : "L" }, 
            "R" : { "L" : "U", "D" : "D", "F" : "R" }
            }
    
    return directions[curr_direction][command_T]

N = int(input())
K = int(input())

apples = []

for _ in range(K):
    row, col = map(int, input().split())
    apples.append((row, col))

L = int(input())

rotation = []

for _ in range(L):
    X, C = input().split()
    X = int(X)

    rotation.append((X, C))

# 초기 뱀의 좌표는 (1,1)

time = 0
directions = {
            "U" : { "L" : "L", "D" : "R"}, 
            "D" : { "L" : "R", "D" : "L"}, 
            "L" : { "L" : "D", "D" : "U"}, 
            "R" : { "L" : "U", "D" : "D"}
            }

board = [[0 for _ in range(N)] for _ in range(N)]
body = deque([(1,1)])
direction = "R"

while True:
    if not(move(body, direction, N, apples)):
        print(time+1)
        break
    
    time += 1

    for r in rotation:
        if r[0] == time:
            direction = changeDirection(direction, r[1])  
