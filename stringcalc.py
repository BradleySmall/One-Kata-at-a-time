def add(string):
    if string == '':
        return '0'
    string = string.replace('\n', ',')
    numbers = string.split(',')
    numbers = map(int, numbers)
    return str(sum(numbers))