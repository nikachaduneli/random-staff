import datetime
from functools import lru_cache


@lru_cache #caching for speed
def fibonacci_recursive(x: int) -> int:
    if x == 1 or x == 2:
        return 1
    return fibonacci_recursive(x-1) + fibonacci_recursive(x-2)


def fibonacci_with_loop(x: int) -> int:
    counter: int = 1
    first: int = 0
    second: int = 1
    third: int = 0
    while counter != x:
        third = second + first
        first = second
        second = third
        counter += 1
    return third

def time_fun(x: int) -> None:
    start = datetime.datetime.now()
    print(fibonacci_recursive(x))
    print(f'recursive: {datetime.datetime.now()-start}')
    start = datetime.datetime.now()
    print(fibonacci_with_loop(x))
    print(f'with loop: {datetime.datetime.now()-start}')


