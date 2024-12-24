import sys
import itertools

if len(sys.argv) < 2:
    print('plz provide input file')
    exit(-1)

D = open(sys.argv[1]).read().strip().split('\n')

def parse_input(inputs, gates):
    wires = {}
    for line in inputs:
        wire, value = line.split(": ")
        wires[wire] = int(value)

    gate_operations = []
    for line in gates:
        parts = line.split(" -> ")
        operation, output = parts[0], parts[1]
        gate_operations.append((operation.split(), output))

    return wires, gate_operations

def evaluate_gate(op, val1, val2):
    if op == "AND":
        return val1 & val2
    elif op == "OR":
        return val1 | val2
    elif op == "XOR":
        return val1 ^ val2
    return None

def simulate(wires, gate_operations):
    while gate_operations:
        for operation, output in gate_operations[:]:
            if len(operation) == 3:  
                inp1, op, inp2 = operation
                if inp1 in wires and inp2 in wires:
                    wires[output] = evaluate_gate(op, wires[inp1], wires[inp2])
                    gate_operations.remove((operation, output))
            elif len(operation) == 1: 
                inp = operation[0]
                if inp in wires:
                    wires[output] = wires[inp]
                    gate_operations.remove((operation, output))
    return wires

def get_decimal_from_z(wires):
    z_wires = sorted((key for key in wires if key.startswith("z")), key=lambda x: int(x[1:]))

    binary = "".join(str(wires[wire]) for wire in z_wires)
    print(binary[::-1])
    return int(binary[::-1], 2)

idx = -1
inputs = list()
for i in range(len(D)):
  line  = D[i]
  if line != '':
    inputs.append(line)
  if line == '':
    idx = i
    break

gates = list()
for i in range(idx + 1, len(D)):
  line = D[i]
  gates.append(line)


wires, gate_operations = parse_input(inputs, gates)
wires = simulate(wires, gate_operations)
result = get_decimal_from_z(wires)
print(result)
