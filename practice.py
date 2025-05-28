# # отсортировать список по количеству гласных в слове
# words = ["banana", "apple", "cherry", "kiwi", "grape", "orange"]


# def sorted_list(l: list):
#     return sorted(
#         words, key=lambda word: sum(char in "aeiou" for char in word), reverse=True
#     )


# print(sorted_list(words))


# numbers = [1, 2, 3, 4, 6, 8, 9, 12, 15, 18, 20]


# def sort_num(lst: list):
#     gen = (x**2 for x in numbers if x % 2 == 0 and x % 3 == 0)
#     return list(gen)


# print(sort_num(numbers))

# Дан список слов. Построй словарь, где ключ — слово, а значение — количество его вхождений.
# Затем отсортируй словарь по убыванию частоты


# words2 = ["apple", "banana", "apple", "cherry", "banana", "apple", "kiwi"]


# def make_new_dict(a):
#     new_d = {elem: words2.count(elem) for elem in set(words2)}
#     return sorted(new_d.items(), key=lambda x: x[1])


# print(make_new_dict(words2))


# people = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 17},
#     {"name": "Charlie", "age": 30},
#     {"name": "Dave", "age": 15},
# ]


# def other_filter(a):
#     return [x["name"].upper() for x in people if x["age"] > 18]


# print(other_filter(people))

# words = ["banana", "apple", "cherry", "kiwi", "grape", "orange"]


# def filter_list(a):
#     return sorted(words, key=lambda x: sum(char not in "aeiou" for char in x))


# print(filter_list(words))

# words2 = ["apple", "banana", "apple", "cherry", "banana", "apple", "kiwi"]


# def filter_word(b):
#     return {x: len(set(x)) for x in set(words2)}


# print(filter_word(words2))

# Дан список строк. Нужно вернуть список тех строк, в которых буква "e" встречается ровно 2 раза
# words = ["tree", "free", "elephant", "bee", "seed", "keep"]


# def filter_str(a):
#     return [elem for elem in words if elem.count("e") == 2]


# print(filter_str(words))

# # Дан список чисел. Нужно вернуть словарь, где ключ — число, а значение — сумма его делителей (кроме самого числа)
# numbers = [6, 10, 15, 28]


# def nums(b):
#     return {n: sum(num for num in range(1, n) if n % num == 0) for n in numbers}


# print(nums(numbers))
# Дан список слов. Верни самое длинное слово, у которого чётное количество букв. Если таких несколько — вернуть первое по порядку.
words = ["car", "banana", "kiwi", "peach", "grapefruit", "melon"]


def filter_str(a):
    words_list = [word for word in words if len(word) % 2 == 0]
    return max(words_list, key=len) if words_list else None


print(filter_str(words))

words1 = ["apple", "banana", "cherry", "kiwi", "plum"]


def func1(s):
    return sorted(words1, key=lambda word: len(set(word)), reverse=True)


print(func1(words1))
