
with open("input.txt") as f:
    file_content = f.read()

string = ''

for index, char in enumerate(file_content):
    if char in string:
        # print(string)
        string = ''
    string += char
    if len(string) == 13:
        print(string)
        print(index + 1)
        exit(0)