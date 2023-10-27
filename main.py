import assistant
from addressBook import AddressBook


def main():
    book = AddressBook()
    book.load()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = assistant.parse_input(user_input)
        if command in ["close", "exit", "bye", "q"]:
            book.save()
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(assistant.add_contact(args, book))
        elif command == "all":
            print(assistant.show_all(book))
        elif command == "change":
            print(assistant.change_contact(args, book))
        elif command == "phone":
            print(assistant.show_phone(args, book))
        elif command == "add-birthday":
            print(assistant.add_birthday(args, book))
        elif command == "show-birthday":
            print(assistant.show_birthday(args, book))
        elif command == "birthdays":
            print(assistant.birthdays(book))
        else:
            print(f"Invalid command.{command}")


if __name__ == "__main__":
    main()
