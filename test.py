
class User:
    instances = []
    def __init__(self, name: str) -> None:
        self.name = name
        self.__class__.instances.append(self)
    
    def __repr__(self) -> str:
        return f'{self.name}'


class City:
    instances = []
    def __init__(self, name: str) -> None:
        self.name = name
        self.__class__.instances.append(self)
    
    def __repr__(self) -> str:
        return f'{self.name}'


class Group:
    instances = []
    def __init__(self,users: list[User], name:str, city: City) -> None:
        self.users = users
        self.name = name
        self.city = city
        self.cases = []
        self.__class__.instances.append(self)
        
      
    def __repr__(self) -> str:
        return f'group {self.name} num_cases = {len(self.cases)}'



class Case:
    instances = []
    def __init__(self, loan: float, city: City) -> None:
        self.loan = loan
        self.group: Group = None
        self.city = city
        self.__class__.instances.append(self)

    def __repr__(self) -> str:
        try:
            return f'{self.loan} - {self.city} ---- group {self.group.name} '
        except:
            return f'{self.loan} - {self.city} ---- group {None}'
    @classmethod
    def grouping(cls):
        groups = Group.instances
        group_cities = {group.city for group in groups}
        cases_grouped = dict()
        groups_grouped = dict()
        cases_with_bad_cities = list(filter(lambda case: case.city not in group_cities, cls.instances))

        for city in group_cities:
            cases_grouped[city] = list(filter(lambda case: case.city == city, cls.instances))
            groups_grouped[city] = list(filter(lambda group: group.city == city, groups))
            
        
        for city in group_cities:
            cases = cases_grouped.get(city)
            if city.name == 'Tbilisi':
                cases = [*cases, *cases_with_bad_cities]
            groups = groups_grouped.get(city)
            len_groups = len(groups)
            len_cases = len(cases) 
            
            for_each_group = len_cases // len_groups
            rest = len_cases % len_groups

            x = 0
            
            for group in groups:
                # group.cases = cases[x:x+for_each_group]
                for case in cases[x:x+for_each_group]:
                    case.group = group
                    group.cases.append(case)
                x+=for_each_group

            for i in range(1,rest+1):
                groups[-i].cases.append(cases[-i])
                cases[-i].group = groups[-i]

    
            


nika = User('nika')
mari = User('mari')
admin = User('admin')
test = User('test')
lasha = User('lasha')
nino = User('nino')
ana = User('ana')
gio = User('gio')

Tbilisi = City('Tbilisi')
Rustavi = City('Rustavi')
Gori = City('Gori')

group_1 = Group([nika,mari,admin],'ჯგუფი 1', Tbilisi)
group_2 = Group([test, lasha, nino], 'ჯგუფი 2', Rustavi)
group_3 = Group([gio,ana],  'ჯგუფი 3', Tbilisi)
group_4 = Group([test, lasha, nino], 'ჯგუფი 4', Rustavi)

case_13 = Case(14337, Tbilisi)
case_14 = Case(19038, Tbilisi)
case_15 = Case(14990, Gori)
case_16 = Case(15283, Gori)
case_17 = Case(11535, Rustavi)
case_18 = Case(13176, Rustavi)
case_19 = Case(17628, Gori)
case_20 = Case(18208, Gori)
case_21 = Case(10551, Gori)
case_22 = Case(17690, Rustavi)
import time


class test:
    def __init__(self,name):
        self.name = name
    
    def pr(self):
        print(self.name)
    
a = test('nika')


class tes:
    def __init__(self,te) -> None:
        self.name = te

    def prw(self):
        test.pr(self)

s = tes('lalal')
s.prw()