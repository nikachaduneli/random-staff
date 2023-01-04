import sqlite3


def create_table(cursor):

    ##SQL კოდი მიეწოდება execute() მეთოდს
    ##ცხრილის შექმნა
    cursor.execute(''' CREATE TABLE if not exists persons(
                    uid INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    gender INTEGER,
                    age INTEGER DEFAULT 18)''')


#ობიექტის შექმნა
def add_persons(name,gender, age):

    ##SQL კოდი მიეწოდება execute() მეთოდს
    #მონაცემების შეყვანა
    cursor.execute("""INSERT INTO persons(name,gender,age)
                    VALUES(?,?,?)""",(name, gender, age))



# "test.db" ბაზის შექმნა და მასთან კავშირის დამყარება

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

#".db" გაფართოების გარდა შესაძლებელია ასევე გამვიყენოთ  ".db3", ".sqlite", ".sqlite3".

with sqlite3.connect('txtsss/test.db') as connection:

     # კურსორ ობიექტის შექმნა
    cursor = connection.cursor()

     ##ცხრილის შექმნა
    create_table(cursor)



    #მონაცემების შეყვანა
    add_persons('გოჩა','male',55)
    add_persons('ჟუჟუნა','female',25)
    add_persons('მალხაზი','male',40)
    add_persons('ნათელა','female',50)

    #მონაცემების წამოღება ჩველებრივი SQL-ივით
    cursor.execute(""" SELECT uid FROM persons  """)# მარტო ამით "<sqlite3.Cursor object at 0x0000029205B5DB90>" ასეთ რაღაცას მივიღებთ

    #ამიტო გასაგებ ენაზე რო ვნახოთ

    data = cursor.fetchone() # მარტო ერთს გახსნის
    data = cursor.fetchmany(10) # რამდენსაც ეტყვი იმდენს
    data = cursor.fetchall() # ყველას
    

    #ცხრილის ბაზიდან წაშლა 'DROP TABLE ...'
    cursor.execute("DROP TABLE persons")

    #რომელიმე რიგის ამოშლა ცხრილიდან
    cursor.execute("DELETE FROM persons WHERE age > 22")

    #რომლიმე რიგში ინფრორმაციის განახლება
    cursor.execute("UPDATE persons SET age = age + 1 WHERE gender = 1 ")


    #ცვლილებების დადასტურება,თუ with-ით ვაკეთებთ მაშინ საჭირო აღარაა
    connection.commit()

    # კავშირის გაწყვეტა ესეც აღარაა საჭირო with-ით
    cursor.close()
    connection.close()


