

class Weight_class:

    def __init__(self, weight_type, weight):

        self.weight_type = weight_type
        self.weight = weight


    def convert_to_kg(self):

        if self.weight_type == 'გრამი':
            return f'{self.weight} {self.weight_type} {self.weight/1000} კილოგრამია'

        elif self.weight_type == 'ფუნტი':
            return f'{self.weight} {self.weight_type} {self.weight * 0.453592} კილოგრამია'

        elif self.weight_type == 'ტონა':
            return f'{self.weight} {self.weight_type} {self.weight * 1000} კილოგრამია'

        elif self.weight_type =='კილოგრამი':
            return f'{self.weight} {self.weight_type} {self.weight} კილოგრამია'

        else: return 'გთხოვთ კორექტულად შეიყვანოთ წონის ერთეული!'


    def convert_to_gg(self):

        if self.weight_type == 'გრამი':
            return f'{self.weight} {self.weight_type} {self.weight} გრამია'

        elif self.weight_type == 'ფუნტი':
            return f'{self.weight} {self.weight_type} {self.weight * 453.592} გრამია'

        elif self.weight_type == 'ტონა':
            return f'{self.weight} {self.weight_type} {self.weight * 1_000_000} გრამია'

        elif self.weight_type =='კილოგრამი':
            return f'{self.weight} {self.weight_type} {self.weight * 1000} გრამია'

        else: return 'გთხოვთ კორექტულად შეიყვანოთ წონის ერთეული!'


    def convert_to_pound(self):

        if self.weight_type == 'გრამი':
            return f'{self.weight} {self.weight_type} {self.weight * 0.00220462} ფუნტია'

        elif self.weight_type == 'ფუნტი':
            return f'{self.weight} {self.weight_type} {self.weight} ფუნტია'

        elif self.weight_type == 'ტონა':
            return f'{self.weight} {self.weight_type} {self.weight * 2204.62} ფუნტია'

        elif self.weight_type =='კილოგრამი':
            return f'{self.weight} {self.weight_type} {self.weight * 2.20462} ფუნტია'

        else: return 'გთხოვთ კორექტულად შეიყვანოთ წონის ერთეული!'


    def convert_to_tonne(self):

        if self.weight_type == 'გრამი':
            return f'{self.weight} {self.weight_type} {self.weight }/1000000 ტონაა'

        elif self.weight_type == 'ფუნტი':
            return f'{self.weight} {self.weight_type} {self.weight * 0.000453592} ტონაა'

        elif self.weight_type == 'ტონა':
            return f'{self.weight} {self.weight_type} {self.weight} ტონაა'

        elif self.weight_type =='კილოგრამი':
            return f'{self.weight} {self.weight_type} {self.weight / 1000} ტონაა'

        else: return 'გთხოვთ კორექტულად შეიყვანოთ წონის ერთეული!'






def menu():

    exit = ''
    weight_types = ['გრამი', 'კილოგრამი','ტონა', 'ფუნტი']

    while  exit != 'exit':

        print('\n'+'='*40)

        weight_type = input('შეიყვანეთ წონის ერთეული ->(გრამი, კილოგრამი,ტონა, ფუნტი): ')

        if weight_type not in weight_types:

            print('გთხოვთ კორექტულად შეიყვანოთ წონის ერთეული!')

            print('='*40)
            exit = input("თუ გსურთ შეწყვეტა აკრიფეთ 'exit': ")
            continue

        weight = input('შეიყვანეთ რიცხვითი მნიშვნელობა: ')

        if weight.isdigit():

            weight = int(weight)

        else:
            print('გთხოვთ შეიყვანოთ რიცხვი!')

            print('='*40)
            exit = input("თუ გსურთ შეწყვეტა აკრიფეთ 'exit': ")

            continue

        #ობიექტის შექმნა
        weight_obj = Weight_class(weight_type,weight)

        type_to_convert = input('შეიყვანეთ ერთეული რომელშიც გსურთ გaდაანგარიშება\n->(გრამი, კილოგრამი,ტონა, ფუნტი): ')


        if type_to_convert == 'გრამი':
            print(weight_obj.convert_to_gg())

        elif type_to_convert == 'ტონა':
            print(weight_obj.convert_to_tonne())

        elif type_to_convert == 'ფუნტი':
            print(weight_obj.convert_to_pound())

        elif type_to_convert == 'კილოგრამი':
            print(weight_obj.convert_to_kg())

        else: print('გთხოვთ კორექტულად შეიყვანოთ წონის ერთეული!')


        print('='*40)
        exit = input("თუ გსურთ შეწყვეტა აკრიფეთ 'exit': ")



menu()
