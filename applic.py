from lib import *
class ImagePro(object):
	@classmethod
	def App(self):
		# grab a reference to the image panels
	# open a file chooser dialog and allow the user to select an input
	# image
		path=tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpeg"),("jpg files","*.jpg"),("png files","*.png"),("all files","*.*")))

	# ensure a file path was selected
		if len(path) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
			img = cv2.imread(path)
			img1=cv2.imread(path)
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			face_cascade=cv2.CascadeClassifier('C://Gui_with_OpenCv_project1/Haar_Cascade_Dataset/haarcascade_onfrtalface_default.xml')
			eye_cascade=cv2.CascadeClassifier('C://Gui_with_OpenCv_project1/Haar_Cascade_Dataset/haarcascade_eye.xml')
			faces=face_cascade.detectMultiScale(gray,1.6,2)
			for (x,y,w,h) in faces:
				cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
				roi_gray=gray[y:y+h,x:x+w]
				roi_color=img[y:y+h,x:x+w]
				eyes=eye_cascade.detectMultiScale(roi_gray)
				for (ex,ey,ew,eh) in eyes:
					cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
			img1,img=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB),cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
		# convert the images to PIL format...
			img1 = Image.fromarray(img1)
			img = Image.fromarray(img)
		# ...and then to ImageTk format
			img1 = ImageTk.PhotoImage(img1)
			img = ImageTk.PhotoImage(img)
		# if the panels are None, initialize them
			if panelA is None or panelB is None:
			# the first panel will store our original image
				panelA = Label(image=img1)
				panelA.image = img1
				panelA.pack(side="left", padx=10, pady=10)
			# while the second panel will store the edge map
				panelB = Label(image=img)
				panelB.image = img
				panelB.pack(side="right", padx=10, pady=10)
		# otherwise, update the image panels
			else:
			# update the pannels
				panelA.configure(image=img1)
				panelB.configure(image=img)
				panelA.image = img1
				panelB.image = img
# initialize the window toolkit along with the two image panels
root = Tk()
panelA = None
panelB = None
obj=ImagePro()
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
root.geometry('{}x{}'.format(1080,480))
btn = Button(root, text="Select an image", command=obj.App)
btn.pack(side="bottom", fill="y", expand="no", padx="10", pady="10")
 
# kick off the GUI
root.mainloop()

