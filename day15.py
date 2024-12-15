import sys
from collections import deque

if(len(sys.argv) < 2):
  print('please put in input')
  exit(-1)

part2 = True # i guess hARD CODE THIS HAAAA
D = open(sys.argv[1]).read().strip()
grid, instructions = D.split('\n\n')
grid = grid.split('\n')


rows = len(grid)
cols = len(grid[0])
grid = [[grid[r][c] for c in range(cols)] for r in range(rows)]
new_grid = []

if part2:
  for r in range(rows):
    row = list()
    for c in range(cols):
      if grid[r][c] == '#':
        row.append('#')
        row.append('#')
      if grid[r][c] == 'O':
        row.append('[')
        row.append(']')
      if grid[r][c] == '.':
        row.append('.')
        row.append('.')
      if grid[r][c] == '@':
        row.append('@')
        row.append('.')
    new_grid.append(row)
  grid = new_grid
  cols = cols * 2

p1 = 0
p2 = 0 
cx, cy = 0,0

for r in range(rows):
  for c in range(cols):
    if grid[r][c] == '@':
      cx, cy = r, c
      grid[r][c] = '.'
      break

for i in instructions:
  if i == '\n':
    continue
  dr,dc = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}[i]
  nr, nc = cx + dr, cy + dc
  if grid[nr][nc] == '#':
    # border
    continue
  elif grid[nr][nc] == '.':
    cx, cy = nr, nc # move forward
  elif grid[nr][nc] in ['[', 'O', ']']:
    # moving rocks ...
    queue = deque([(cx,cy)])
    seen = set()
    ok = True
    while queue:
      nr, nc = queue.popleft()
      if (nr, nc) in seen:
        continue
      seen.add((nr,nc))
      nnr, nnc = nr + dr, nc + dc #next one over
      if grid[nnr][nnc] == '#':
        #can no longer move
        ok = False
        break
      if grid[nnr][nnc] == 'O':
        queue.append((nnr,nnc)) # more rocks to move
      if grid[nnr][nnc] == '[':
        queue.append((nnr,nnc)) # [
        queue.append((nnr, nnc + 1)) # ]
      if grid[nnr][nnc] == ']':
        queue.append((nnr, nnc)) # ]
        queue.append((nnr, nnc - 1)) #[
        
    if not ok:
      #no moving with '#'
      continue
    
    while len(seen) > 0:
      for nr, nc in sorted(seen):
        nnr, nnc = nr + dr, nc + dc
        if (nnr, nnc) not in seen:
          grid[nnr][nnc] = grid[nr][nc]
          grid[nr][nc] = '.'
          seen.remove((nr,nc))
    cx = cx + dr
    cy = cy + dc

for r in range(rows):
  for c in range(cols):
    if grid[r][c] in ['[', 'O']:
      p1 += 100 * r + c

print(p1)







    



