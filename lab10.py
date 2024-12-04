import math

def my_log(numbers):
    result = []
    for num in numbers:
        if num > 0:
            result.append(math.log(num))
        else:
            result.append(None)
    return result

test_list = [1, 3, 2.5, -1, 9, 0, 2.71]
print(my_log(test_list))

def name_age_opeeations(names, ages):
    if len(names) == len(ages):
        return dict(zip(names, ages)) #zip создает кортежи для каждой пары элементов
    else:
        print("Списки имеют разную длину")
        return {}

names = ["Ann", "Tim", "Sam"]
ages = [12, 23, 17]
print(name_age_opeeations(names, ages))

names = ["Ann", "Tim", "Sam"]
ages = [12, 23, 17, 45]
print(name_age_opeeations(names, ages))

def binomial_coef(n, k):
    # Вычисляет биномиальный коэффициент C(n, k)
    # n: общее количество испытаний
    # k: количество успехов
    # Возвращает значение биномиального коэффициента

    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def binom_prob(p, n, k):
    # p: вероятность успеха в одном испытании
    # n: общее количество испытаний
    # k: количество успехов
    # Возвращает вероятность получения ровно k успехов
    
    if not (0 <= p <= 1):
        raise ValueError("Вероятность p должна быть в пределах от 0 до 1")
    if not (0 <= k <= n):
        raise ValueError("Количество успехов k должно быть в пределах от 0 до n")
    
    coef = binomial_coef(n, k)
    return coef * (p ** k) * ((1 - p) ** (n - k))

print(binom_prob(0.5, 10, 3))

def all_sort(*args):
    numbers = list(args)

    # Сортировка пузырьком
    for i in range(len(numbers)): # Число итераций чтобы отсортировать все элементы
        for j in range(0, len(numbers) - 1 - i): # В конце итерации в конец идёт самое большое число, уменьшаем кол-во элементов для сравнения на i
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers

print(all_sort(7, 6, 1, 3, 8, 0, -2))