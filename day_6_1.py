def read(filename):
    grid = []

    with open(filename) as f:
        for line in f:
            row = []
            for token in line.split():
                row.append(int(token) if token.isdigit() else token)
            grid.append(row)

    return grid


def solve():
    grid = read("input.txt")

    n = len(grid)
    m = len(grid[0])
    numbers = []

    for j in range(m):
        operator = grid[n - 1][j]
        number = grid[0][j]

        for i in range(1, n - 1):
            value = grid[i][j]
            if operator == "+":
                number += value
            elif operator == "*":
                number *= value

        numbers.append(number)

    print(sum(numbers))


if __name__ == '__main__':
    solve()
