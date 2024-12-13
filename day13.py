import sys
from sympy import Matrix, Integer, symbols, solve_linear_system

if len(sys.argv) < 2:
    print('please put in input')
    exit(-1)

D = open(sys.argv[1]).read().strip()
lines =  D.split("\n")  #array for input
p1 = True # if False, p2
all_things = list()
current_prize = list() #ax, ay, bx, by, px, py
for line in lines:
  if line == '0':
    break
  if line == '':
    all_things.append(tuple(current_prize[2:]))
    current_prize = []
  else:
    if 'A' in line:
      items = line.split(": ")
      move_x, move_y = items[1].split(',')
      a_x = int(move_x[2:])
      a_y = int(move_y[2:])
      current_prize.append(a_x)
      current_prize.append(a_y)
    if 'B' in line:
      items = line.split(": ")
      move_x, move_y = items[1].split(',')
      b_x = int(move_x[2:])
      b_y = int(move_y[2:])
      current_prize.append(b_x)
      current_prize.append(b_y)
    if 'P' in line:
      items = line.split(": ")
      move_x, move_y = items[1].split(',')
      p_x = int(move_x[2:])
      p_y = int(move_y[3:])
      if p1:
        current_prize.append(p_x)
        current_prize.append(p_y)
      else:
        current_prize.append(p_x + 10000000000000)
        current_prize.append(p_y + 10000000000000)
        

# print(all_things)

# 94a + 22b = 8400
# 34a + 67b = 5400

# if a and b are ints, is a solution

# SOLUTION OF TWO EQUATIONS??

ans = 0

for t in all_things:
    A = Matrix([[t[0], t[2]], [t[1], t[3]]])
    
    b = Matrix([t[4], t[5]])
    
    x1, x2 = symbols('x1 x2')
    
    system = A.col_insert(2, b) 
    solution = solve_linear_system(system, x1, x2)
    if isinstance(solution[x1], Integer) and isinstance(solution[x2], Integer):
      cost = 3 * solution[x1] + solution[x2]
      ans += cost
      

# if your running p2 change the p1 variable to false, up top at line 10
print(ans)


