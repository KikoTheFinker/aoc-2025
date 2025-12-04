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

    count = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != "@":
                continue

            neighbour_count = 0

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if 0 <= ni < rows and 0 <= nj < cols:
                    if matrix[ni][nj] == "@":
                        neighbour_count += 1

            if neighbour_count < 4:
                count += 1

    print(count)


if __name__ == '__main__':
    solve()
