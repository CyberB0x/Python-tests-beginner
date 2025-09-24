from formatter.phone_formatter import format_phone_number

if __name__ == "__main__":
    raw_input = input("Введите номер телефона: ")

    formatted  =format_phone_number(raw_input)

    print("Отформатированный номер:", formatted)
