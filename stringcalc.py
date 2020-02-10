def add(string):
    if string == '':
        return '0'
    
    pos = string.find(',\n')
    if pos != -1:
        raise ValueError(f"Number expected but '\n' found at position {pos+1}.")
    string = string.replace('\n', ',')

    if string.endswith(','):
        raise ValueError("Number expected but EOF found.")

    numbers = string.split(',')
    numbers = map(int, numbers)
    return str(sum(numbers))