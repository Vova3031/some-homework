def is_even(number):
    return number % 2 == 0

def count_vowels(input_string):
    vowels = "aeiou"
    input_string = input_string.lower()
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

def factorial(n):
    if n < 0:
        return "Факторіал визначений тільки для невід'ємних цілих чисел."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Приклади використання функцій:
number = 6
string = "Hello, World"
n_factorial = 5

is_even_result = is_even(number)
vowels_count = count_vowels(string)
factorial_result = factorial(n_factorial)

print(f"Число {number} парне: {is_even_result}")
print(f"Кількість голосних у рядку '{string}': {vowels_count}")
print(f"Факторіал числа {n_factorial}: {factorial_result}")
