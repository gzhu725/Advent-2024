import sys
if(len(sys.argv) < 2):
  print('please put in input')
  exit(-1)
D = open(sys.argv[1]).read().strip()
lines = D.split("\n") #array for input
p1 = 0

rules = dict() #before, list(after)
index = 0
for line in lines:
  if line == '':
    break
  else:
    index += 1
    numbers = list(map(int,line.split('|')))
    if numbers[0] not in rules:
      rules[numbers[0]] = [numbers[1]]
    else:
      rules[numbers[0]].append(numbers[1])

valid_rules = list()
invalid_rules = list()
for i in range(index + 1, len(lines)):
  line = lines[i]
  line = list(map(int,line.split(',')))
  ok = True
  for j in range(len(line)):
    cur_value = line[j]
    potential_before = line[0: j:]
    potential_after = line[j+1::]
    for value in potential_before:
      if value not in rules:
        ok = False
        break
      if cur_value not in rules[value]:
        ok=False
    for value in potential_after:
      if cur_value not in rules:
        ok = False
        break
      elif value not in rules[cur_value]:
        ok=False
  if ok:
    valid_rules.append(line)
  if not ok:
    invalid_rules.append(line)

p1 = 0
for rule in valid_rules:
  middle = rule[len(rule) // 2]
  p1 += middle
  
print(p1)
  
def reorder_pages(rule, rules):
    ordered = rule.copy()
    changed = True

    while changed:
        changed = False
        for i in range(len(ordered)):
            for j in range(i + 1, len(ordered)):
                x = ordered[i]
                y = ordered[j]
                # is x before y?
                if x in rules and y in rules[x]:
                    if ordered.index(x) > ordered.index(y):  # out of order, needs to be before
                        ordered[i], ordered[j] = ordered[j], ordered[i]
                        changed = True
                # is y before x?
                if y in rules and x in rules[y]:
                    if ordered.index(y) > ordered.index(x):  # out of order, needs to be after
                        ordered[i], ordered[j] = ordered[j], ordered[i]
                        changed = True
    return ordered

p2 = 0
for rule in invalid_rules:
    corrected = reorder_pages(rule, rules)
    middle = corrected[len(corrected) // 2]
    p2 += middle
print(p2)