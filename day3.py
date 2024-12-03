import sys
if(len(sys.argv) < 2):
  print('please put in input')
  exit(-1)
D = open(sys.argv[1]).read().strip()
lines = D.split("\n") #array for input
p1 = 0
p2 = 0

do = True

for row in lines:
  for i in range(len(row) - 3):
    if row[i:].startswith('do()'):
        do = True
    if row[i:].startswith("don't()"):
        do = False
    if(row[i: i+3] == 'mul'):
      next_char = row[i+3]
      if(next_char == '('):
        for j in range(i+3, len(row)):
          if row[j] == ')':
            new_numbers = row[i+4: j]
            if new_numbers.count(',') == 1:
              try:
                s = list(map(int, new_numbers.split(',')))
                product = s[0] * s[1]
                p1 += product
                if do:
                  p2 += product
              except Exception as e:
                pass
            break
print(p1)
print(p2)
