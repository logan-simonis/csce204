num = 0
with open("examples/mar29/text.txt") as file:
    for line in file:
        num = int(line.strip())
        break

num += 1

with open("examples/mar29/text.txt", "w") as file:
    file.write(f"{num}\n")
