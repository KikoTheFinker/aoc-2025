def read(filename):
    ranges = []
    ingredients = []
    in_ingredients = False

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()

            if not in_ingredients:
                if not line:
                    in_ingredients = True
                else:
                    ranges.append(list(map(int, line.split("-"))))
            else:
                if line:
                    ingredients.append(int(line))

    return ranges, ingredients


def solve():
    ranges, ingredients = read("input.txt")

    result = {
        ingredient
        for ingredient in ingredients
        if any(r[0] <= ingredient <= r[1] for r in ranges)
    }

    print(len(result))


if __name__ == "__main__":
    solve()
