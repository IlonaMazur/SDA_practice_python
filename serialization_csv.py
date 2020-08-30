import csv


def csv_write():
    users = [("Ala", "Summer", "8938273890666"),
             ("Adam", "Garden", "7303439999777")]
    try:
        with open("./text,csv", "w") as file_descriptor:
            writer = csv.writer(file_descriptor)
            for user in users:
                writer.writerow(user)
    except (IOError, csv.Error, BaseException) as e:
        print(f"You have an error; more info at{e.args}")


def csv_read():
    users = []
    try:
        with open("./text,csv", "r") as file_descriptor:
            csv_reader = csv.reader(file_descriptor)
            for row in csv_reader:
                if row:
                    users.append(row)
    except (IOError, csv.Error, BaseException) as e:
        print(f"You have an error; more info at{e.args}")
    print(users)


def main():
    csv_write()
    csv_read()


if __name__ == "__main__":
    main()
