import sys
from collections import deque
import heapq


if(len(sys.argv) < 2):
  print('please put in input')
  exit(-1)
D = open(sys.argv[1]).read().strip()
grid = D.split("\n")
letters = ['E', 'S', 'W', 'N']
dirs = {'E': (0, 1), 'S': (1, 0), 'W': (0, -1), 'N': (-1, 0) }
rows = len(grid)
cols = len(grid[0])
rx, ry = 0,0 # reindeer x, y
ex, ey = 0,0 #ending x, y
# find start and end positions
for r in range(rows):
  for c in range(cols):
    if grid[r][c] == 'S':
      rx, ry = r, c
    if grid[r][c] == 'E':
      ex, ey = r, c

val = [] # cost, reindeer x, reindeer y, direction
heapq.heappush(val, (0, rx, ry, 'E'))
visited = set()
dist = {}
lowest_score = sys.maxsize
scores = list()
while val:
  score, rx, ry, dirr = heapq.heappop(val)

  if rx == ex and ry == ey:
    # we ended, find lowest score
    scores.append(score)
    continue
  if (rx,ry,dirr) not in dist:
    dist[(rx,ry,dirr)] = score
  if ((rx,ry,dirr) in visited):
    continue
  visited.add((rx,ry,dirr))

  dx, dy = dirs[dirr] # current direction
  nx, ny = rx + dx, ry + dy
  if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
    heapq.heappush(val, (score +1, nx, ny, dirr))
  
  heapq.heappush(val, (score + 1000, rx, ry, letters[(letters.index(dirr) - 1) % 4]))
  heapq.heappush(val, (score + 1000, rx, ry, letters[(letters.index(dirr) + 1) % 4]))

  
print(min(scores))


dist2 = {}
val = []
visited = set()
heapq.heappush(val, (0, ex, ey, 'E'))
heapq.heappush(val, (0, ex, ey, 'S'))
heapq.heappush(val, (0, ex, ey, 'W'))
heapq.heappush(val, (0, ex, ey, 'N'))

while val:
  score, rx, ry, dirr = heapq.heappop(val)

  if (rx,ry,dirr) not in dist2:
    dist2[(rx,ry,dirr)] = score
  if ((rx,ry,dirr) in visited):
    continue
  visited.add((rx,ry,dirr))

  dx, dy = dirs[letters[(letters.index(dirr) + 2) % 4]] # current direction
  nx, ny = rx + dx, ry + dy
  if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
    heapq.heappush(val, (score +1, nx, ny, dirr))
  heapq.heappush(val, (score + 1000, rx, ry, letters[(letters.index(dirr) + 1) % 4]))
  heapq.heappush(val, (score + 1000, rx, ry, letters[(letters.index(dirr) + 3) % 4]))

p2 = set()
for r in range(rows):
    for c in range(cols):
        for dirr in ['E', 'S', 'W', 'N']:
            if (r, c, dirr) in dist and (r, c, dirr) in dist2 and dist[(r, c, dirr)] + dist2[(r, c, dirr)] == min(scores):
                p2.add((r, c))
print(len(p2) + 1)