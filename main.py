import random
import time
def func():
    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    print('Your password can only consist of letters and numbers')
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
    seconds = end_time - time_start
    if seconds < 60:
        print(f'Your password: {password}\nEnigma: {enigma} \nTotal selected: {counts}\nTime: {round(seconds, ndigits=2)} sec')
    elif seconds % 60 == 0:
        minutes = seconds // 60
        print(f'Your password: {password}\nEnigma: {enigma} \nTotal selected: {counts}\nTime: {minutes} min')
    else:
        minutes = seconds // 60
        sec = seconds % 60
        print(f'Your password: {password}\nEnigma: {enigma} \nTotal selected: {counts}\nTime: {minutes} min, {round(sec, ndigits=1)} sec')
func()

