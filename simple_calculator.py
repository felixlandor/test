def add(left, right):
    return left + right


def multiply(left, right):
    return left * right


if __name__ == "__main__":
    first_number = 6
    second_number = 7
    print(f"{first_number} + {second_number} = {add(first_number, second_number)}")
    print(f"{first_number} * {second_number} = {multiply(first_number, second_number)}")
