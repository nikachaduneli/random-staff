import sqlite3

connection = sqlite3.connect("teams.db")
cursor = connection.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS teams(
                    team_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR ,
                    color VARCHAR )""")


cursor.execute("""CREATE TABLE IF NOT EXISTS info(
                    tid INTEGER,
                    country VARCHAR,
                    date INTEGER)""")


class Team:

    def __init__(self, name, color):
        self.name = name
        self.color = color

        cursor.execute("""INSERT INTO teams(name,color)
                    VALUES(?,?)""",(self.name,self.color))
        cursor.execute('''SELECT MAX(team_id)
                        FROM teams''')
        self.team_id = cursor.fetchone()[0]
        connection.commit()


    @staticmethod
    def show_teams():
        cursor.execute("""SELECT * from teams""")
        teams = cursor.fetchall()
        for i in teams:
            print(i)

    @staticmethod
    def show_info():
        cursor.execute("""SELECT * from info""")
        info = cursor.fetchall()
        for i in info:
            print(i)

    def self_update_team(self):
        new_name = input('შეიყვანეთ ახალი სახელი: ')
        new_color = input('შეიყვანეთ ახალი ფერი: ')
        cursor.execute("""UPDATE teams SET name = ? , color = ? WHERE team_id = ?""", (new_name, new_color, self.team_id))

        self.name = new_name
        self.color = new_color
        connection.commit()


    @staticmethod
    def update_team():
        Team.show_teams()

        id_to_up = input('აირჩიეთ id ნომრით გუნდი რომლის შეცვლაც გსურთ: ')
        new_name = input('შეიყვანეთ ახალი სახელი: ')
        new_color = input('შეიყვანეთ ახალი ფერი: ')
        cursor.execute("""UPDATE teams SET name = ? , color = ? WHERE team_id = ?""", (new_name, new_color, id_to_up))
        connection.commit()

    def self_del_team(self):

        cursor.execute("""DELETE FROM teams WHERE team_id = ?""", (self.team_id,))
        cursor.execute("""DELETE FROM info WHERE tid = ?""", (self.team_id,))

        a = input('გუნდის წაშლასთან ერთად წაიშლება მასზე ინფორმაციაც')

        connection.commit()

    @staticmethod
    def del_team():

        Team.show_teams()

        id_to_del = input('აირჩიეთ id ნომრით გუნდი  რომლის წაშლაც გსურთ: ')
        cursor.execute("""DELETE FROM teams WHERE team_id = ?""", (id_to_del,))
        cursor.execute("""DELETE FROM info WHERE tid = ?""", (id_to_del,))
        a = input('გუნდის წაშლასთან ერთად წაიშლება მასზე ინფორმაციაც')
        connection.commit()


    def self_add_info(self):

        country = input('შეიყვანეთ ქვეყნის დასახელება: ')
        date = input('შეიყვანეთ დაარსების თარიღი: ')

        cursor.execute('''INSERT into info(tid,country, date) values (?,?,?) ''',(self.team_id,country, date))
        connection.commit()


    @staticmethod
    def add_info():
        Team.show_teams()

        id_to_add = input('აირჩიეთ id ნომრით რომელი გუნდისთვის გსურთ ინფორმაციის შეტანა:')
        country = input('შეიყვანეთ ქვეუნის დასახელება: ')
        date = input('შეიყვანეთ დაარსების თარიღი: ')

        cursor.execute('''insert into info(tid,country, date) values (?,?,?) ''',(id_to_add,country, date))
        connection.commit()


    def self_update_info(self):


            new_country = input('შეიყვანეთ ქვეყნის ახალი დასახელება: ')
            new_date = input('შეიყვანეთ დაარსების ახალი თარიღი: ')
            cursor.execute('''UPDATE info set country = ?, date = ? where tid = ?''',(new_country, new_date, self.team_id))
            connection.commit()

    @staticmethod
    def update_info():

        Team.show_info()
        id_to_update = input('აირჩიეთ id ნომრით რომელი ჩანაწერის შეცვლა გსურთ')
        new_country = input('შეიყვანეთ ქვეყნის ახალი დასახელება: ')
        new_date = input('შეიყვანეთ დაარსების ახალი თარიღი: ')
        cursor.execute('''UPDATE info set country = ?, date = ? where tid = ?''',(new_country, new_date, id_to_update))
        connection.commit()


    @staticmethod
    def show_teams_info():

        country = input('რომელი ქვეყნის გუნდების ნახვა გსურთ: ')

        cursor.execute("""SELECT  name, color, info.date FROM teams
                    JOIN info ON teams.team_id = info.tid where country = ?""",(country,))

        info = cursor.fetchall()
        for i in info:
            print(i)











def menu():
    command =''
    team = None
    while command != '-1':
        print('='*30)

        command = input('''1.ახალი გუნდის დამატება
2.გუნდის რედაქტირება
3.გუნდის წაშლა
4.გუნდზე ინფორმაციის შეტანა
5.ინფორმაციის განახლება
6.გუნდების ნახვა
7.გამოსვლა
>>>''')
        if team != None:

            if command == '1':
                name = input('სახელი: ')
                color = input('ფერი: ')
                team = Team(name, color)
            elif command =='2':
                choice = input(f'1.{team.name}-(ი)ს რედაქტირება\n2.სხვა გუნდის ტედაქტირება\n>>>')
                if choice == '1':
                    team.self_update_team()
                elif choice == '2':
                    Team.update_team()

            elif command == '3':
                choice = input(f'1.{team.name}-(ი)ს წაშლა\n2.სხვა გუნდის წაშლა\n>>>')
                if choice == '1':
                    team.self_del_team()
                elif choice == '2':
                    Team.del_team()
            elif command == '4':
                choice = input(f'1.ინფორმაციის შეტანა {team.name}-(ი)სთვის \n2.ინფორმაციის შეტანა სხვა გუნდისთვის \n>>>')

                if choice =="1":
                    team.self_add_info()
                elif choice == '2':
                    Team.add_info()
            elif command =='5':
                choice = input(f'1.ინფორმაციის განახლება {team.name}-(ი)სთვის \n2.ინფორმაციის განახვლება სხვა გუნდისთვის \n>>>')

                if choice == '1':
                    team.self_update_info()
                elif choice == '2':
                    Team.update_info()
            elif  command == '6':
                Team.show_teams_info()
            elif command =='7':break


        else:

            if command == '1':
                name = input('სახელი: ')
                color = input('ფერი: ')
                team = Team(name,color)
            elif command =='2':
                Team.update_team()
            elif command == '3':
                Team.del_team()
            elif command == '4':
                Team.add_info()
            elif command =='5':
                Team.update_info()
            elif command == '6':
                Team.show_teams_info()
            elif command =='7':break

menu()

