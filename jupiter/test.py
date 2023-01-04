import pyodbc

class Server:
    def __init__(self):
        self.server = '10.10.5.101'
        self.db_user = 'gek'
        self.db_password = 'giogiogio123'
        self.db_name = 'Abacus_fern'


def get_server():
    return Server()

def get_abacus_data():
    ser = get_server()
    conne = pyodbc.connect(Driver="{ODBC Driver 17 for SQL Server}",
                           Server="{0},1433".format(ser.server),
                           Database=ser.db_name,
                           UID=ser.db_user,
                           PWD=ser.db_password,
                           Trusted_Connection="no")
    with conne.cursor() as cursor:
        cursor.execute("SELECT * FROM information_schema.tables")
        print(cursor)
        datas = cursor.fetchall()
    return datas

for i in get_abacus_data():
    print(i)
