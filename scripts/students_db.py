import sqlite3


conn = sqlite3.connect('students.db')

cursor = conn.cursor()

cursor.execute("""create table if not exists students(
              saxeli text,
              gvari text,
              nishani_programirebashi int,
              nishani_matematikashi int,
              nishani_inglisurshi int, 
              sashualo_qula int
              )
               """)

conn.commit()
cursor.close()
conn.close()


class Student:

  def __init__(self,saxeli, gvari, qula_prog, qula_math, qula_ing ):
      
      try:  
        self.saxeli = saxeli
        self.gvari = gvari
        self.qula_prog = int(qula_prog)
        self.qula_math =int( qula_math)
        self.qula_ing = int(qula_ing)

      except:
        print('ერთერთი მნიშვნელობა არასწორადაა შეყვანილი.')
        return 

      Student.insert(self.saxeli, self.gvari, self.qula_prog,self.qula_math, self.qula_ing)

  def insert(saxeli, gvari, qula_prog, qula_math, qula_ing):
    with sqlite3.connect('students.db') as conn:
      cursor = conn.cursor()
      sashualo_qula =  round((qula_prog+qula_math+qula_ing)/3, 2)
      cursor.execute("""insert into students 
                    values(?,?,?,?,?,?)""",(saxeli, gvari, qula_prog, qula_math, qula_ing, sashualo_qula))

  def show_students():
    with sqlite3.connect('students.db') as conn:
      cursor = conn.cursor()

      cursor.execute("""select * from students""")
      students = cursor.fetchall()
      for index, student in enumerate(students,1):
        print(f'{index}.' , end='')  
        for column in student:
          print(f'{column},  ', end='')
        print('\n')



def menu():
  while True:
    choice = input('(აირჩიეთ ნორმით)\n1.ახალი სტუდენტის ჩამატება \n2.ყველა სტუდენტის ნახვა \n3.პროგრამის გათიშვა \n>>>')

    if choice =='1' :
      stud_num = input('რამდენი სტუდენტის დამატება გსურთ: ')
      if stud_num.isdigit():
        stud_num = int(stud_num)
      else: 
        print('რიცხვი უნდა შეიყვანოთ.')
        continue  
      for i in range(stud_num):
        saxeli = input('სახელი: ')
        gvari = input('გვარი: ')
        qula_prog = input('ქულა პროგრამირებაში: ')
        qula_math = input('ქულა მათემატიკაში: ')
        qula_ing = input('ქულა ინგლისურში: ')
        new_student = Student(saxeli, gvari, qula_prog, qula_math, qula_ing)
    elif choice == '2':
      Student.show_students()
    elif choice == '3':
      break  
    else: print('ბრძანება არასწორადაა შეყვანილი.')  
  input()  

menu()
