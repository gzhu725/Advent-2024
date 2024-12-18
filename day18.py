import sys
from collections import deque

if len(sys.argv) < 2:
    print('Please provide an input file.')
    exit(-1)

D = open(sys.argv[1]).read().strip()
p1 = 0
dirs = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left

n = 71
grid = [['.' for c in range(n)] for r in range(n)]
bs = D.split('\n')
for i,line in enumerate(bs):
    x,y = list(map(int, line.split(',')))
    if 0<=y<n and 0<=x<n:
        grid[y][x] = '#'

    queue = deque([(0,0,0)])
    visited = set()
    ok = False
    while queue:
        dist,r,c = queue.popleft()
        if (r,c) == (n-1,n-1):
            if i==1023:
                print(dist)
            ok = True
            break
        if (r,c) in visited:
            continue
        visited.add((r,c))
        for dr,dc in dirs:
            nr = r+dr
            nc = c+dc
            if 0<=nr<n and 0<=nc<n and grid[nr][nc] != '#':
                queue.append((dist+1,nr,nc))
    if not ok:
      print(x,y)
      break
