import tkinter as tk
from tkinter import filedialog


def main():
    root = tk.Tk()

    root.geometry('500x400')

    frame = tk.Frame(root, bg='#111')
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(root, text='enter numbers')
    label.pack()

    a = tk.Entry(root)

    a.pack()

    b = tk.Entry(root)
    b.pack()



    def calculate():
        try:
            a_num = int(a.get())
            b_num = int(b.get())
            jami = a_num + b_num
            sxvaoba = a_num - b_num
            namravli = a_num * b_num

            if b_num == 0:
                ganayofi = "can't divide by 0"
            else:
                ganayofi = a_num / b_num
        except:
            label = tk.Label(root, text='enter numbers!!!!',fg='#fff',bg='#111')
            label.pack()

        label = tk.Label(root, text='{} + {} = {} \n{} - {} = {} \n{} x {} = {} \n{} / {} = {}  '.format(a_num, b_num,jami,
                                                                                                         a_num, b_num,sxvaoba,a_num, b_num,
                                                                                                         namravli,a_num, b_num,ganayofi.__round__(3)),fg='#fff',bg='#111')
        label.pack()

    submit = tk.Button(root, text='submit',
                       padx=10, pady=2, fg='white', bg='black', command=calculate)
    submit.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
