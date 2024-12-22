import sys

if len(sys.argv) < 2:
    print("plz provide an input file")
    exit(-1)

D = open(sys.argv[1]).read().strip().split("\n")


def gen_number(num):
    prices = [num] 

    for _ in range(2000):
        num ^= (num * 64)
        num %= 16777216

        num ^= (num // 32)
        num %= 16777216

        num ^= (num * 2048)
        num %= 16777216

        prices.append(num)  

    return prices


def price_change(prices):
  lol = list()
  for i in range(len(prices) - 1):
    lol.append(prices[i+1] - prices[i])
  return lol

def calcp2(prices, changes):
    d = {}
    for i in range(len(changes) - 3):
        pattern = tuple(changes[i : i + 4])
        if pattern not in d:
            d[pattern] = prices[i + 4]
    return d


p1 = 0
SCORE = {} 

for line in D:
    num = int(line)

    prices = gen_number(num)
    p1 += prices[-1]

    prices = [x % 10 for x in prices]  
    changes = price_change(prices)
    scores = calcp2(prices, changes)

    for key, value in scores.items():
        if key not in SCORE:
            SCORE[key] = value
        else:
            SCORE[key] += value

print(p1)
print(max(SCORE.values()))
