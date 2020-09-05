class Person:
    def __init__(self, name: str, s_name: str, b_date: int) -> str:
        self._name = name
        self._s_name = s_name
        self._b_date = b_date

    @property
    def set_name(self, Adam):
        self._name = Adam

    def set_surname(self, Kowalski):
        self._s_name = Kowalski

    def set_b_date(self, March):
        self._b_date = March


def main():
    print(f" Mr {name}")


if __name__ == "__main__":
    main()
