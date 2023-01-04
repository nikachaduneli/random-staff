from itertools import groupby

NUMBERS: tuple = (48,58)
CAPITALS: tuple = (65,91)
LOWERS: tuple = (97,123)  
PASSWORD_MIN_LENGTH: int = 6 

"""
    password must have one number, uppercase latter, lower case letter,
    must be longer or equal to 6 letters and shorter than or equal to 20,
    there shouldn't be more than 2 same letters next to each other. 
"""


def check_password_complexity(password: str) -> dict:

    PASSWORD_MIN_LENGTH = 6 
    has_lower: bool = False
    has_capital: bool = False
    has_number: bool = False

    for i in password:
        sys_ord = ord(i)
        if min(LOWERS) <= sys_ord <= max(LOWERS):
            has_lower = True
        elif min(CAPITALS) <= sys_ord <= max(CAPITALS):
            has_capital = True
        elif min(NUMBERS) <= sys_ord <= max(NUMBERS):
            has_number = True

    flaws: int = [has_number, has_capital, has_lower].count(False)
    is_strong: bool = all([has_number, has_capital, has_lower]) and len(password) >= PASSWORD_MIN_LENGTH

    return {'is_strong':is_strong, 'flaws': flaws}


#Checks if there are number of same letters next to each other in password and returns the amount of numbers that needs to be swaped
def same_letters(password: str, number: int) -> int:
    for letter, group in groupby(password):
        group = list(group)
        if len(group) >= number:
            return len(group) // number 
    return 0


#calculate minimum number of steps to make password safe
def minumum_steps_to_complex(password: str) -> int:
    if len(password) < PASSWORD_MIN_LENGTH:
        return PASSWORD_MIN_LENGTH - len(password)

    complexity: dict = check_password_complexity(password)
    is_strong: bool = complexity['is_strong']
    flaws: int = complexity['flaws']
    
    if is_strong:
        return same_letters(password=password, number=3)
    else:
        return flaws + same_letters(password=password, number=3)      
    
def main():
    password = input('Enter Password: ')

    steps = minumum_steps_to_complex(password)

    if steps == 0:
        print('your password is safe')
    else:
        print(f'minumum steps to make "{password}" complex enough is {steps}')


if __name__ == '__main__':
    main()
