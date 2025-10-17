# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")
#         try:
#             result = func(*args, **kwargs)
#             print(f"Функция {func.__name__} вернула {result}")
#             return result
#         except Exception as e:
#             print(f"Функция {func.__name__} вызвала исключение: {e}")
#             raise
#     return wrapper
#
# @logger
# def add(a, b):
#     return a + b
#
# @logger
# def divide(a, b):
#     return a / b
#
# @logger
# def greet(name):
#     return f"Привет, {name}!"
#
# # Примеры вызова
# add(5, 3)
# divide(10, 2)
# try:
#     divide(5, 0)
# except ZeroDivisionError:
#     print("Обработали деление на ноль")
# greet("Анна")

# def require_role(allowed_roles):
#     def decorator(func):
#         def wrapper(user, *args, **kwargs):
#             if user.get('role') in allowed_roles:
#                 return func(user, *args, **kwargs)
#             else:
#                 print(f"Доступ запрещён пользователю {user['name']}")
#         return wrapper
#     return decorator
#
# @require_role(['admin'])
# def delete_database(user):
#     print(f"База данных удалена пользователем {user['name']}")
#
# @require_role(['admin', 'manager'])
# def edit_settings(user):
#     print(f"Настройки изменены пользователем {user['name']}")
#
# # Тестирование
# users = [
#     {'name': 'Анна', 'role': 'admin'},
#     {'name': 'Борис', 'role': 'manager'},
#     {'name': 'Виктор', 'role': 'user'}
# ]
#
# for user in users:
#     print(f"\nПользователь {user['name']} (роль: {user['role']}):")
#     delete_database(user)
#     edit_settings(user)