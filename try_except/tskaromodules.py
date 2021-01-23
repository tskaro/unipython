def divide(num1, num2):
    try:
        result = num1 / num2
    except:
        text = "გაყოფა შეუძლებელია"
        status = False
        return text, status
    else:
        status = True
        return result, status


def square(num1, num2):
    try:
        result = num1 ** num2
    except:
        text = "კვადრატში აყვანა შეუძლებელია"
        status = False
        return text, status
    else:
        status = True
        return result, status


if __name__ == "__main__":
    # TRUE
    print(divide(4, 2))
    print(square(4, 5))

    # FALSE
    print(divide(4, 0))
    print(square(6, "ბევრი"))
