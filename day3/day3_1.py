with open("input.txt") as f:
    file_content = f.read().split('\n')[:-1]

stuff = []
for compartment in file_content:
    container1 = set(compartment[:int(len(compartment)/2)])
    container2 = set(compartment[int(len(compartment)/2):])
    hi = container2.intersection(container1).pop()
    asc = ord(hi)
    if asc <= 90:
        val = asc - 64 + 26
    else:
        val = asc - 96
    print(val)
    stuff.append(val)
print(sum(stuff))