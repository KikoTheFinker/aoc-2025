def read(filename: str):
    with open(filename, "r") as file:
        return [line.strip() for line in file]


def calculate_area(x1: int, y1: int, x2: int, y2: int):
    width = abs(x1 - x2) + 1
    height = abs(y1 - y2) + 1
    return width * height


def solve():
    pairs = read("input.txt")
    maximum_area = 0

    for i in range(len(pairs)):
        x1_str, y1_str = pairs[i].split(",")
        x1, y1 = int(x1_str), int(y1_str)

        for j in range(i + 1, len(pairs)):
            x2_str, y2_str = pairs[j].split(",")
            x2, y2 = int(x2_str), int(y2_str)

            area = calculate_area(x1, y1, x2, y2)
            if area > maximum_area:
                maximum_area = area

    print(maximum_area)


if __name__ == "__main__":
    solve()
