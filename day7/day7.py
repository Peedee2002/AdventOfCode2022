import pprint
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
    else:
        print("wtf ????? " + output)
def calc_dir_size(directory):
    size = 0
    for thing_name, thing_value in directory.items():
        if thing_name == '..':
            continue
        if isinstance(thing_value, dict):
            size += calc_dir_size(thing_value)
        else:
            size += thing_value
    return size

dir_sizes = []
def append_dir_sizes(name, dir):
    dir_sizes.append(calc_dir_size(dir))
    for item_name, item_value in dir.items():
        if item_name == '..':
            continue
        if isinstance(item_value, dict):
            append_dir_sizes(item_name, item_value)

append_dir_sizes('/', top_dir)
print("part 1: " + str(sum([absaga for absaga in dir_sizes if absaga <= 100000])))
# part 2
# find the size of the dir:
size_total = dir_sizes[0]
sorted_dirs = list(sorted(dir_sizes))
max_space_used = 70000000 - 30000000
space_to_free = size_total - max_space_used

possible_deletes = [direc for direc in sorted_dirs if space_to_free < direc]

print("part 2: " + str(possible_deletes[0]))