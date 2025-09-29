import time
from functools import wraps

def timer(func):
    """Декоратор: печатает время работы функции"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t1 = time.time()
        print(f"[timer] {func.__name__} заняла {t1 - t0:.6f} сек")
        return result
    return wrapper

def debug(func):
    """Декоратор: выводит имя функции и её аргументы"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[debug] {func.__name__} args={args} kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

def safe_nan(func):
    """Декоратор: ловит ошибки и возвращает NaN вместо падения программы"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[safe_nan] {func.__name__}: {e}")
            return float("nan")
    return wrapper

if __name__ == "__main__":
    @timer
    @debug
    @safe_nan
    def test(x):
        return 10 / x

    print(test(2))
    print(test(0))