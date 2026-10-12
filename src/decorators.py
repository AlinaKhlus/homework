import functools


# декоратор для логирования
def log(filename=None):
    """декоратор log автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие
    ошибки. Декоратор принимет необязательный аргумент filename, который определяет, куда будут записываться
    логи (в файл или в консоль):"""
    def _write_log(message):
        if filename:
            with open(filename, "a") as f:
                f.write(message + "\n")
        else:
            print(message)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            try:
                result = func(*args, **kwargs)
                _write_log(f"{func_name} ok")
                return result
            except Exception as e:
                _write_log(f"{func_name} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                return None

        return wrapper

    return decorator
