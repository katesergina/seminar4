# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


n = int(input('Введите число: '))

def get_prime_factors (n):
    i = 2
    lst = []
    while n != 1: 
        if n % i == 0:
            lst.append(i) 
            n = n / i
            i = 2
        else: 
            i += 1
    return (lst)

print (get_prime_factors(n))

