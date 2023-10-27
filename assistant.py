from addressBook import Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please"
        except KeyError:
            return "User not found"
        except IndexError:
            return "Enter user name"
        except Exception:
            return "Please enter right command"

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def validate_args(args):
    if len(args) != 2 or not args[1].isdigit():
        return False
    return True


@input_error
def add_contact(args, book):
    if not validate_args(args):
        raise ValueError
    name, phone = args
    contact = book.find(name)
    if contact:
        contact.add_phone(phone)
        return "phone added successfully"
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return f"Contact: {name} was added."


@input_error
def change_contact(args, book):
    name, old_phone, new_phone = args
    if not book.find(name):
        return "Contact not found."
    else:
        contact = book.find(name)
        contact.edit_phone(old_phone, new_phone)
    return f"Contact: {name} was updated."


@input_error
def show_phone(args, book):
    name = args[0]
    contact = book.find(name)
    if contact:
        return contact
    else:
        return f"Name: {name} not found!"


@input_error
def show_all(book):
    formatted_list = []
    if not book.data:
        raise Exception
    for name, record in book.data.items():
        formatted_list.append(f"{name}: {record}\n")

    return "".join(formatted_list)


@input_error
def add_birthday(args, book):
    name = args[0]
    birthday = args[1]
    contact = book.find(name)
    if contact:
        contact.add_birthday(birthday)
        return "Birthday added"
    else:
        return f"Contact: {name} not found!"


@input_error
def show_birthday(args, book):
    name = args[0]
    contact = book.find(name)
    if contact and contact.birthday:
        return contact.birthday.value
    else:
        return "Birthday not found."


@input_error
def birthdays(book):
    return book.get_birthdays_per_week()


if __name__ == "__main__":
    print("Welcome to the assistant function!")
