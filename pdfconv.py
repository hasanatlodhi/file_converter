import tabula
import aspose.pdf as pdf
def generate_excel_from_pdf(input_pdf,output_excel):
    # Load input PDF document
    document = pdf.Document(input_pdf)
    
    # Initialize the ExcelSaveOptions
    excelSaveOptions = pdf.ExcelSaveOptions()
    
    # Convert the PDF to Excel workbook
    document.save(output_excel, excelSaveOptions)
    
    print("Conversion process completed")
    

