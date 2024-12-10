from collections import deque
import sys
if(len(sys.argv) < 2):
  print('please put in input')
  exit(-1)

with open(sys.argv[1], 'r') as file:
    grid = [list(map(int, row.strip())) for row in file.readlines()]

def scores(grid):
    rows = len(grid)
    cols = len(grid[0])
    trailheads = list()
    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == 0:
          trailheads.append((r,c))
    #all 0s and positions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def bfs(r, c):
        visited = set()
        queue = deque([(r, c)])
        visited.add((r, c))
        nines = set()

        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols:
                    if (nx, ny) not in visited and grid[nx][ny] == grid[x][y] + 1:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        if grid[nx][ny] == 9:
                            nines.add((nx, ny))

        return len(nines)

    total_score = 0
    for r, c in trailheads:
        total_score += bfs(r, c)

    return total_score


def ratings(grid):
    rows = len(grid)
    cols = len(grid[0])
    trailheads = list()
    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == 0:
          trailheads.append((r,c))
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    path_count_cache = {}

    def dfs(x, y):
        if (x, y) in path_count_cache:
            return path_count_cache[(x, y)]

        if grid[x][y] == 9:
            return 1

        total_paths = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == grid[x][y] + 1:
                total_paths += dfs(nx, ny)

        path_count_cache[(x, y)] = total_paths
        return total_paths

    total_rating = 0
    for r, c in trailheads:
        total_rating += dfs(r, c)

    return total_rating

p1 = scores(grid)
p2 = ratings(grid)

print(p1)
print(p2)