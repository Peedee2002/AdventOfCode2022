with open("input.txt") as f:
    file_content = f.read().split('\n')[:-1]
total = 0
for line in file_content:
    ranges = line.split(',')
    elf1 = [int(i) for i in ranges[0].split('-')]
    elf2 = [int(i) for i in ranges[1].split('-')]
    if len(set(range(elf1[0], elf1[1] + 1)).intersection(range(elf2[0], elf2[1] + 1))) > 0:
        total += 1
print(total)