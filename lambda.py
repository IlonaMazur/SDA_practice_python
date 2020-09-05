from decimal import Decimal


def lambda_ex1():
    names = ['Ala', 'Max', 'Bogdan', 'Krystyna', 'Kunegunda']
    print("result a")
    result_a = sorted(names, key=lambda name: len(name))
    print(result_a)

    print('result b')
    result_b = sorted(names, key=lambda name: len(name), reverse=True)
    print(result_b)

    print('result c')
    result_c = sorted(names, key=lambda name: name[0] if len(name) > 0 else " ")
    print(result_c)

    print('result c*')
    result_c_ = sorted(names, key=lambda name: name)
    print(result_c_)


class BankAccount:
    def __init__(self, name: str, balance: Decimal):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name} - {self.balance}"


def lambda_ex2_ex3():
    account1 = BankAccount('1', Decimal(1000))
    account2 = BankAccount('2', Decimal(4000))
    account3 = BankAccount('3', Decimal(5000))
    account4 = BankAccount('4', Decimal(7000))
    account5 = BankAccount('5', Decimal(10000))
    accounts = [account1, account2, account3, account4, account5]
    print("exercise 2")
    filtered_accounts = list(filter(lambda account: account if account.balance > Decimal(4500) else None, accounts))
    for account in filtered_accounts:
        print(account)

    print('exercise 3')
    max_account = max(accounts, key=lambda account: account.balance)
    print(max_account)


def main():
    lambda_ex1()
    lambda_ex2_ex3()


if __name__ == "__main__":
    main()

# dokończ zadania 4 i 5