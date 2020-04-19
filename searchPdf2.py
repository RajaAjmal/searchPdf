from PyPDF2 import utils
import re
import os, sys, subprocess
from threading import Thread
import PyPDF2

def searchPdf(si,ch):
	found = False
	for foldername, subfolders, files in os.walk(ch):
		for file in files:
			if file[-3:] == 'pdf':
				try:
					object = PyPDF2.PdfFileReader(os.path.join(foldername, file))
					numPages = object.getNumPages()
					try:
						for i in range (0,numPages):
							pageObj = object.getPage(i)
							text = pageObj.extractText()
							textCase = text.lower()
							resSearch = re.search(si,textCase)
							if resSearch != None:
								found = True
								print(file)
								break
					except:
						print ('Cannot extract text from ' + file)
				except:
					print (file + ' is corrupt')
	print ('Search completed')
	if found == False:
		print ('Searched words not found')
		
searchedItem = input ('Enter search word: ')
print ('1.	SC')
print('2.	HSC')
choice = int(input('Select a folder:  '))
if choice == 1:
	cho = '/media/raja/316E396D3C478D8A/pdrv/computer science/SC/'
else:
	cho = '/media/raja/316E396D3C478D8A/pdrv/computer science/HSC/'

searchPdf (searchedItem,cho)
