def read(filename):
    ranges = []

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            ranges.append(list(map(int, line.split("-"))))

    return ranges


def solve():
    ranges = read("input.txt")
    ranges = sorted(ranges, key=lambda x: x[0])

    i = 0
    while i < len(ranges) - 1:
        a, b = ranges[i]
        na, nb = ranges[i + 1]

        if na <= b and nb <= b:
            ranges.pop(i + 1)
            continue

        if na <= b < nb:
            ranges[i][1] = nb
            ranges.pop(i + 1)
            continue

        i += 1

    numbers = sum(b - a + 1 for a, b in ranges)

    print(numbers)
    print(ranges)


if __name__ == '__main__':
    solve()
