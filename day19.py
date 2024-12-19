import sys
from collections import deque

if(len(sys.argv) < 2):
  print('please put in input')
  exit(-1)

D = open(sys.argv[1]).read().strip()
D = D.split('\n')
patterns = D[0].split(', ')
designs = D[2:]


def dp1(patterns, designs):
  #memo dict
  memo = dict()

  def can_construct(design):
    if not design:
      return True

    if design in memo:
      return memo[design]
    
    for pattern in patterns:
      if design.startswith(pattern):
        if can_construct(design[len(pattern):]):
          memo[design] = True
          return True
    memo[design] = False
    return False
  
  p1 = 0
  for design in designs:
    if can_construct(design):
      p1 += 1
  return p1


def dp2(patterns, designs):
  memo = dict()

  def num_ways(design):
    if not design:
      return 1
    if design in memo:
      return memo[design]
    
    ways = 0
    for p in patterns:
      if design.startswith(p):
        ways += num_ways(design[len(p):])
    memo[design] = ways
    return ways
  
  p2 = 0
  for d in designs:
    p2 += num_ways(d)
  return p2



print(dp1(patterns, designs))
print(dp2(patterns, designs))

