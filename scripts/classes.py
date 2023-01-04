



class Person:
    '''
    this is Person class

    '''

    present_year = 2020
    num = 0

    '''__init metodi gamoicaxeba classis instansis yovel sheqmnaze'''
    def __init__(self, name, last_name, age):

        self.name = name
        self.last_name = last_name
        self.age = age

        Person.num+=1


    def full_name(self):
        return "{} {}".format(self.name,self.last_name)




    @classmethod
    def set_year(cls,present_year):
        cls.present_year = present_year

    @classmethod
    def from_string(cls, per_str):
        name, last_name, age = per_str.split("-")
        return cls(name, last_name, int(age))



    '''static metodi ar igebs argumentad arc class da arc instancss  chveulebrivi funciasavit mushaobs'''

    def product(x,y):

        return x*y



    '''special methods'''
    def __repr__(self):
        return "Person('{}','{}',{})".format(self.name, self.last_name, self.age)

    def __str__(self):
        return "{} {}".format(self.full_name(),self.age)

    def __add__(self, other):
        return self.age + other.age



    '''am metodidan mnishvnelobas amovigebt rogorc cvladidan
    anu print(xx.full_information()) is magivrad
    print(xx.full_information)
    '''
    @property
    def full_information(self):
        return "{} {} years old".format(self.full_name(),self.age)



    '''informaciis shesacvelad'''
    @full_information.setter
    def  full_information(self, string):

        name , last_name , age = string.split(" ")

        self.name = name
        self.last_name = last_name
        self.age = int(age)

    '''wasashlelad'''
    @full_information.deleter
    def full_information(self):

        self.name = None
        self.last_name = None
        self.age = None



#instancis Sheqmna
guguli = Person("guguli", "guguliani" , 67)
gugu = Person("gugu", "guguliani" , 67)
guli = Person("guli", "guguliani" , 67)
gela1 = Person("guli1", "guguliani" , 67)


#stingidan sheqmna
new_pers = "gela-gamgebeli-40"
gela = Person.from_string(new_pers)
print("Person.instance.full_name():",gela.full_name())



##setter
print(gela1.full_information)
gela1.full_information = 'lamara lamariani 91'
print(gela1.full_information)

del gela1.full_information
print(gela1.full_information)




#sheqmnili instancebis raodenoba
print("Person.num:",Person.num)


#class-shi Variable shecvla
print("Person.present_year:",Person.present_year)
Person.set_year(2021)
print("Person.Changed-present_year:",Person.present_year)

#static method
print('static:',Person.product(9,8))

#####!!!####
# print(help(Person))


#from special methods __add__
print(gela)
print(gela + guli)
print(repr(gela))







'''shvilobili classi '''
class Child_Person(Person):

    '''mshoblis metodis gadaketeba'''
    def __init__(self,name, last_name, age , addres):

        #an ase
        super().__init__(name, last_name, age) # anu mshoblis __init__().methods gadaewodeba name,last_name,
        # da age da addres-s mere chven vamushavebt



        #an ase
        Person.__init__(self,name, last_name, age)

        self.addres = addres
    def __str__(self):

        return f'{self.name} {self.last_name} {self.age} {self.addres}'

    def __repr__(self):

        return "Person('{}','{}',{}, {})".format(self.name, self.last_name, self.age,self.addres)






gela = Child_Person("gela","geliani",21,"borjomi")

####damatebuli misamarti
print("Child_class: gela.full_name():",gela.full_name())
print("Child_class: gela.addres:",gela.addres)

