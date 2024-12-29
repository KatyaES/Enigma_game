import random
import time
def func():
    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{};:'|,.<>/?"
    password = input("Enter password: ")
    time_start = time.time()
    length_password = len(password)
    counts = 0
    enigma = ''.join(random.choices(symbols, k=length_password))
    while enigma != password:
        enigma = ''.join(random.choices(symbols, k=length_password))
        counts = counts + 1
        print(enigma, counts)
    end_time = time.time()
    print(f'Your password: {password}\nEnigma: {enigma} \nTotal selected: {counts}\nTime: {round(end_time-time_start, ndigits=2)} sec')
func()

