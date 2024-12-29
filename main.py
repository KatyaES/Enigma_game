import random

def func():
    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{};:'|,.<>/?"
    password = input("Enter password: ")
    length_password = len(password)
    counts = 0
    enigma = ''.join(random.choices(symbols, k=length_password))
    while enigma != password:
        enigma = ''.join(random.choices(symbols, k=length_password))
        counts = counts + 1
        print(enigma, counts)
    print(f'Your password: {password}\nEnigma: {enigma} Total selected: {counts}')
func()

