def calculate(base, height):
    print("__name__:", __name__)
    return 1 / 2 * (base * height)


if "__name__" == "__main__":
    print("I am in first main")
    area = calculate(4, 5)
    print("Area becomes: ", area)