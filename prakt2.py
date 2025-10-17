def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")
        try:
            result = func(*args, **kwargs)
            print(f"Функция {func.__name__} вернула {result}")
            return result
        except Exception as e:
            print(f"Функция {func.__name__} вызвала исключение: {e}")
            raise
    return wrapper

@logger
def add(a, b):
    return a + b

@logger
def divide(a, b):
    return a / b

@logger
def greet(name):
    return f"Привет, {name}!"

# Примеры вызова
add(5, 3)
divide(10, 2)
try:
    divide(5, 0)
except ZeroDivisionError:
    print("Обработали деление на ноль")
greet("Анна")