def solve(filename):
    total = 0

    with open(filename, "r") as f:
        for line in f:
            battery = line.strip()
            highest = 0
            for i in range(len(battery)):
                for j in range(i + 1, len(battery)):
                    number = int(battery[i] + battery[j])
                    highest = max(highest, number)
            total += highest
    print(total)



if __name__ == "__main__":
    solve("input.txt")