import typing
from address_book import AddressBook, Record, Name, Phone

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
    # name_user = Name(name)
    # phone_number = Phone(phone_num)

    if name in PHONE_BOOK:
        # print(PHONE_BOOK[name_user.value])
        PHONE_BOOK[name].add_phone(phone_num)
        return f"In phone book added user '{name}' with phone '{phone_num}'"
    else:
        PHONE_BOOK[name].add_phone(phone_num)
    # PHONE_BOOK[name_user.value].add_phone(phone_number)
    return f"In phone book field user '{name}' added phone '{phone_num}'"


@input_error
def change_contact(name: str,old_phone, new_phone: str) -> str:
    if name not in PHONE_BOOK:
        raise ValueError(f"User '{name}' is not in phone book")
    PHONE_BOOK[name].edit_phone(old_phone,new_phone)
    return f"In phone book changed phone number '{old_phone}' of user '{name}' to '{new_phone}'"


@input_error
def to_delete(name, phone):
    user_name = Name(name)
    phone_number = Phone(phone)

    if name not in PHONE_BOOK:
        raise ValueError(f"User '{name}' is not in phone book")
    PHONE_BOOK[name].remove_phone(phone_number)
    return f"In phone book deleted phone number '{phone}' of user '{name}"


@input_error
def get_phone(name: str) -> str:
    if name not in PHONE_BOOK:
        raise ValueError(f"User '{name}' is not in phone book.")
    return f"Target phone number for user '{name}' is '{PHONE_BOOK[name]}'"


@input_error
def show_all() -> str:
    if not PHONE_BOOK:
        return "The phone book is empty."
    result = "show_all:\n"
    # for name, phone in PHONE_BOOK.items():
    #     result += f"{name} - {phone}\n"
    for name  in PHONE_BOOK:
        result += f"{name}: {PHONE_BOOK[name].value}"
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


def get_handler(comand: str) -> typing.Callable:
    return COMANDS.get(comand, default_handler)


def main() -> None:
    print("I'm a Bot")
    while True:
        user_input = input("Please input a command: ").lower()

        if user_input in ["good bye", "close", "exit"]:
            handler = get_handler('close')
            request_data = user_input.replace('good bye', "").replace("close","").replace("exit","").split()
            print(handler(*request_data))
            break

        elif 'show all' in user_input:
            handler = get_handler('show all')
            request_data = user_input.replace('show all', "").split()
            print(handler(*request_data))
            continue

        list_of_request = user_input.strip().split(' ')
        comand = list_of_request[0]
        request_data = list_of_request[1:]

        print("RECVEST DATA", request_data)

        handler = get_handler(comand)
        print(handler(*request_data))


if __name__ == "__main__":
    main()
