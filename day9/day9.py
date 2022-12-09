class Head():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def move(self, direction: str):
        if direction == 'U':
            self.y += 1
        elif direction == 'D':
            self.y -= 1
        elif direction == 'L':
            self.x -= 1
        elif direction == 'R':
            self.x += 1

        return (self.x, self.y)

class Tail():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.visited = set([(0, 0)])
    def follow(self, headX, headY):
        # nesting is to allow for diagonal, i can probably improve that behavior
        if headX - self.x > 1:
            self.x += 1
            if headY - self.y > 0:
                self.y += 1
            elif self.y - headY > 0:
                self.y -= 1
        elif self.x - headX > 1:
            self.x -= 1
            if headY - self.y > 0:
                self.y += 1
            elif self.y - headY > 0:
                self.y -= 1

        if headY - self.y > 1:
            self.y += 1
            if headX - self.x > 0:
                self.x += 1
            elif self.x - headX > 0:
                self.x -= 1
        elif self.y - headY > 1:
            self.y -= 1
            if headX - self.x > 0:
                self.x += 1
            elif self.x - headX > 0:
                self.x -= 1
        self.visited.add((self.x, self.y))
        return (self.x, self.y)

with open("input.txt") as f:
    file_content = f.read().split('\n')[:-1]

head = Head()
tails = [Tail(), Tail(), Tail(), Tail(), Tail(), Tail(), Tail(), Tail(), Tail()]
for line in file_content:
    direction, distance = line.split(" ")
    for _ in range(int(distance)):
        head_place = head.move(direction)
        place_to_move = head_place
        for tail in tails:
            place_to_move = tail.follow(place_to_move[0], place_to_move[1])


print("part 1:", len(tails[0].visited))
print("part 2:", len(tails[-1].visited))
