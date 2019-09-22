import os
from docx import Document

path = r'C:\\Users\\lemue\\Documents\\School Files\\'

docx_name = input('Create ')
document = Document()
docx_path = path + (docx_name + '.docx')
document.save(docx_path) 
print("Document successfully made and saved")
os.startfile(docx_path)


