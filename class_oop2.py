class Person:
    def __init__(self, name: str, s_name: str, b_date: int):
        self._name = name
        self._s_name = s_name
        self._b_date = 0

    @property
    def set_name(self, x):
        self._name = x

    def set_surname(self, y):
        self._s_name = y

    def set_birth_date(self, z):
        self._b_date = z


def main():
    print()


if __name__ == "__main__":
    main()
