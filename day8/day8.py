with open("input.txt") as f:
    file_content = f.read().split('\n')[:-1]
grid = [[int(tree) for tree in line] for line in file_content]

def visible(tree, x, y):
    # row from left
    if max(grid[x][0:y] + [-1]) < tree:
        return True
    if max(grid[x][y + 1:] + [-1]) < tree:
        return True
    # column from top
    if max([row[y] for row in grid][0:x] + [-1]) < tree:
        return True
    # column to bottom
    if max([row[y] for row in grid][x + 1:] + [-1]) < tree:
        return True
    return False

def count_seen(list, tree):
    count = 0
    for val in list:
        if val >= tree:
            count += 1
            break
        else:
            count += 1
    return count

def scene(tree, x, y):
    return count_seen(reversed(grid[x][0:y]), tree) * count_seen(grid[x][y + 1:], tree) * count_seen(reversed([row[y] for row in grid][0:x]), tree) * count_seen([row[y] for row in grid][x + 1:], tree)
    

total_visible = 0
best_view = 0
for x, row in enumerate(grid):
    for y, tree in enumerate(row):
        if visible(tree, x, y):
            total_visible += 1
        scenery = scene(tree, x, y)
        if scenery > best_view:
            best_view = scenery
print(total_visible)
print(best_view)