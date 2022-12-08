with open("input.txt") as f:
    file_content = f.read().split('\n')[1:-1] # ignore the cd /
top_dir = {}
curr_dir = top_dir
my_iter = iter(enumerate(file_content))
for index, output in my_iter:
    if output == '$ ls':
        index, output = next(my_iter)
        while True:
            size, name = output.split(' ')
            if size == 'dir':
                curr_dir[name] = {'..': curr_dir}
            else:
                curr_dir[name] = int(size)
            if index + 1 != len(file_content) and not file_content[index + 1].startswith('$'):
                index, output = next(my_iter)
            else:
                break
    elif output.startswith('$ cd'):
        _, _, goto = output.split(' ')
        curr_dir = curr_dir[goto]

def calc_dir_size(directory):
    size = 0
    for thing in directory.keys():
        if thing == '..':
            continue
        if isinstance(directory[thing], dict):
            size += calc_dir_size(directory[thing])
        else:
            size += directory[thing]
    return size

dir_sizes = {}
def append_dir_sizes(name, dir):
    dir_sizes[name] = calc_dir_size(dir)
    for items in dir.keys():
        if items == '..':
            continue
        if isinstance(dir[items], dict):
            append_dir_sizes(items, dir[items])

append_dir_sizes('/', top_dir)
print(dir_sizes)
print([absaga for absaga in dir_sizes.values() if absaga <= 100000])