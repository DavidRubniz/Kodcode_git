#1
def safe_int(s):
    try:
        return int(s)
    except Exception:
        return None
    
#2
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "undefined"
    
#3
def read_first_line(path):
    try:
        with open(path, 'r') as file:
            return file.readline()
    except FileNotFoundError:
        return None
    
#4
def get_value(d, key):
    try:
        return d[key]
    except KeyError:
        return "missing"
    
#5
def parse_ints(values):
    result = []
    for v in values:
        try:
            result.append(int(v))
        except ValueError:
            pass
    return result

#6
def set_age(age):
    if age < 0 or age > 150:
        raise ValueError("Age is invalid")
    return age

#7
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Amount exceeds balance")
    return balance - amount


#8
def retry(func, n):
    last_exception = None
    for _ in range(n):
        try:
            return func() 
        except Exception as e:
            last_exception = e 
            
    if last_exception is not None:
        raise last_exception
    
#9
def count_errors(funcs):
    error_count = 0
    for func in funcs:
        try:
            func()
        except Exception:
            error_count += 1
    return error_count

#10
def load_config(path):
    try:
        with open(path, 'r') as file:
            return int(file.readline())
    except Exception as e:
        raise RuntimeError("failed to load config") from e
    
    