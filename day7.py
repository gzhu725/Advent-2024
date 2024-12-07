import sys
from itertools import product

if len(sys.argv) < 2:
    print('please put in input')
    exit(-1)

D = open(sys.argv[1]).read().strip()
lines = D.split("\n")  # array for input

p1 = 0
symbols = ['+', '*']  # FOR PART TWO, MAKE SYMBOLS ['+', '*', '||']

for line in lines:
    num, vals = line.split(":")
    vals = vals.split(" ")
    vals = vals[1:]
    num = int(num)
    vals = list(map(int, vals))
    s = len(vals) - 1
    combinations = product(symbols, repeat=s)
    is_solvable = False

    for combo in combinations:
        result = vals[0]
        for i, op in enumerate(combo):
            if op == '+':
                result += vals[i + 1]
            elif op == '*':
                result *= vals[i + 1]
            elif op == '||':
              result = str(result)
              lol = str(vals[i + 1])
              new = result + lol
              result = int(new) 

        if result == num:
            is_solvable = True
            break 

    if is_solvable:
        p1 += num

print(p1)
