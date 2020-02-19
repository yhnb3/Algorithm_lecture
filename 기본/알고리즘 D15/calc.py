def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return '0으로는 나눌 수 없습니다.'
    else:
        return result


def gob(a, b):
    return a * b

