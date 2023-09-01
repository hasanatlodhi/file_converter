# import fitz  # PyMuPDF
# import re

# def preprocess_text(text):
#     # Remove extra whitespace and special characters
#     processed_text = re.sub(r'\s+', ' ', text)
#     return processed_text.strip()

# def remove_watermark_from_page(page, watermark_text):
#     text = page.get_text("textutf8")
#     processed_text = preprocess_text(text)
    
#     if watermark_text.lower() in processed_text.lower():
#         areas = page.search_for(watermark_text)
#         for quads in areas:
#             # Create white rectangles to cover the watermark text
#             page.add_redact_annot(quads)
#             page.apply_redactions()

# # Path to the PDF file
# pdf_path = "output.pdf"
# watermark_text = "Evaluation Warning : The document was created with Spire.XLS for Python"

# pdf_document = fitz.open(pdf_path)

# # Iterate through pages and remove watermark text
# for page_num in range(pdf_document.page_count):
#     page = pdf_document.load_page(page_num)
#     remove_watermark_from_page(page, watermark_text)

# # Remove the last page
# if pdf_document.page_count > 0:
#     pdf_document.delete_page(pdf_document.page_count - 1)

# # Save the modified PDF to a new file
# modified_pdf_path = "output_modified.pdf"
# pdf_document.save(modified_pdf_path)
# pdf_document.close()

# print("Watermark removed and last pag
from aspose.cells import Workbook, SaveFormat, BorderType,CellBorderType
workbook = Workbook("scccs.xlsx")

worksheets = workbook.worksheets

worksheet = worksheets.get(0)

#Hiding the grid lines of the first worksheet of the Excel file

worksheet.auto_fit_columns()

worksheet.is_gridlines_visible=False


workbook.save( "asfasfasfaslfkaslfoutput.pdf", SaveFormat.PDF)