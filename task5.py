# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0

def remake(equation):
    dictEquation = {}
    equation = equation.replace(' - ', ' -').replace(' + ', ' +')[:-4]
    equation = equation.split(' ')
    for value in equation:
        value = value.replace('+', '').split('x**')
        dictEquation[int(value[1])] = int(value[0])
    return dictEquation


def sumEquation(dict1, dict2):
    dictFinal = {}
    for key in list(dict1.keys()) + list(dict2.keys()):
        first = dict1.get(key, 0)
        second = dict2.get(key, 0)
        if first or second:
            dictFinal[key] = first + second
    return dictFinal


def coefResult(dictFinal):
    result = ''
    for i in dictFinal.items():
        result += (' - ' if i[1] < 0 else ' + ') + str(abs(i[1])) + 'x^' + str(abs(i[0]))
        result = result.replace('x^1 ', 'x ').replace('x^0', '').replace(' 1x^', ' x^')
        if result.startswith(' '):
            result = result[3:]
    return result + ' = 0'


def read_polynom(filename):
    with open(filename, 'r') as text:
        equation = text.readline()

    return equation


equation = read_polynom('file1task5.txt')
equation2 = read_polynom('file2task5.txt')

print(equation)
print(equation2)
dictEquation = remake(equation)
dictEquation2 = remake(equation2)
print(dictEquation)
print(dictEquation2)

dictFinal = sumEquation(dictEquation, dictEquation2)
print(dictFinal)

dictFinal = coefResult(dictFinal)
print(dictFinal)
with open('file3task5.txt', 'w') as text:
    text.writelines(dictFinal)
