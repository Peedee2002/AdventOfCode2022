def calculate_round_1(opposition, me):
    total = 0
    
    if me == 'X':
        total += 1
    if me == 'Y':
        total += 2
    if me == 'Z':
        total += 3
    if opposition == 'A' and me == 'X':
        total += 3
    if opposition == 'A' and me == 'Y':
        total += 6
    if opposition == 'A' and me == 'Z':
        total += 0


    if opposition == 'B' and me == 'X':
        total += 0
    if opposition == 'B' and me == 'Y':
        total += 3
    if opposition == 'B' and me == 'Z':
        total += 6

    if opposition == 'C' and me == 'X':
        total += 6
    if opposition == 'C' and me == 'Y':
        total += 0
    if opposition == 'C' and me == 'Z':
        total += 3


    return total

def calculate_round_2(opposition, me):
    total = 0

    if me == 'X':
        total += 0
    if me == 'Y':
        total += 3
    if me == 'Z':
        total += 6
    if opposition == 'A' and me == 'X':
        total += 3
    if opposition == 'A' and me == 'Y':
        total += 1
    if opposition == 'A' and me == 'Z':
        total += 2


    if opposition == 'B' and me == 'X':
        total += 1
    if opposition == 'B' and me == 'Y':
        total += 2
    if opposition == 'B' and me == 'Z':
        total += 3

    if opposition == 'C' and me == 'X':
        total += 2
    if opposition == 'C' and me == 'Y':
        total += 3
    if opposition == 'C' and me == 'Z':
        total += 1


    return total

with open("input.txt") as f:
    file_content = f.read().split('\n')[:-1]
print(sum(calculate_round_2(string.split(" ")[0], string.split(" ")[1]) for string in file_content))