import sys

if len(sys.argv) < 2:
    print("plz provide input")
    exit(-1)

with open(sys.argv[1]) as f:
    grid = f.read().strip().split("\n")

word = "XMAS"
rows = len(grid)
cols = len(grid[0])
p1 = 0
p2 = 0

def check_word(r, c, dr, dc):
    for i in range(4):
        next_row = r + i * dr
        next_col = c + i * dc
        if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or grid[next_row][next_col] != word[i]:
            return False
    return True

for r in range(rows):
    for c in range(cols):
        directions = [ (0, 1),(0, -1), (1, 0),
            (-1, 0),
            (1, 1), 
            (-1, -1),
            (1, -1), 
            (-1, 1),
        ]
        for dr, dc in directions:
            if check_word(r, c, dr, dc):
                p1 += 1

print(p1)

def check_xmas(r, c):
    if grid[r][c] != 'A':
        return False

    if (r - 1 >= 0 and c - 1 >= 0 and grid[r - 1][c - 1] == 'M' and r + 1 < rows and c - 1 >= 0 and grid[r + 1][c - 1] == 'M' and  r - 1 >= 0 and c + 1 < cols and grid[r - 1][c + 1] == 'S' and r + 1 < rows and c + 1 < cols and grid[r + 1][c + 1] == 'S'):
      return True
    if (r - 1 >= 0 and c - 1 >= 0 and grid[r - 1][c - 1] == 'S' and r + 1 < rows and c - 1 >= 0 and grid[r + 1][c - 1] == 'S' and r - 1 >= 0 and c + 1 < cols and grid[r - 1][c + 1] == 'M' and r + 1 < rows and c + 1 < cols and grid[r + 1][c + 1] == 'M'):
      return True
    if(r - 1 >= 0 and c - 1 >= 0 and grid[r - 1][c - 1] == 'M' and r + 1 < rows and c - 1 >= 0 and grid[r + 1][c - 1] == 'S' and r - 1 >= 0 and c + 1 < cols and grid[r - 1][c + 1] == 'M' and r + 1 < rows and c + 1 < cols and grid[r + 1][c + 1] == 'S'):
      return True
    if (r - 1 >= 0 and c - 1 >= 0 and grid[r - 1][c - 1] == 'S' and r + 1 < rows and c - 1 >= 0 and grid[r + 1][c - 1] == 'M' and r - 1 >= 0 and c + 1 < cols and grid[r - 1][c + 1] == 'S' and r + 1 < rows and c + 1 < cols and grid[r + 1][c + 1] == 'M'):
      return True
    return False

for r in range(rows):
    for c in range(cols):
        if check_xmas(r, c):
            p2 += 1

print(p2)
