import os
from docx import Document

path = r'C:\\Users\\lemue_000\Documents\\School Projects\\'

docx_name = input('Create File: ')  #Input of the user
document = Document()  #Makes the word file and saves it
docx_path = path + (docx_name + '.docx')
document.save(docx_path)
print("Document successfuly made and saved.")
os.startfile(docx_path)  #Initializes the file 
