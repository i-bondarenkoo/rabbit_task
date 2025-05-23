import time


list_words = ["banana", "pineapple", "12", "jin", "cucumber"]


def log_call(verbose):
    def get_name(func):
        def wrapper(*args, **kwargs):
            if verbose:
                print(
                    f"Вызов функции: {func.__name__} c аргументами {','.join(map(str, args))}"
                )

            return func(*args, **kwargs)

        return wrapper

    return get_name


@log_call(verbose=True)
def filter_and_uppercase_words(list_words: list):
    return [item.upper() for item in list_words if len(item) > 3]


def get_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        time.sleep(2)
        stop = time.time() - start
        return f"Время выполнения функции составило: {stop}, результат: {result}"

    return wrapper


@get_time
def pow_digit(list_digit):
    return [x**2 for x in list_digit]


def file_name(name_f):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            if isinstance(name_f, str):
                filename = name_f if name_f.endswith(".txt") else name_f + ".txt"
                with open(file=filename, mode="w", encoding="utf-8") as file:
                    result = f"Название вызванной функции: {func.__name__}, время вызова функции: {time.time()}"
                    file.write(result)
            return func(*args, **kwargs)

        return wrapper

    return real_decorator


@file_name(name_f="report")
def get_len_string(list_string):
    return [len(elem) for elem in list_string]


def make_multiplier(n):

    def inner(x):
        result = x * n
        return result

    return inner


def call_counter(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        return f"Функция была вызвана {count} раз, результат функции: {func(*args, **kwargs)}"

    return wrapper


@call_counter
def greet(name):
    return f"Privet, {name}"


if __name__ == "__main__":
    print(pow_digit([2, 7, -4, 2, 0, 5]))
    result = get_time(pow_digit)
    print(result([2, 7, -4, 2, 0, 5]))
    print(get_len_string(["a", "sasad", "sadasdasdads"]))
    test_decorator = file_name("report")(get_len_string)
    print(test_decorator(["a", "sasad", "sadasdasdads"]))
    test = make_multiplier(3)
    print(test(5))
    print(test(7))
    print(greet("Jopa"))
    print(greet("123"))
    test_func = call_counter(greet)
    print(test_func("stepa"))
    print(test_func("grisha"))
