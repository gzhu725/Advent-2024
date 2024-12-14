import sys

if len(sys.argv) < 2:
    print('please put in input')
    exit(-1)

width, height = 101, 103
middle_x, middle_y = width // 2, height // 2
grid = [['.' for _ in range(width)] for _ in range(height)]
x = 1

data = open(sys.argv[1]).read().strip()
lines = data.split("\n")
final_coords = []

for robot in lines:
    values = robot.split(" ")
    x, y = map(int, values[0][2:].split(","))
    vx, vy = map(int, values[1][2:].split(","))

    # Update positions for 100 seconds
    for i in range(100):
        x = (x + vx) % width
        y = (y + vy) % height

    grid[y][x] = 'l'
    final_coords.append((x, y))
    
 
    while x % 103 != 88 or x % 101 != 38:
        x += 1
    print(x)

q1 = q2 = q3 = q4 = 0
for x, y in final_coords:
    if x == middle_x or y == middle_y:
        continue 
    elif x < middle_x and y < middle_y:
        q1 += 1 
    elif x > middle_x and y < middle_y:
        q2 += 1 
    elif x < middle_x and y > middle_y:
        q3 += 1
    elif x > middle_x and y > middle_y:
        q4 += 1 

print(q1 * q2 * q3 * q4)
# i got too lazy, prints out the part 2 first multiple times, then part 1 at the bottom
# for item in grid: 
#   print(''.join(item))