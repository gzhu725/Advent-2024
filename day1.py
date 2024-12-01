import sys
if(len(sys.argv) < 2):
  print('please put in input')
  exit(-1)
D = open(sys.argv[1]).read().strip()
lines = D.split("\n") #array for input


left = []
right = []
for line in lines:
  numbers = line.split("   ")
  left.append(int(numbers[0]))
  right.append(int(numbers[1]))

#part 1
sorted_left = sorted(left)
sorted_right = sorted(right)
distance = 0
for i in range(len(left)):
  distance += abs(sorted_left[i] - sorted_right[i])
print(distance)

#part 2
count = 0 
for number in left:
  score = number * right.count(number)
  count += score
print(count)



