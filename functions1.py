import random
from itertools import permutations

def grams_to_ounces(grams):
    return grams * 28.3495231  # Просто умножаем граммы на коэффициент перевода

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9  # Используем стандартную формулу перевода

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if chickens * 2 + rabbits * 4 == numlegs:
            return chickens, rabbits  # Возвращаем найденное количество
    return None  # Если решения нет

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes  # Возвращаем список простых чисел

def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])  # Разбиваем, переворачиваем и соединяем обратно

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False  # Проверяем, есть ли подряд идущие тройки

def spy_game(nums):
    found_zeros = 0
    for num in nums:
        if num == 0 and found_zeros < 2:
            found_zeros += 1
        elif num == 7 and found_zeros == 2:
            return True
    return False

def sphere_volume(radius):
    return (4 / 3) * 3.14159 * (radius ** 3)  # Формула объёма сферы

def unique_elements(lst):
    unique_lst = []
    for elem in lst:
        if elem not in unique_lst:
            unique_lst.append(elem)
    return unique_lst

def is_palindrome(word):
    return word == word[::-1]  # Проверяем, читается ли слово одинаково в обе стороны

def histogram(lst):
    for num in lst:
        print('*' * num)  # Просто печатаем звёздочки по количеству

def guess_the_number():
    name = input("Привет! Как тебя зовут?\n")
    number = random.randint(1, 20)
    print(f"\n{ name }, я загадал число от 1 до 20.")
    guesses = 0
    while True:
        guess = int(input("Попробуй угадать.\n"))
        guesses += 1
        if guess < number:
            print("Слишком маленькое.")
        elif guess > number:
            print("Слишком большое.")
        else:
            print(f"Молодец, { name }! Ты угадал число за { guesses } попыток!")
            break

# Создаём файл для тестирования импортов
with open("import_test.py", "w") as f:
    f.write("from python_functions import grams_to_ounces, fahrenheit_to_celsius, solve\n")
    f.write("print(grams_to_ounces(10))\n")
    f.write("print(fahrenheit_to_celsius(100))\n")
    f.write("print(solve(35, 94))\n")
