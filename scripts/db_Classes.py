from datetime import datetime
import sqlite3



class Database:

	entries = []

	def add_to_db(self, todo):
		self.entries.append(todo)
		print("\nჩანაწერი წარმატებით დამატებულია!")


	def edit_todo_db(self, index, newtodo):
		self.entries[index] = newtodo
		print("\nჩანაწერო წარმატებით შეცვლილია!")


	def delete_todo_db(self, index):
		self.entries.pop(index)
		print("\nჩანაწერი წარმატებით ამოშლილია!")


	def get_all_todos(self):
		return self.entries


class Manager:

	def __init__(self, db):
		self.database = db


	def add_todo(self, todo):
		self.database.add_to_db(todo)


	def edit_todo(self, index, newtodo):
		self.database.edit_todo_db(index, newtodo)


	def delete_todo(self, index):
		self.database.delete_todo_db(index)


	def show_all(self):
		data = self.database.get_all_todos()

		for index, item in enumerate(data, 1):
			print(20 * "-" + str(index) + 20 * "-")
			print(item)
			print(41 * "-")


	def count_todos(self):
		return len(self.database.get_all_todos())


class Todo:

	def __init__(self, text):
		self.text = text
		self.date = datetime.now()


	def __str__(self):
		return "Date: " + self.date.strftime("%d/%m/%Y %H:%M") + "\nTodo: " + self.text


def menu():

	choice = None

	db = Database()
	manager = Manager(db)


	while choice != "exit":

		print("\nმენიუ:")
		print("1. ჩანაწერის ჩამატება")
		print("2. ჩანაწერის რედაქტირება")
		print("3. ჩანაწერის წაშლა")
		print("4. ჩანაწერების ჩვენება")
		print("პროგრამიდან გამოსვლა 'exit'")

		choice = input("\nაირჩიეთ სასურველი მოქმედება: ")


		if choice == "1":

			text = input("შეიტანეთ მიზანი: ")
			todo = Todo(text)

			manager.add_todo(todo)



		elif choice == "2":


			if manager.count_todos():

				while True:

					manager.show_all()

					index = input("აირჩიეთ ჩანაწერი: ")

					if not index.isdigit():
						print("\nგთხოვთ შეიტანოთ რიცხვი!")
						continue

					if int(index) > manager.count_todos() or int(index) <= 0:
						print("გთხოვთ კორექტულად აირჩიოთ ჩანაწერის N!")
						continue

					index = int(index)

					text = input("შეიტანეთ ახალი მიზანი: ")
					newtodo = Todo(text)

					manager.edit_todo(index - 1, newtodo)
					break

			else:
				print("ბაზაში ჩანაწერები არ მოიძებნება!")



		elif choice == "3":

			if manager.count_todos():

				while True:

					manager.show_all()

					index = input("აირჩიეთ ჩანაწერის N: ")

					if not index.isdigit():
						print("\nშეიტანეთ რიცხვი!")
						continue

					if int(index) > manager.count_todos() or int(index) <= 0:
						print("\nგთხოვთ კორექტულად აირჩიოთ N!")
						continue

					index = int(index)

					manager.delete_todo(index - 1)
					break



			else:
				print("ბაზაში ჩანაწერები არ მოიძებნება")




		elif choice == "4":

			manager.show_all()



		else:
			print("გთხოვთ აირჩიოთ კორექტული მოქმედება!")


menu()

