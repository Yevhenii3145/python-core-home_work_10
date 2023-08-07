from collections import UserDict
import typing

class Field():
    def __init__(self, value):
        self.value = value

class Name(Field):
    def __init__(self, name:str):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone:int):
        super().__init__(phone)


class Record():
    def __init__(self, name:Name, phone=None):
        self.name = name
        self.phone = Phone(phone)
        self.phones = []

    def add_phone(self, phone:int):
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone:int):
        index = self.find_phone_index(phone)
        if index is not None:
            self.phones.pop(index)

    def edit_phone(self, old_phone:int, new_phone:int):
        index = self.find_phone_index(old_phone)
        if index is not None:
            self.phones[index] = Phone(new_phone)

    def find_phone_index(self, phone:int):
        for index, p in enumerate(self.phones):
            if p.value == phone:
                return index
        return None

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

PHONE_BOOK = AddressBook()


def input_error(func: typing.Callable) -> typing.Callable:
    def inner(*args: str, **kwargs: dict) -> str:
        try:
            return f"{func(*args, **kwargs)}"
        except (KeyError, ValueError, IndexError, TypeError) as error:
            return f"DECORATOR An error has occurred. Er: {error}"
    return inner


@input_error
def say_hello() -> str:
    return "How can I help you?"


@input_error
def add_user(name: str, phone_num: str) -> str:
    name_user = Name(name)
    if name_user.value in PHONE_BOOK:
        PHONE_BOOK[name_user.value].add_phone(phone_num)
        return f"In phone book added user '{name}' with phone '{phone_num}'"
    else:
        record = Record(name_user, phone_num)
        PHONE_BOOK.add_record(record)
        return f"In phone book field user '{name}' added phone '{phone_num}'"


@input_error
def change_contact(name: str, old_phone: int, new_phone: int) -> str:
    if name not in PHONE_BOOK:
        raise ValueError(f"User '{name}' is not in the phone book")
    PHONE_BOOK[name].edit_phone(old_phone, new_phone)
    return f"In the phone book changed phone number '{old_phone}' of user '{name}' to '{new_phone}'"


@input_error
def to_delete(name: str, phone: int):
    if name not in PHONE_BOOK:
        raise ValueError(f"User '{name}' is not in the phone book")
    PHONE_BOOK[name].remove_phone(phone)
    return f"In the phone book deleted phone number '{phone}' of user '{name}'"


@input_error
def get_phone(name: str) -> str:
    if name not in PHONE_BOOK:
        raise ValueError(f"User '{name}' is not in the phone book.")
    return f"Target phone number for user '{name}' is '{', '.join(str(p.value) for p in PHONE_BOOK[name].phones)}'"


@input_error
def show_all() -> str:
    if not PHONE_BOOK:
        return "The phone book is empty."
    result = "show_all:\n"
    for name in PHONE_BOOK:
        result += f"{name}: {', '.join(str(p.value) for p in PHONE_BOOK[name].phones)}\n"
    return result


@input_error
def to_close() -> str:
    return "Good bye!"


def default_handler(*args) -> str:
    return f"I don't know such a command"


COMANDS: dict[str, typing.Callable] = {
    'hello': say_hello,
    'add': add_user,
    'change': change_contact,
    'phone': get_phone,
    'show all': show_all,
    'close': to_close,
    'delete': to_delete,
}


def get_handler(command: str) -> typing.Callable:
    return COMANDS.get(command, default_handler)


def main() -> None:
    print("I'm a Bot")
    while True:
        user_input = input("Please input a command: ").lower()

        if user_input in ["good bye", "close", "exit"]:
            handler = get_handler('close')
            request_data = user_input.replace('good bye', "").replace("close","").replace("exit","").strip()
            print(handler(request_data))
            break

        elif 'show all' in user_input:
            handler = get_handler('show all')
            request_data = user_input.replace('show all', "").strip()
            print(handler(request_data))
            continue

        list_of_request = user_input.strip().split(' ')
        command = list_of_request[0]
        request_data = list_of_request[1:]

        print("REQUEST DATA", request_data)

        handler = get_handler(command)
        print(handler(*request_data))


if __name__ == "__main__":
    main()
