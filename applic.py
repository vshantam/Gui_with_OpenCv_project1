


from lib import *


class img_pro:
	

	def Hello(self):

		global name 

		name=raw_input("PLease Enter Your Name To Proceed\n:>").strip()

		print("Hello, {}".format(name))

		print("Please wait for Few Second to Initialialize the sofware.....")

		time.sleep(5)


	def Tkwindow(self):

		global master

		master=Tk()

		master.geometry('{}x{}'.format(1080,480))

		greetings="{}!, PLease select an option Below to Continue".format(name)

		msg=Label(master,text=greetings)

		msg.configure(background='lightgreen', font=('times', 24, 'italic'))

		msg.pack()

		global frame

		frame = Frame(master)

    		frame.pack()

    		button = Button(frame, text="Agree and Continue.", fg="blue",command=App)

		button1=Button(frame,text='Exit',fg='red',command=Quit)

    		button.pack(side=LEFT)

		button1.pack(side=RIGHT)

		mainloop()


	global Quit

	def Quit():


		frame.destroy()

		master.destroy()

	

	global App

	def App():

		root=Tk()

		global panelA , panelB

		panelA=None

		panelB=None
		
		path=tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

		if len(path)>0:

			print("Image Selected")

			img=cv2.imread(path)

			gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

			edge=cv2.Canny(gray,50,15)

			img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

			img=Image.fromarray(img)

			edge=Image.fromarray(edge)

			img=ImageTk.PhotoImage(img)

			edge=ImageTk.PhotoImage(edge)



			if panelA is None or panelB is None:

				panela=Label(image=img)
			
				panela.pack(side='left',padx=10,pady=10)
				
				panelb=Label(image=edge)

				panelb.pack(side='right',padx=10,pady=10)


			else:

				pannelA.configure(image=img)

				panelB.configure(image=edge)

				panelA.image=img

				panelB.image=edge
			

		else:

			print("Image Not Selected")



		root.mainloop()
