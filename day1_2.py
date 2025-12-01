def solve(filename):
    zero_hits = 0
    position = 50

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = 1 if line[0] == "R" else -1
            amount = int(line[1:])

            old = position
            new = old + direction * amount

            if new > old:
                zero_hits += new // 100 - old // 100
            elif new < old:
                zero_hits += (old - 1) // 100 - (new - 1) // 100

            position = new

    return zero_hits


if __name__ == "__main__":
    print(solve("input.txt"))
