import sys
if(len(sys.argv) < 2):
  print('please put in input')
  exit(-1)
D = open(sys.argv[1]).read().strip()
grid = D.split("\n") #array for input
grid = [list(row) for row in grid]
rows = len(grid)
cols = len(grid[0])
current_x, current_y =  -1, -1 
p1 = 0
cd = 0
p2 = 0

# current pos of guard
for r in range(rows):
  for c in range(cols):
    if grid[r][c] == '^':
      current_x, current_y = r, c

dirs = [(-1,0), (0,1), (1, 0), (0,-1)]
#up (one row over), right (one col over), left (one row over), down (one col over)
visited = set()
visited.add((current_x, current_y))

while current_x >= 0 and current_x < rows and current_y >= 0 and current_y < cols:
  visited.add((current_x, current_y))
  while True:
    #going in one direction
    current_dir = dirs[cd]
    next_row = current_x + current_dir[0]
    next_col = current_y + current_dir[1]
    if next_row >=0 and next_row < rows and next_col >= 0 and next_col < cols and grid[next_row][next_col] == '#':
      cd += 1
      if cd == 4:
        cd = 0
    else:
      current_x, current_y = next_row, next_col
      break

p1 = len(visited)
print(p1)

# p2

for r in range(rows):
  for c in range(cols):
    if grid[r][c] == '^':
      current_x, current_y = r, c

for iter_row in range(rows):
  for iter_col in range(cols):
    if (iter_row == current_x and iter_col == current_y) or grid[iter_row][iter_col] != '.':
      continue
    r,c = current_x, current_y
    cd = 0
    visited2 = set()
    while True:
      if(r,c,cd) in visited2: 
        p2 += 1
        break
      visited2.add((r,c,cd))
      current_dir = dirs[cd]
      next_row = r + current_dir[0]
      next_col = c + current_dir[1]
      if next_row <0 or next_row > rows -1 or next_col < 0 or next_col > cols -1:
        break
      if grid[next_row][next_col] == '#' or (next_row == iter_row and next_col == iter_col):
        cd += 1
        if cd == 4:
          cd = 0
      else:
        r, c = next_row, next_col

print(p2)



 


