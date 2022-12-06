import heapq
elves = []
with open("input.txt") as f:
    file_content = f.read().split('\n')
    current_elf: list[int] = []
    for string in file_content:
        if string == '':
            # new elf
            elves.append(current_elf)
            current_elf = []
        else:
            current_elf.append(int(string))

calories = [sum(elf) for elf in elves]
print(sum(heapq.nlargest(3, calories)))