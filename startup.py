#!/usr/bin/python
import os


print
print "Checking Matplotlib"
try:
	
	import matplotlib.pyplot as plt
	
except ImportError:
	print "Installing Matplotlib.."
	os.system("pip install  matplotlib")
	print("Installed..")


print
print "Checking itertools"
try:
	
	import itertools
except ImportError:
	print "Installing itertools.."
	os.system("pip install itertools")
	print("Installed..")


print
print "Checking threading"
try:
	
	import threading
except ImportError:
	print "Installing threading.."
	os.system("pip install threading")
	print("Installed..")



print
print "Checking PIL"
try:
	
	import PIL
except ImportError:
	print "Installing PIL.."
	os.system("pip install Pillow")
	print("Installed..")

print
print "Checking Time"
try:
	
	import time
except ImportError:
	print "Installing Time.."
	os.system("pip install time")
	print("Installed..")


print
print "Checking OPENCV"
try:
	
	import cv2
except ImportError:
	print "Installing OPENCV.."
	os.system("pip install opencv-python")
	print("Installed..")

print
print "Checking numpy"
try:
	
	import numpy as np
except ImportError:
	print "Installing numpy.."
	os.system("pip install numpy")
	print("Installed..")

print
print "Checking Tkinter"
try:
	
	import tkinter
except execption as e:
	
	print(str(e))


print
print "you're ready to go!"

