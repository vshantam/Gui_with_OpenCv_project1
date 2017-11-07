from lib import *

from login import *


class mains(object):
    @classmethod
    def Hello(self):
        self.quit()

    @classmethod
    def Tkwindow(self):
        global master, frame
        master = Tk()
        master.geometry('{}x{}'.format(1080, 480))
        greetings = "{}!, PLease select an option Below to Continue".format("")  # enter any user name
        msg = Label(master, text=greetings)
        msg.configure(background='lightgreen', font=('times', 24, 'italic'))
        msg.pack()
        frame = Frame(master)
        frame.pack()
        button = Button(frame, text="Agree and Continue.", fg="blue", command=self.Hello)
        button1 = Button(frame, text='Exit', fg='red', command=self.quit)
        button.pack(side=LEFT)
        button1.pack(side=RIGHT)
        mainloop()

    @classmethod
    def quit(self):
        master.destroy()


if __name__ == '__main__':
    ob = mains()
    ob.Tkwindow()
