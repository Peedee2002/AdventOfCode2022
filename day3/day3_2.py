with open("input.txt") as f:
    file_content = f.read().split('\n')[:-1]
groups = []
current_group = []
for index, line in enumerate(file_content):
    if index % 3 == 0 and index != 0:
        groups.append(current_group)
        current_group = []
    current_group.append(line)

groups.append(current_group)
print(groups)
stuff = []
for group in groups:
    container1 = set(group[0])
    container2 = set(group[1])
    container3 = set(group[2])
    hi = container2.intersection(container1).intersection(container3)
    print(hi)
    
    asc = ord(hi.pop())
    if asc <= 90:
        val = asc - 64 + 26
    else:
        val = asc - 96
    stuff.append(val)
print(len(stuff))
print(sum(stuff))