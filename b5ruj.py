#from viesis import *
#from admin import *
import fileinput
with fileinput.FileInput(files=('admin.txt','viesis.txt'),mode='r') as datne:
    for line in datne:
        print(f"Lasa datni {datne.filename()}...")
        print*(line) 