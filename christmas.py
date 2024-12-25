import sys
if(len(sys.argv) < 2):
  print('please put in input')
  exit(-1)
D = open(sys.argv[1]).read().strip()
lines = D.split("\n") #array for input
grids = list()
lines.append('')
cur_line = ''
for line in lines:
  if line == '':
    grids.append(cur_line)
    cur_line = ''
  else:
    cur_line += line


locks = list()
keys = list()
def calc_height(grid):
  global locks
  global keys
  heights = list()
  if grid[0] == '#####':
    for col in range(5):
      for row in range(7):
        if grid[row][col] == '.':
          heights.append(row - 1)
          break
  if grid[0] == '.....':
    for col in range(5):
      for row in range(7):
        # print(grid[row][col])
        if grid[row][col] == '#':
          heights.append(7 - row - 1)
          break
  if grid[0] == '.....':
    keys.append(heights)
  else:
    locks.append(heights)


          




for grid in grids:
  grid = [grid[i:i+5] for i in range(0, len(grid), 5)]
  calc_height(grid)

p1 = 0
for l in locks:
  for k in keys:
    ok = True
    for i in range(5):
      if k[i] + l[i] > 5:
        ok = False
    if ok:
      p1 += 1

print(p1)
    

