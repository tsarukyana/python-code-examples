def smart_divide(func):
    def inner(a, b):
        print("Dividing", a, "by", b)
        if b == 0:
            print("Make sure Denominator is not zero")
            return
        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    print(a / b)


result = divide(1, 0)

print(result)
