"""
        [H]         [S]         [D]
    [S] [C]         [C]     [Q] [L]
    [C] [R] [Z]     [R]     [H] [Z]
    [G] [N] [H] [S] [B]     [R] [F]
[D] [T] [Q] [F] [Q] [Z]     [Z] [N]
[Z] [W] [F] [N] [F] [W] [J] [V] [G]
[T] [R] [B] [C] [L] [P] [F] [L] [H]
[H] [Q] [P] [L] [G] [V] [Z] [D] [B]
 1   2   3   4   5   6   7   8   9 
"""

import re
init = [
    ['H', "T", "Z", "D"],
    ['Q', "R", "W", "T", "G", "C", "S"],
    ['P', "B", "F", "Q", "N", "R", "C", "H"],
    ['L', "C", "N", "F", "H", "Z"],
    ['G', "L", "F", "Q", "S"],
    ['V', "P", "W", "Z", "B", "R", "C", "S"],
    ['Z', "F", "J"],
    ['D', "L", "V", "Z", "R", "H", "Q"],
    ['B', "H", "G", "N", "F", "Z", "L", "D"],
]

with open("input.txt") as f:
    file_content = f.read().split('\n')[:-1]
for line in file_content:
    amount, start, finish = re.match("move (\d+) from (\d+) to (\d+)", line).groups()
    # type 1
    # for _ in range(int(amount)):
    #     box = init[int(start) - 1].pop()
    #     init[int(finish) - 1].append(box)
    # type 2
    boxes = init[int(start) - 1][-int(amount):]
    for _ in range(int(amount)):
        init[int(start) - 1].pop()
    init[int(finish) - 1].extend(boxes)
print(''.join(stack[-1] for stack in init))