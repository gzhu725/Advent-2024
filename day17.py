import sys
if(len(sys.argv) < 2):
  print('please put in input')
  exit(-1)
D = open(sys.argv[1]).read().strip()
lines = D.split("\n") #array for input
for l in range(len(lines) - 2):
  val1, val2 = lines[l].split(": ")
  if 'A' in val1:
    a = int(val2)
  elif 'B' in val1:
    b = int(val2)
  elif 'C' in val1:
    c = int(val2)

instr = list(map(int, lines[len(lines) - 1].split(": ")[1].split(",")))

def get_combo_value(operand):
    if operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    return operand


out = list()
# a, b, c, instr
i = 0 
# 440 to 
while i < len(instr):
  opcode = instr[i]
  operand = instr[i+1]
  # print(opcode, operand)
  if opcode == 0:
    a = a // (2 ** get_combo_value(operand))
  elif opcode == 1:
    b = b ^ operand
  elif opcode == 2:
    b = get_combo_value(operand) % 8 
  elif opcode == 3:
    if a != 0:
      i = operand
      continue 
  elif opcode == 4:
    b = b ^ c
  elif opcode == 5:
     out.append(get_combo_value(operand) % 8)
  elif opcode == 6:
    b = a // (2 ** get_combo_value(operand))
  elif opcode == 7:
    c = a // (2 ** get_combo_value(operand))
  i = i + 2

print(",".join(map(str, out)))

#  2,4,1,1,7,5,1,5,4,2,5,5,0,3,3,0
# solution credit to jim chen - doing math backwards
a = 0
Q = [0,1,2,3,4,5,6,7]
for i in range(len(instr)-1,-1,-1):
    goal_b = instr[i]
    Q2 = []
    while Q:
        a = Q.pop()
        for j in range(8):
            test_a = a*8+j
            b = test_a%8
            b = b^1
            c = test_a//(2**b)
            b = b^5
            b = b^c
            b = b%8
            if b==goal_b:
                Q2.append(test_a)
    Q = Q2.copy()
min(Q)
print(min(Q))