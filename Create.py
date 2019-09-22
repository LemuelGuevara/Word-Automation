import os
from docx import Document

path = r'C:\\Users\\Username\\Folder where you would save your document\\'

docx_name = input('Create ')
document = Document()
docx_path = path + (docx_name + '.docx')
document.save(docx_path) 
print("Document successfully made and saved")
os.startfile(docx_path)


