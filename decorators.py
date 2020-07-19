def flashing(func):
    def wrapper(t_write: float=0.0, t_clear: float=0.0, *args, **kwargs):
        for r in range(10):
            t_write -= 0.02
            t_clear -= 0.02
            func(t_write, t_clear)
        return func(t_write, t_clear, *args, **kwargs)
    return wrapper

def decrement_delay(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) - 0.001
    return wrapper

def map_min_max(func):
    def wrapper(value, leftMin=0.1, leftMax=0.01, rightMin=1, rightMax=10):
        leftRange = leftMax - leftMin
        rightRange = rightMax - rightMin
        valuesScaled = float(value - leftMin) / float(leftRange)
        return '%g'%(rightMin + (valuesScaled * rightRange))
    return wrapper

def increment_score(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 10
    return wrapper

if __name__ == '__main__':
    pass