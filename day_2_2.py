def is_invalid_id(num: int) -> bool:
    s = str(num)
    return s in (s+s)[1:-1]


def solve(filename):
    total = 0

    with open(filename, "r") as f:
        for line in f:
            ranges = line.split(",")

            for r in ranges:
                if not r:
                    continue

                start, end = map(int, r.split("-"))
                for i in range(start, end + 1):
                    if is_invalid_id(i):
                        total += i

    print(total)


if __name__ == "__main__":
    solve("input.txt")
