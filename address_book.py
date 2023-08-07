from collections import UserDict


class Field():
    def __init__(self, value):
        self.value = value


class Name(Field):
    def __init__(self, name: str):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone: str):
        super().__init__(phone)


class Record():
    def __init__(self, name: Name, phone=None):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.phones = []
        if phone:
            self.add_phone(phone)

    def add_phone(self, phone: str):
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone: str):
        index = self.find_phone_index(phone)
        if index is not None:
            self.phones.pop(index)

    def edit_phone(self, old_phone: str, new_phone: str):
        index = self.find_phone_index(old_phone)
        if index is not None:
            self.phones[index] = Phone(new_phone)

    def find_phone_index(self, old_phone: str):
        for index, phone in enumerate(self.phones):
            if phone.value == old_phone:
                return index
        return None


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


if __name__ == '__main__':
    new_contact_1 = Record("Nina", 322223322)
    new_contact_2 = Record("Olga", 1488322)
    new_contact_3 = Record("Kizaru", 666)
    new_phone_book = AddressBook()
    new_phone_book.add_record(new_contact_1)
    new_phone_book.add_record(new_contact_2)
    new_phone_book.add_record(new_contact_3)
    print(new_phone_book)
