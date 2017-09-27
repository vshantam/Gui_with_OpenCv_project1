

from tkinter import *

failures=[]
failure_max=3
passwords=[('root','toor')]

def check_cred():

	print(username.get(), password.get())
	if (username.get(), password.get()) in passwords:
		master.destroy()
	        print('Logged in')
	        from applic import *

	else:	
		failures.append(1)
		if sum(failures) >= failure_max:
			master.destroy()
		else:
        		master.title('Try again. Attempt %i/%i' % (sum(failures)+1, failure_max))
 

def login:
	check_cred()


global quit
def quit:
	master.destroy()


master = Tk()
master.geometry('720x480')
Label(master, text="username").grid(row=0)
Label(master, text="password").grid(row=1)

username= Entry(master)
password = Entry(master)

username.grid(row=0, column=1)
password.grid(row=1, column=1)

Button(master, text='Quit', command=quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='login', command=login).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
