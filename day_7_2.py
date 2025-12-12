def read(filename):
    with open(filename, "r") as f:
        return [list(line.strip()) for line in f]


def solve():
    matrix = read("input.txt")
    m = len(matrix)
    n = len(matrix[0])

    dp = [[0] * n for _ in range(m)]

    j_start = matrix[0].index("S")
    dp[0][j_start] = 1

    for i in range(m - 1):
        for j in range(n):
            if dp[i][j] == 0:
                continue

            if matrix[i][j] in {".", "S"}:
                dp[i + 1][j] += dp[i][j]

            elif matrix[i][j] == "^":
                if j - 1 >= 0:
                    dp[i + 1][j - 1] += dp[i][j]
                if j + 1 < n:
                    dp[i + 1][j + 1] += dp[i][j]

    print(sum(dp[m - 1]))


if __name__ == "__main__":
    solve()
