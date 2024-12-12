import sys
from collections import deque


DIRS = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left
import sys
if(len(sys.argv) < 2):
  print('please put in input')
  exit(-1)
D = open(sys.argv[1]).read().strip()
grid = D.split("\n") #array for input
rows = len(grid)
cols = len(grid[0])
p1 = 0
p2 = 0

seen = set()
for r in range(rows):
    for c in range(cols):
        if (r,c) in seen:
            continue
        queue = deque([(r,c)])
        area = 0
        perim = 0
        PERIM = dict()
        while queue:
            cr,cc = queue.popleft()
            if (cr,cc) in seen:
                continue
            seen.add((cr,cc))
            area += 1
            for dr,dc in DIRS:
                nr = cr+dr
                nc = cc+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==grid[cr][cc]:
                    queue.append((nr,nc))
                else:
                    perim += 1
                    if (dr,dc) not in PERIM:
                        PERIM[(dr,dc)] = set()
                    PERIM[(dr,dc)].add((cr,cc))

        sides = 0
        for k,v in PERIM.items():
            SEEN_PERIM = set()
            old_sides = sides
            for (pr,pc) in v:
                if (pr,pc) not in SEEN_PERIM:
                    sides += 1
                    Q = deque([(pr,pc)])
                    while Q:
                        r2,c2 = Q.popleft()
                        if (r2,c2) in SEEN_PERIM:
                            continue
                        SEEN_PERIM.add((r2,c2))
                        for dr,dc in DIRS:
                            nr,nc = r2+dr,c2+dc
                            if (nr,nc) in v:
                                Q.append((nr,nc))

        p1 += area*perim
        p2 += area*sides


print(p1)
print(p2)