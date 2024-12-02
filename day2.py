import sys
if(len(sys.argv) < 2):
  print('please put in input')
  exit(-1)
D = open(sys.argv[1]).read().strip()
lines = D.split("\n") #array for input

p1 = 0
p2 = 0

def is_safe(numbers):
  def isMonotonic(l):
    first = l[0]
    last = l[len(l) - 1]
    m = -2
    if(first > last):
      m = 1
    else:
      m = 0
    for i in range(len(l) - 1):
      if m == 1:
        if(l[i] < l[i + 1]):
          return False
      if m == 0:
        if(l[i] > l[i + 1]):
          return False
    return True
  if not isMonotonic(numbers):
      return False

  for i in range(len(numbers) - 1):
    distance = abs(numbers[i] - numbers[i+1])
    if distance < 1 or distance > 3:
      return False
  return True

for line in lines:
    numbers = list(map(int, line.split()))
    safe = False

    if is_safe(numbers):
        p1 += 1
        safe = True
    else:
        for i in range(len(numbers)):
            copy = numbers[:i] + numbers[i + 1:]  # remove the i-th element
            if is_safe(copy):
                safe = True
                break

    if safe:
        p2 += 1

print(p1)
print(p2)