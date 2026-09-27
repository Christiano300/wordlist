import json
import random

weighing_func = lambda x: x ** 2

def random_with_weight(distr: list[int]):
    total = sum((weighing_func(i) for i in distr))
    if total == 0:
        return 26
    rand = random.randint(0, total - 1)
    for i, weight in enumerate(distr):
        if rand < weighing_func(weight):
            return i
        rand -= weighing_func(weight)
    return len(distr) - 1

with open("out.json") as f:
    probs = json.load(f)


def gen() -> str:
    word = []
    num = random_with_weight(probs[0])
    word.append(chr(num + ord('a')))
    i = 1
    while i < 13:
        prev = word[i - 1]
        next = random_with_weight(probs[i][ord(prev) - ord('a')])
        if next == 26:
            break
        word.append(chr(next + ord('a')))
        i += 1
    return "".join(word)

for i in range(20_000):
    print(gen())