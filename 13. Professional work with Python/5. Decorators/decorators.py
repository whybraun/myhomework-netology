import datetime
from functools import wraps

def logger(path):
    def decorator_param(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            with open(path, 'a') as f:
                start = datetime.datetime.now()
                result = old_function(*args, **kwargs)
                f.write(
                    f"Начало работы {start} \n"
                    f"Имя функции {old_function.__name__} \n"
                    f"Аргументы {args} и {kwargs} \n"
                    f"Значение {result} \n"
                )
                return result
        
        return new_function
    
    return decorator_param
