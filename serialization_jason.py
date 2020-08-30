import json


def json_writer():
    names = [
        {'name': 'Anna'},
        {'name': 'Ala'}
    ]

    try:
        with open("./text.json", "w") as file_descriptor:
            json.dump(names, file_descriptor)
    except (IOError, json.JSONDecodeError, BaseException) as e:
        print(f"name error; more infor {e.args}")


def json_reader():
    output_json = []
    try:
        with open("./text.json", 'r') as file_descriptor:
            output_json = json.load(file_descriptor)
            print(output_json)
    except (IOError, json.JSONDecodeError, BaseException) as e:
        print(f"name error; more infor {e.args}")
    print(output_json)


def main():
    json_writer()
    json_reader()


if __name__ == "__main__":
    main()
