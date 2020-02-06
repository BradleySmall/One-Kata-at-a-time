def fizzbuzz(num):
    result = ""
    substituions = {
        3: 'Fizz',
        5: 'Buzz',
        7: 'Flugal'
    }
    for (factor, name) in substituions.items():
        if num % factor == 0:
            result += name
    if result:
        return result  
    return num