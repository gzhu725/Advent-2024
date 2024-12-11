import sys

if len(sys.argv) < 2:
    print('please put in input')
    exit(-1)

D = open(sys.argv[1]).read().strip()
D = list(map(int, D.split(" ")))

dp = {}

def find_steps(number, steps):
  # for each number, how many stones do we get from STEPS step
  if (number, steps) in dp:
    return dp[(number,steps)]
  if steps == 0:
    stones = 1
  elif number == 0:
    #if the number is 0, its now 1
    stones = find_steps(1, steps - 1) 
  elif len(str(number))%2==0:
    string_number = str(number)
    left = string_number[0: len(string_number)//2]
    right = string_number[len(string_number)//2:]
    left, right = (int(left), int(right))
    stones = find_steps(left, steps-1) + find_steps(right, steps-1)
  else:
    stones = find_steps(number*2024, steps-1)
  dp[(number, steps)] = stones
  return stones


p1 = 0
for stone in D:
  p1 += find_steps(stone, 25)

print(p1)

p2 = 0
for stone in D:
  p2 += find_steps(stone, 75)

print(p2)