from PyPDF4 import PdfFileReader, PdfFileWriter
from PyPDF4.pdf import ContentStream
from PyPDF4.generic import TextStringObject, NameObject
from PyPDF4.utils import b_
import aspose.slides as slides

def remove_watermark(wm_text, inputFile, outputFile):
    
    
    with open(inputFile, "rb") as f:
        source = PdfFileReader(f, "rb")
        output = PdfFileWriter()

        for page in range(source.getNumPages()):
            page = source.getPage(page)
            content_object = page["/Contents"].getObject()
            content = ContentStream(content_object, source)

            for operands, operator in content.operations:
                if operator == b_("Tj"):
                    text = operands[0]
                    
                    if isinstance(text, str) and (text.startswith(wm_text[0]) or text.startswith(wm_text[1]) or text.startswith(wm_text[2])):
                        operands[0] = TextStringObject('')

            page.__setitem__(NameObject('/Contents'), content)
            output.addPage(page)

        with open(outputFile, "wb") as outputStream:
            output.write(outputStream)
            



def generate_pdf(input_file,output_path):
    pres = slides.Presentation(input_file)

    # Create PDF options
    options = slides.export.PdfOptions()

    # Include hidden slides
    options.show_hidden_slides = True

    # Save PPTX as PDF
    pres.save("output.pdf", slides.export.SaveFormat.PDF, options)

    wm_text = ['Evaluation only.','Created with Aspose.Slides for .NET Standard 2.0 23.8.','Copyright 2004-2023Aspose Pty Ltd.']

    inputFile = r'output.pdf'
    remove_watermark(wm_text, inputFile, output_path)

# generate_pdf('output.pptx')
