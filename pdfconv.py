import tabula
import aspose.pdf as pdf
def generate_excel_from_pdf(input_pdf,output_excel):
    # Load input PDF document
    document = pdf.Document(input_pdf)
    
    # Initialize the ExcelSaveOptions
    excelSaveOptions = pdf.ExcelSaveOptions()
    
    # Convert the PDF to Excel workbook
    document.save("scccs.xlsx", excelSaveOptions)
    
    print("Conversion process completed")

    df = tabula.read_pdf(input_pdf, pages=1)
    tabula.convert_into(input_pdf, output_excel, output_format="csv", pages='all')
    

