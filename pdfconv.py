import tabula
import aspose.pdf as pdf
import time
def generate_excel_from_pdf(input_pdf,output_excel):
    # Load input PDF document
    document = pdf.Document(input_pdf)
    
    # Initialize the ExcelSaveOptions
    excelSaveOptions = pdf.ExcelSaveOptions()
    
    # Convert the PDF to Excel workbook
    nm=round(time.time())
    document.save(f'{nm}.xlsx', excelSaveOptions)
    
    workbook = openpyxl.load_workbook(f'{nm}.xlsx')

    # String to search for and remove
    search_string = "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2023 Aspose Pty Ltd."
    
    # Iterate through all sheets in the workbook
    for worksheet in workbook.sheetnames:
        current_sheet = workbook[worksheet]
        for row in current_sheet.iter_rows(min_row=1, max_row=3):
            for cell in row:
                if cell.value == search_string:
                    cell.value = ""
    
    # Save the modified Excel file
    workbook.save(output_excel)
    

