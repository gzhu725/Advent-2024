import sys

if len(sys.argv) < 2:
    print('please put in input')
    exit(-1)

disk_map = open(sys.argv[1]).read().strip()

string_rep = ""
char_rep = []

def find_last_occurrence_of_number(lst):
    for i in range(len(lst) - 1, -1, -1):
        if isinstance(lst[i], (int)): 
            return i
    return -1

f = 0 #0 is a file, 1 is free blocks
cur_id = -1
for char in disk_map:
  freq = int(char)
  if f == 0:
    cur_id += 1
  for i in range(freq):
    if f == 0:
      char_rep.append(cur_id)
    else:
      char_rep.append('.')
  f = (f + 1) % 2

while True:
  first_dot_index = char_rep.index('.')
  last_number_index = find_last_occurrence_of_number(char_rep)
  if last_number_index == -1 or first_dot_index > last_number_index:
    break
  char_rep[first_dot_index] = char_rep[last_number_index]
  char_rep[last_number_index] = '.'

p1 = 0
for i in range(len(char_rep)):
  if char_rep[i] == '.':
    break
  lol = i * char_rep[i]
  p1 += lol

print(p1)
