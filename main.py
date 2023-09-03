from fastapi import FastAPI, File, UploadFile,Response
from fastapi.responses import FileResponse
from conversion import convert_docx2pdf
from ppit_to_pdf import generate_pdf
from excel_conv import generate_pdf_from_excel
from typing import List
from pdfconv import generate_excel_from_pdf
import random
import img2pdf
app = FastAPI()
from conversion import *
import os

folder_name = "user_files"
folder_name2 = "static"
if not os.path.exists(folder_name) or not os.path.exists(folder_name2):
    os.makedirs(folder_name)
    os.makedirs(folder_name2)
    print(f"Folder '{folder_name}' created successfully.")
else:
    print(f"Folder '{folder_name}' already exists.")


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/docx_to_pdf/")
async def upload_file(file: UploadFile = File(...)):
    random_number = random.randrange(100000, 1000000)
    random_name = str(random_number)
    upload_dir = "user_files"
    file_path = os.path.join(upload_dir, file.filename)
    if file.filename.endswith('.docx') or file.filename.endswith('.doc'):
       with open(file_path, "wb") as f:
            f.write(file.file.read())
       convert_docx2pdf(f"user_files/{file.filename}",f"{os.path.splitext(file.filename)[0]}.pdf")
       return FileResponse(f"{os.path.splitext(file.filename)[0]}.pdf", media_type="application/pdf")
    
    else:
        return {"error": "Unsupported file format"}

@app.post("/pdf_to_docx/")
async def upload_file(file: UploadFile = File(...)):
    random_number = random.randrange(100000, 1000000)
    random_name = str(random_number)
    upload_dir = "user_files"
    file_path = os.path.join(upload_dir, file.filename)
    if file.filename.endswith('.pdf'):
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        convert_pdf2docx(f"user_files/{file.filename}",f"{random_name}.docx")  
        return FileResponse(path=f"{random_name}.docx",filename=f"{random_name}.docx",media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    else:
        return {"error": "Unsupported file format"}


@app.post("/ppit_to_pdf/")
async def upload_file(file: UploadFile = File(...)):
    random_number = random.randrange(100000, 1000000)
    random_name = str(random_number)
    upload_dir = "user_files"
    file_path = os.path.join(upload_dir, file.filename)
    if file.filename.endswith('.ppt') or file.filename.endswith('.pptx'):
       with open(file_path, "wb") as f:
            f.write(file.file.read())
            
       generate_pdf(f"user_files/{file.filename}",f"{random_name}.pdf")
       return FileResponse(f"{random_name}.pdf", media_type="application/pdf")
    else:
        return {"error": "Unsupported file format"}

@app.post("/excel_to_pdf/")
async def upload_file(file: UploadFile = File(...)):
    upload_dir = "user_files"
    random_number = random.randrange(100000, 1000000)
    random_name = str(random_number)
    file_path = os.path.join(upload_dir, file.filename)
    if file.filename.endswith('.xlsx') or file.filename.endswith('.csv'):
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        generate_pdf_from_excel(f"user_files/{file.filename}",f"{random_name}.pdf")
        return FileResponse(f"{random_name}.pdf", media_type="application/pdf")
    else:
        return {"error": "Unsupported file format"}
    

@app.post("/pdf_to_excel/")
async def upload_file(file: UploadFile = File(...)):
    random_number = random.randrange(100000, 1000000)
    random_name = str(random_number)
    upload_dir = "user_files"
    file_path = os.path.join(upload_dir, file.filename)
    if file.filename.endswith('.pdf'):
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        generate_excel_from_pdf(f"user_files/{file.filename}",f"{random_name}.csv")
        return FileResponse(f"{random_name}.csv",media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename=f"{random_name}.csv")
    else:
        return {"error": "Unsupported file format"}

@app.post("/imgs_to_pdf/")
async def upload_file(images: List[UploadFile] = File(...)):
    random_number = random.randrange(100000, 1000000)
    random_name = str(random_number)
    try:
        uploaded_images = []
        for img in images:
            with open(f"user_files/{img.filename}", "wb") as f:
                f.write(img.file.read())
                uploaded_images.append(f"user_files/{img.filename}")
        with open(f"{random_name}.pdf", "wb") as pdf_file:
            pdf_file.write(img2pdf.convert(uploaded_images))
        return FileResponse(f"{random_name}.pdf", media_type="application/pdf")
    except:
        return {"error": "Unsupported file format"}
