import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS students(
                    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fName VARCHAR ,
                    lName VARCHAR )""")


cursor.execute("""CREATE TABLE IF NOT EXISTS marks(
                    sid INTEGER,
                    subject VARCHAR,
                    mark INTEGER)""")

class Student:
    def __init__(self,fName , lName):
        self.fName = fName
        self.lName = lName

        cursor.execute("""INSERT INTO students(fName,lName)
                    VALUES(?,?)""",(self.fName,self.lName))
        cursor.execute('''SELECT MAX(student_id)
                        FROM    students''')
        self.student_id = cursor.fetchone()[0]
        connection.commit()
        

    def self_update_student(self):
        new_name = input('შეიყვანეთ ახალი სახელი: ')
        new_last = input('შეიყვანეთ ახალი გვარი: ')
        cursor.execute("""UPDATE students SET fName = ? , lName = ? WHERE student_id = ?""", (new_name, new_last, self.student_id))
        connection.commit()


    def self_del_stud(self):

        cursor.execute("""DELETE FROM students WHERE student_id = ?""", (self.student_id,))
        cursor.execute("""DELETE FROM marks WHERE sid = ?""", (self.student_id,))

        a = input('სტუდენტის წაშლასთან ერთად წაიშლება მისი ქულებიც.')
        connection.commit()

    def self_add_mark(self):

        subject = input('შეიყვანეთ საგნის დასახელება: ')
        mark = input('შეიყვანეთ ნიშანი: ')

        cursor.execute("""INSERT INTO marks(sid,fName,lName)
                        VALUES(?,?,?)""",(self.student_id,subject,mark))
        connection.commit()



    @staticmethod
    def update_student():

        cursor.execute('''SELECT * FROM students''')
        students = cursor.fetchall()

        for student in students:
            print(student)

        id_to_up = input('აირჩიეთ id ნომრით სტუდენტი რომლის შეცვლაც გსურთ: ')
        new_name = input('შეიყვანეთ ახალი სახელი: ')
        new_last = input('შეიყვანეთ ახალი გვარი: ')
        cursor.execute("""UPDATE students SET fName = ? , lName = ? WHERE student_id = ?""", (new_name, new_last, id_to_up))
        connection.commit()


    @staticmethod
    def delete_student():

        cursor.execute('''SELECT * FROM students''')
        students = cursor.fetchall()

        for student in students:
            print(student)


        id_to_del = input('აირჩიეთ id ნომრით სტუდენტი რომლის წაშლაც გსურთ: ')
        cursor.execute("""DELETE FROM students WHERE student_id = ?""", (id_to_del))
        cursor.execute("""DELETE FROM marks WHERE sid = ?""", (id_to_del))
        a = input('სტუდენტის წაშლასთან ერთად წაიშლება მისი ქულებიც.')
        connection.commit()
    @staticmethod
    def add_mark():

        cursor.execute('''SELECT * FROM students''')
        students = cursor.fetchall()

        for student in students:
            print(student)

        student = input('აირჩიეთ id ნომრით რომელი სტუდენტისთვის შეგყავთ ქულა: ')
        subject = input('შეიყვანეთ საგნის დასახელება: ')
        mark = input('შეიყვანეთ ნიშანი: ')

        cursor.execute("""INSERT INTO marks(sid,subject,mark)
                        VALUES(?,?,?)""",(student,subject,mark))
        connection.commit()




def menu():
    command =''
    student = None
    while command != '-1':
        print('='*30)

        command = input('''1.ახალი სტუდენტის დამატება
2.რედაქტირება
3.წაშლა
4.ნიშნის შეტანა
5.გამოსვლა
>>>''')
        if student != None:

            if command == '1':
                name = input('სახელი: ')
                last = input('გვარი: ')
                student = Student(name, last)
            elif command =='2':
                choice = input(f'1.{student.fName}, {student.lName}-(ი)ს რედაქტირება\n2.სხვა სტუდენტის ტედაქტირება\n>>>')
                if choice == '1':
                    student.self_update_student()
                elif choice == '2':
                    Student.update_student()
                else:continue
            elif command == '3':
                choice = input(f'1.{student.fName}, {student.lName}-(ი)ს წაშლა\n2.სხვა სტუდენტის წაშლა\n>>>')
                if choice == '1':
                    student.self_del_stud()
                elif choice == '2':
                    Student.delete_student()
            elif command == '4':
                choice = input(f'1.ნიშნის შეტანა {student.fName}, {student.lName}-(ი)სთვის \n2.ნიშის შეტანა სხვა სტუდენტისთვის \n>>>')

                if choice =="1":
                    student.self_add_mark()
                elif choice == '2':
                    Student.add_mark()
            elif command =='5':
                break
        else:

            if command == '1':
                name = input('სახელი: ')
                last = input('გვარი: ')
                student = Student(name, last)
            elif command =='2':
                Student.update_student()
            elif command == '3':
                Student.delete_student()
            elif command == '4':
                Student.add_mark()
            elif command =='5':
                break





menu()


