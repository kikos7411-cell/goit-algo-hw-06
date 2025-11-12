from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):

    def __init__(self, value):

        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)
    pass

class Phone(Field):
    def __init__(self, value):

        if not value or not value.isdigit() or len(value) != 10:
            raise ValueError("Phone cannot be empty")
        super().__init__(value)

    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)
        if phone not in self.phones:
            self.phones.append(phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def remove_phone(self, phone):
        p = self.find_phone(phone)
        if p.value == phone:
            self.phones.remove(p)
            return True
        return False

    def edit_phone(self, phone, new_p ):
        p = self.find_phone(phone)
        if not p:
            raise ValueError("Old phone number not found")
        new_p = Phone(new_p)
        

    

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
 
    pass

