from flask import Flask
from flask_restful import Api, Resource
import sqlite3


# app = Flask(__name__)
# api = Api(app)

connection = sqlite3.connect('students.db')
cursor = connection.cursor()
cursor.execute(''' CREATE TABLE if not exists STUDENTS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    lastname TEXT NOT NULL,
                    gender INTEGER,
                    age INTEGER NOT NULL)''')
cursor.execute(''' CREATE TABLE if not exists GRADES(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    subject TEXT NOT NULL,
                    grade TEXT NOT NULL,
                    student INTEGER)''')

connection.commit()



class Student:
    def __init__(self, name, lastname, gender, age) -> None:
        self.name = name
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def get_attrs(self):
        return ['name', 'lastname', 'gender', 'age']

    def __str__(self) -> str:
        return f"Student: {self.name} {self.lastname}"
    
    def save(self) -> None:
        cursor.execute('''
                        INSERT INTO STUDENTS(name, lastname, gender, age)
                        VALUES (?,?,?,?)''', (self.name, self.lastname, self.gender, self.age))
        connection.commit()
    
    @staticmethod
    def get(student_id) -> 'Student':
        cursor.execute('''SELECT * FROM STUDENTS WHERE id = ?''', (student_id,))    
        student = cursor.fetchone()
        return Student(student[1], student[2], student[3], student[4])               
        
    def update(self, **kwargs) -> None:

        for i in kwargs:
            if i in self.get_attrs():
                cursor.execute(f'''
                         UPDATE STUDENTS set {i} = ?
                         WHERE student_id = ?''', (kwargs[i],))

        # cursor.execute('''
        #                 UPDATE STUDENTS set(name, lastname, gender, age)
        #                 VALUES (?,?,?,?)''', (self.name, self.lastname, self.gender, self.age))
        # connection.commit()
        print(kwargs)
        print(self.__getattribute__())



# st = Student(name='lamazo', lastname='chaduneli', gender='male', age=210)
# st.save()
new_st = Student.get(student_id=18)
print(new_st)
new_st.update(name='lasha', age='asd')

new_st = Student.get(student_id=18)
print(new_st)

# class Test(Resource):
    
#     def get(self):
#         return {'hello':'hello world'}

# api.add_resource(Test, '/test')
# if __name__ == '__main__':
#     app.run(debug=True)