import random
import string

def generate_password(length=8):
    if length < 4:
        raise ValueError("Длина пароля должна быть не меньше 4")

    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Введите длину пароля: "))
    pw = generate_password(length)
    print("Сгенерированный пароль: ", pw)