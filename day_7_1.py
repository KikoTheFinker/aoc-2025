def read(filename):
    with open(filename, "r") as f:
        return [list(line.strip()) for line in f]


def solve():
    matrix = read("input.txt")
    m = len(matrix)
    n = len(matrix[0])
    index_s = matrix[0].index("S")
    j_falling_down = set()
    j_falling_down.add(index_s)
    split = 0

    for i in range(1, m):
        for j in range(n):
            if matrix[i][j] == "^":
                if matrix[i-1][j] == "|":
                    split+=1
                j_falling_down.discard(j)
                j_falling_down.add(j - 1)
                j_falling_down.add(j + 1)
        for j in j_falling_down:
            matrix[i][j] = "|"

    print(split)
    for row in matrix:
        print("".join(row))


if __name__ == '__main__':
    solve()
