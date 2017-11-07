from tkinter import *
from applic import *

failures = []
failure_max = 3
passwords = [('root', 'toor')]


class Login(object):
    @classmethod
    def check_cred(self):
        print(username.get(), password.get())
        if (username.get(), password.get()) in passwords:
            master.destroy()
            print('Logged in')
        else:
            failures.append(1)
            if sum(failures) >= failure_max:
                master.destroy()
            else:
                master.title('Try again. Attempt %i/%i' % (sum(failures) + 1, failure_max))

    @classmethod
    def login(self):
        self.check_cred()

    @classmethod
    def kills(self):
        master.destroy()


objs = Login()
master = Tk()
master.geometry('720x480')
Label(master, text="username").grid(row=0)
Label(master, text="password").grid(row=1)
username = Entry(master)
password = Entry(master)
username.grid(row=0, column=1)
password.grid(row=1, column=1)
Button(master, text='Quit', command=objs.kills).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='login', command=objs.login).grid(row=3, column=1, sticky=W, pady=4)
mainloop()
