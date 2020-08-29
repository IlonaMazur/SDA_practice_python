

def exceptions_f1():
    nums = [0, 2, 3, 4, 5]
    print(nums[5])


def exceptions_f2(name: str):
    if len(name):
        raise ValueError("empty name is invalid")

def exception_f3 (value1: int, value2: int):
    return value1 / value2

def main():
    try:

        exceptions_f1()
    except IndexError as e:
        print(f"my bug, more infor: {e.args}")

    try:
        exceptions_f2("")
    except ValueError as e:
        print(f"new bug")

    try:
        exception_f3(10, 1)
    except ZeroDivisionError as e:
        print (f" next bug, more info in {e.args}")

if __name__ == "__main__":
    main()

#zadanie 1, 2, 3 z exceptions exercises