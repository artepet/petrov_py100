#def get_random_password() -> str:  # TODO написать функцию генерации случайных паролей
import secrets
symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz0123456789'
a = int(input("Сколько символов в паролей? "))
b = int(input("Сколько паролей? "))
count = 0
passlist = []
while count < b:
    while True:
        password = ''.join(secrets.choice(symbols) for i in range(a))

        if (any(c.islower() for c in password) and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)):
            break
    count += 1
    passlist.append(password)
print(passlist)