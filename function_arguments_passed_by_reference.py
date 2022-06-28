def append_number(numbers):
    numbers.append(5)


def main():
    items = [1, 2, 3, 4]

    append_number(items)

    print(f"after: {items}")


if __name__ == '__main__':
    main()


