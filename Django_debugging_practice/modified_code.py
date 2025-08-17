import time
from functools import wraps

def time_calculate(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} excuted in {end-start:.6f}seconds")
        return result
    return wrapper


@time_calculate
def get_even_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

nums = [1,2,3,4,5,6,7,8,9,10]

print(get_even_numbers(nums))