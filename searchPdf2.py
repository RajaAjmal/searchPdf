import PyPDF2
import re
import os
from multiprocessing import Pool
import time
example = '/home/joe/PycharmProjects/PDFsearch'

def find_pdfs(directory):
    pdfs = []
    for foldername, subfolder, files in os.walk(directory):
        for file in files:
            if '.pdf' in file:
                pdfs.append(foldername + '/' + file)
    return pdfs

def search_pdf(critera):
    search_term, path = critera
    try:
        pdf = PyPDF2.PdfFileReader(path)
        try:
            for n in range(0, pdf.getNumPages()):
                page = pdf.getPage(n)
                text = page.extractText().lower()
                search = re.search(search_term, text)
                if search != None:
                    print(path)
                    break
        except:
            print ('cannot extract text')
    except:
        print ('PDF file corrupt')


term = input('Enter search word: ')
choice = int(input('1.	SC\n2.	HSC \nSelect a folder:  '))

thread_count = int(input('How many threads would you like to devote? '))

if choice == 1:
    cho = '/media/raja/316E396D3C478D8A/pdrv/computer science/SC/'
else:
    cho = '/media/raja/316E396D3C478D8A/pdrv/computer science/HSC/'

pdfs = find_pdfs(cho)
startTime= time.time()
search_crit = []
for pdf in pdfs:
    search_crit.append((term, pdf))

with Pool(thread_count) as p:
        p.map(search_pdf, search_crit)
dur = time.time() - startTime
print (dur)
