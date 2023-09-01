
import aspose.cells as apc

import fitz  # PyMuPDF

def remove_text_from_pdf(input_pdf_path, output_pdf_path, text_to_remove):
    doc = fitz.open(input_pdf_path)

    for page_number in range(doc.page_count):
        page = doc.load_page(page_number)
        draft = page.search_for(text_to_remove)

        for rect in draft:
            annot = page.add_redact_annot(rect)
            page.apply_redactions()
            page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)

    doc.save(output_pdf_path, garbage=3, deflate=True)
    doc.close()
    
def generate_pdf_from_excel(input_path,outputFile):
# Load the Excel file
    workbook = apc.Workbook(input_path)

    # Get the first worksheet
    worksheet = workbook.worksheets.get(0)
    for col in range(worksheet.cells.max_column + 1):
        worksheet.auto_fit_column(col)
    # Create a PDF save options object
    pdf_save_options = apc.PdfSaveOptions()

    # Set the page layout to one page per sheet
    pdf_save_options.one_page_per_sheet=True

    # Set the output PDF file path
    
    output_path='Ooutput.pdf'
    # Save the workbook as a PDF
    workbook.save(output_path, pdf_save_options)
    
    remove_text_from_pdf(output_path,outputFile,'Evaluation Only. Created with Aspose.Cells for .NET.Copyright 2003 - 2023 Aspose Pty Ltd.')

# generate_pdf_from_excel('scccs.xlsx','output.pdf')



