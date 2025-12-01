def solve(filename):
    zero_hits = 0
    position = 50

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            is_right = (line[0] == "R")
            amount = int(line[1:])

            if is_right:
                position = (position + amount) % 100
            else:
                position = (position - amount) % 100

            zero_hits += (position == 0)

    return zero_hits


if __name__ == '__main__':
    print(solve("input.txt"))
