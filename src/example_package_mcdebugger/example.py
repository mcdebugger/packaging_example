def add_one(number):
    return number + 1

def add_two(number):
    return number + 2

def main():
    digit = 1
    
    print(f'Executing add_one calculation on digit: {digit}')
    digit = add_one(digit)
    print(f'Result: {digit}')
    
    print(f'Executing add_two calculation on digit: {digit}')
    digit = add_two(digit)
    print(f'Result: {digit}')
    
    print('Congratulations! You\'re computing magician!')
