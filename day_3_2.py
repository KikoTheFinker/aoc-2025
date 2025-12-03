def solve(filename):
    total = 0

    with open(filename, "r") as f:
        for line in f:
            battery = line.strip()
            needed = 12
            remove = len(battery) - 12

            stack = []

            for i in range(len(battery)):
                for j in range(len(battery)):
                    digit = int(battery[j])
                    while remove > 0 and stack and digit > stack[-1]:
                        stack.pop()
                        remove -= 1
                    stack.append(digit)
                while remove > 0:
                    stack.pop()
                    remove -= 1
            stack = stack[:12]

            battery_number = ''.join(str(x) for x in stack)
            print(battery_number)
            total += int(battery_number)

    print(total)


if __name__ == "__main__":
    solve("input.txt")
