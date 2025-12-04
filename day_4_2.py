def read(filename):
    with open(filename, "r") as f:
        return [list(line.strip()) for line in f]


def solve():
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

    matrix = read("input.txt")
    rows = len(matrix)
    cols = len(matrix[0])

    sum_of_count = 0

    while True:
        to_change = []

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] != "@":
                    continue

                neighbour_count = 0

                for di, dj in directions:
                    ni = i + di
                    nj = j + dj

                    if 0 <= ni < rows and 0 <= nj < cols:
                        if matrix[ni][nj] == "@":
                            neighbour_count += 1

                if neighbour_count < 4:
                    to_change.append((i, j))

        if not to_change:
            break

        sum_of_count += len(to_change)
        for i, j in to_change:
            matrix[i][j] = "x"

    print(sum_of_count)


if __name__ == "__main__":
    solve()
