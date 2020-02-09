def add(string):
    if string == '':
        return '0'
    numbers = string.split(',')
    numbers = map(int, numbers)
    return str(sum(numbers))