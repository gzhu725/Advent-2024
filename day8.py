import sys

if len(sys.argv) < 2:
    print('please put in input')
    exit(-1)

D = open(sys.argv[1]).read().strip()
grid = D.split("\n")  #array for input
grid = [list(row) for row in grid]
rows = len(grid)
cols = len(grid[0])
antennas = {}
antinodes = set()
antinodes_2 = set()

for r in range(rows):
    for c in range(cols):
        if grid[r][c].isalnum():
            if grid[r][c] not in antennas:
                antennas[grid[r][c]] = []
            antennas[grid[r][c]].append([r, c])

#  FOR EACH POSITION OF A POTENTIAL ANTINODE
for r in range(rows):
  for c in range(cols):
    for freq, positions in antennas.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                # two possible positions for nodes
                r1, c1 = positions[i]
                r2, c2 = positions[j]
                d1 = abs(r-r1)+abs(c-c1)
                d2 = abs(r-r2)+abs(c-c2)  
                dr1 = r-r1 
                dr2 = r-r2
                dc1 = c-c1
                dc2 = c-c2
                #dr dc refer to if the potnetial antinode is in line with the two nodes
                #is (r - r1)/(c -c1) = (r2 - r1)/(c2 - c1)
                if (d1==2*d2 or d1*2==d2) and 0<=r<rows and 0<=c<cols and (dr1*dc2 == dc1*dr2):
                  antinodes.add((r,c))
                if 0<=r<rows and 0<=c<cols and (dr1*dc2 == dc1*dr2):
                  antinodes_2.add((r,c))

print(len(antinodes))
print(len(antinodes_2))