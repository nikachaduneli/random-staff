
class Vector:

    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        if isinstance(other,Vector):

            return 'result -> {}'.format(Vector(self.x * other.x,
                            self.y * other.y,
                            self.z * other.z))
        elif isinstance(other,(int,float)):
            return 'result -> {}'.format(Vector(self.x * other,
                            self.y * other,
                            self.z * other))
        else:return "can't multiply these arguments"

    def __add__(self, other):
        if isinstance(other,Vector):

            return 'result -> {}'.format(Vector(self.x + other.x,
                            self.y + other.y,
                            self.z + other.z))
        elif isinstance(other,(int,float)):
            return 'result -> {}'.format(Vector(self.x + other,
                            self.y + other,
                            self.z + other))

        else:return "can't add these arguments"

    def __sub__(self, other):
        if isinstance(other,Vector):

            return 'result -> {}'.format(Vector(self.x - other.x,
                            self.y - other.y,
                            self.z - other.z))
        elif isinstance(other,(int,float)):
            return 'result -> {}'.format(Vector(self.x - other,
                            self.y - other,
                            self.z - other))

        else:return "can't subtract these arguments"

    def __truediv__(self, other):
        if isinstance(other,Vector):

            return 'result -> {}'.format(Vector(self.x / other.x,
                            self.y / other.y,
                            self.z / other.z))
        elif isinstance(other,(int,float)):
            return 'result -> {}'.format(Vector(self.x / other,
                            self.y / other,
                            self.z / other))
        else:return "can't divide with these arguments"

    def __str__(self):
        return f'Vector: ({self.x}, {self.y}, {self.z})'

    def create_vector(parameters):

        x, y, z = parameters

        return Vector(float(x), float(y), float(z))

class Number_vector(float):

    def __init__(self, number):
        self.number = float(number)

    def __truediv__(self, other):

        if isinstance(other,Number_vector):
            return 'result -> {}'.format(self.number/other.number)


        elif isinstance(other,Vector):
            return 'result -> {}'.format(Vector(self.number / other.x,
                            self.number / other.y,
                            self.number / other.z))
        else:return "can't divide these arguments"

    def __sub__(self, other):

        if isinstance(other,Number_vector):
            return 'result -> {}'.format(self.number-other.number)

        elif isinstance(other,Vector):
            return 'result -> {}'.format(Vector(self.number - other.x,
                            self.number - other.y,
                            self.number - other.z))
        else:return "can't subtract these arguments"

    def __add__(self,other):

        if isinstance(other,Number_vector):
            return 'result -> {}'.format(self.number+other.number)

        elif isinstance(other,Vector):
            return 'result -> {}'.format(Vector(self.number + other.x,
                            self.number + other.y,
                            self.number + other.z))
        else:return "can't add these arguments"

    def __mul__(self,other):

        if isinstance(other,Number_vector):
            return 'result -> {}'.format(self.number*other.number)

        elif isinstance(other,Vector):
            return 'result -> {}'.format(Vector(self.number * other.x,
                            self.number * other.y,
                            self.number * other.z))
        else:return "can't multiply these arguments"


def operation():

#####
    first_argument = input('argument N1: ').split()

    if len(first_argument) == 3:
        try:
            first_argument = Vector.create_vector(first_argument)
        except: return 'parameters for first argument is wrong'
    elif len(first_argument) == 1:
        try:
            first_argument = Number_vector(first_argument[0])
        except: return 'parameters for first argument is wrong'
    else: return 'parameters for first argument is wrong'
#####
    second_argument = input('argument N2: ').split()

    if len(second_argument) == 3:
        try:
            second_argument = Vector.create_vector(second_argument)
        except: return 'parameters for second argument is wrong'
    elif len(second_argument) == 1:
        try:
            second_argument = Number_vector(second_argument[0])
        except: return 'parameters for second argument is wrong'
    else: return 'parameters for second argument is wrong'
#####
    operation_sign = input("enter operation sign  '-', '+', '/' or '*':  ").split()

    if len(operation_sign) == 1:
        if operation_sign[0] == '*':
            return  first_argument * second_argument
        elif operation_sign[0] == '/':
            return  first_argument / second_argument
        elif operation_sign[0] == '-':
            return  first_argument - second_argument
        elif operation_sign[0] == '+':
            return  first_argument + second_argument
        else: return 'operation sign is wrong'
    else: return 'operation sign is wrong'


print(operation())


