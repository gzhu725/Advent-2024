import sys
from itertools import combinations
import random

# Check for input file
if len(sys.argv) < 2:
    print('Please provide an input file.')
    exit(-1)

# Read input
D = open(sys.argv[1]).read().strip().split('\n')

edges = {}
for line in D:
    start, end = line.split('-')
    if start not in edges:
        edges[start] = set() # of connections
    if end not in edges:
        edges[end] = set() # of connections
    edges[start].add(end) # not go in same direction so add them all
    edges[end].add(start)

three_interconnected = []
nodes = list(edges.keys())
for a, b, c in combinations(nodes, 3):
    if b in edges[a] and c in edges[a] and c in edges[b]:
        three_interconnected.append((a, b, c))

p1 = list()
for t in three_interconnected:
  if t[0].startswith('t') or t[1].startswith('t') or t[2].startswith('t'):
    p1.append(t)

print(len(p1))

starts = list(edges.keys())
best = None
for t in range(10000):
  random.shuffle(starts)
  clique = list()
  for start in starts:
    flag = True
    for val in clique:
      if start not in edges[val]:
        flag = False
    if flag:
      clique.append(start)
  if best is None or len(clique) > len(best):
    best = clique

print(','.join(sorted(best)))
