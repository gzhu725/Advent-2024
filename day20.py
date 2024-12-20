# ALL CRED TO JIM CHEN
import sys
import collections
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
n = len(lines)
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    if 'S' in lines[i]:
        sx = i
        sy = lines[i].index('S')
    if 'E' in lines[i]:
        ex = i
        ey = lines[i].index('E')
m = len(lines[0])
print(sx,sy,ex,ey)

directions = [(0,1),(1,0), (0,-1),(-1,0)]
memo = {}
def bfs(cheat_wall):
    Q = collections.deque()
    Q.append((sx,sy,0))
    visited = set()
    while Q:
        x,y,dist = Q.popleft()
        if (x,y) in visited or x<0 or x>=n or y<0 or y>=m or ((x,y) != cheat_wall and lines[x][y]=='#'):
            continue
        if (x,y) not in memo:
            memo[(x,y)] = dist
        if lines[x][y]=='E':
            return dist
        visited.add((x,y))
        for d in directions:
            dx,dy = d
            Q.append((x+dx,y+dy,dist+1))
memo2 = {}
def bfs2():
    Q = collections.deque()
    Q.append((ex,ey,0))
    visited = set()
    while Q:
        x,y,dist = Q.popleft()
        if (x,y) in visited or x<0 or x>=n or y<0 or y>=m or (lines[x][y]=='#'):
            continue
        if (x,y) not in memo2:
            memo2[(x,y)] = dist
        if lines[x][y]=='S':
            return dist
        visited.add((x,y))
        for d in directions:
            dx,dy = d
            Q.append((x+dx,y+dy,dist+1))
ans = 0
memo = {}
memo2 = {}
base_case = bfs((0,0))
bfs2()
for i in range(1,n-1):
    for j in range(1,m-1):
        if lines[i][j]=="#":
            for d in directions:
                if (i+d[0],j+d[1]) in memo and (i-d[0],j-d[1]) in memo2:
                    diff = base_case - (memo[(i+d[0],j+d[1])] + memo2[(i-d[0],j-d[1])] + 1)
                    if diff >=100:
                        #print(diff)
                        ans += 1
print(ans)

def bfs3():
    Q = collections.deque()
    Q.append((sx,sy,0))
    visited = set()
    while Q:
        x,y,dist = Q.popleft()
        if (x,y) in visited or x<0 or x>=n or y<0 or y>=m or ( lines[x][y]=='#'):
            continue
        if (x,y) not in memo:
            memo[(x,y)] = dist
        visited.add((x,y))
        for d in directions:
            dx,dy = d
            Q.append((x+dx,y+dy,dist+1))
    Q = collections.deque()
    Q.append((ex,ey,0))
    visited = set()
    while Q:
        x,y,dist = Q.popleft()
        if (x,y) in visited or x<0 or x>=n or y<0 or y>=m or (lines[x][y]=='#'):
            continue
        if (x,y) not in memo2:
            memo2[(x,y)] = dist
        if lines[x][y]=='S':
            return dist
        visited.add((x,y))
        for d in directions:
            dx,dy = d
            Q.append((x+dx,y+dy,dist+1))

ans2 = 0
bfs3()
counts = {}
visited = set()
for i in range(1,n-1):
    for j in range(1,m-1):
        if lines[i][j]==".":
            for d in directions:
                x,y=i+d[0],j+d[1]
                if (x,y) in visited:
                    continue
                for a in range(max(1,x-20),min(n-1,x+20+1)):
                    for b in range(max(1,y-20),min(m-1,y+20+1)):
                        dis = abs(a-x)+abs(b-y)
                        if dis<=20:
                            if (x,y) in memo and (a,b) in memo2:
                                diff = base_case - (memo[(x,y)]+memo2[(a,b)]+dis)
                                if diff>=100:
                                    #print(diff,x,y,a,b)
                                    if diff not in counts:
                                        counts[diff] = 0
                                    counts[diff]+=1
                                    ans2 += 1
                visited.add((x,y))
print(ans2)