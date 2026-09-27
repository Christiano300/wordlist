from time import perf_counter
import sys

# matrix[0][letter(a-z)]
# matrix[index][previous(a-z)][next(a-z+end)]
matrix = [[[0 for i in range(27)] for i in range(26)] for i in range(13)]
matrix[0] = [0 for i in range(26)]

CSTART = ord('a')
def index(char: str) -> int:
    return ord(char) - CSTART

def enter(word: str):
    first = word[0]
    matrix[0][index(first)] += 1
    for i in range(1, len(word) - 1):
        prev = word[i - 1]
        next = word[i] if i < len(word) else chr(ord('a') + 26)
        matrix[i][index(prev)][index(next)] += 1

    matrix[len(word)][index(word[-1])][26] += 1

with open("simple.txt") as f:
    start = perf_counter()
    for line in f:
        enter(line.strip())
    
    sys.stderr.write("done, ")
    sys.stderr.write(f"{perf_counter() - start:.02f} seconds\n")
    
    print("\n\n".join(str(i) for i in matrix).replace(", ", ","))