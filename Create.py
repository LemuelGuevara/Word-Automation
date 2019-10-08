import os
from docx import Document

path = r'C:\\Users\\lemue_000\Documents\\School Projects\\'

docx_name = input('Create File: ')  #Input of the user
document = Document(path + (docx_name + '.docx')).save()  #Makes the word file and saves it
print("Document successfuly made and saved.")
os.startfile(docx_path)  #Initializes the file 
