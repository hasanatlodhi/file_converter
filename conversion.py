from pdf2docx import parse,Converter
from docx2pdf import convert
# from openpyxl import load_workbook
# import pandas as pd
# import img2pdf
# from PIL import Image
# from find_water import remove_watermark_from_page

# from docx import Document

def convert_pdf2docx(input_file: str, output_file: str):
    cv = Converter(input_file)
    cv.convert(output_file, start=0, end=None)
    cv.close()


def convert_docx2pdf(input_word_path,output_pdf_path):
    convert(input_word_path, output_pdf_path)


# from reportlab.lib.pagesizes import letter
# from reportlab.lib import utils
# from reportlab.pdfgen import canvas
# from io import BytesIO

# def image_to_pdf(image_path):
#     with open(output_pdf_path, "wb") as pdf_file:
#         pdf_file.write(img2pdf.convert(image_paths))

# convert_pdf2docx('mypdf.pdf','worddy.docx')
# convert_docx2pdf('worddy.docx','mypdf.pdf')
# image_to_pdf('imgPD.png')
