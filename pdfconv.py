import tabula
def generate_excel_from_pdf(input_pdf,output_excel):
    df = tabula.read_pdf(input_pdf, pages='all',java_options='-Djava.awt.headless=true -Xmx4G')
    tabula.convert_into(input_pdf, output_excel, output_format="csv", pages='all')
    

