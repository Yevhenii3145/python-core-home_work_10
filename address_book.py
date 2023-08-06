from collections import UserDict


class Field():
    pass

class Name(Field):
    def __init__(self,name):
        self.value=name


class Phone(Field):
    def __init__(self,phone):
        self.value=phone


class Record():
    #Name = Name()
    #Phone = [Phone(),]
    def __init__(self,name,phone):
        self.name = name
        self.phone = [phone]

    def add_field(self,phone):
        self.phone.append(phone)

    def remove_field(self,phone):
        pass

    def editing_field(self,field):
        pass

class AddressBook(UserDict):
    def add_record(self, record):
        self.data.name.value = record
