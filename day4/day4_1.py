with open("input.txt") as f:
    file_content = f.read().split('\n')[:-1]
total = 0
for line in file_content:
    ranges = line.split(',')
    elf1 = [int(i) for i in ranges[0].split('-')]
    elf2 = [int(i) for i in ranges[1].split('-')]
    if elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
        total += 1
    elif elf2[0] >= elf1[0] and elf2[1] <= elf1[1]:
        total += 1
print(total)