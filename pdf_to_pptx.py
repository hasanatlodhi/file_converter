# # import aspose.slides as slides
# # import aspose.pydrawing as drawing
        
# # with slides.Presentation() as pres:
# #     pres.slides.add_from_pdf("pdfslide.pdf")
# #     pres.save("OutputPresentation.pptx", slides.export.SaveFormat.PPTX)

# # import aspose.words as aw

# # # Load word document
# # doc = aw.Document("user_files/Measurements.docx")

# # # Save as PDF
# # doc.save("PDF.pdf")
# import fitz  # PyMuPDF
# from skimage.metrics import structural_similarity as ssim
# from skimage.io import imread
# import numpy as np
# import matplotlib.pyplot as plt
# import cv2
# import io
# # Load images
# image1 = cv2.imread("user_files/remove_img.png")
# new_size = (100, 100)  # Set your desired size
# image1 = cv2.resize(image1, new_size)
# # imread()

# # Convert bytes to a Pillow Image object


# # Convert to RGB format if not already in RGB


# def extract_images_from_pdf(pdf_path, output_folder):
#     pdf_document = fitz.open(pdf_path)
    
#     for page_num in range(pdf_document.page_count):
#         page = pdf_document[page_num]
#         image_list = page.get_images(full=True)
#         for img_index, img_info in enumerate(image_list):
#             xref = img_info[0]
#             base_image = pdf_document.extract_image(xref)
#             print(img_info)
#         #     image_io = io.BytesIO(base_image['image'])

#         #     # Read image from BytesIO using OpenCV
#         #     image_data = image_io.getvalue()  # Convert BytesIO to bytes-like object
#         #     image_cv = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)
#         #     image_cv = cv2.resize(image_cv, new_size)
#         #     mse_similarity = np.mean((image1 - image_cv)**2)
            
#     pdf_document.save("output_path.pdf")
#     pdf_document.close()


# # Usage

# pdf_path = "pdfslide.pdf"
# output_folder = "user_files"


# # def pdf_to_pptx(pdf_file, pptx_file):
# # convert_pdf2pptx(pdf_path,"masfas.pptx",start_page=0,page_count=None,resolution=300,op)
#     # cv.convert("pptx_file.pptx", start=0, end=None)
#     # cv.close()

# # extract_images_from_pdf(pdf_path, output_folder)

import subprocess

def convert_doc_to_docx(input_doc_path, output_docx_path):
    try:
        subprocess.run(['unoconv', '--format=docx', '--output', output_docx_path, input_doc_path])
        print(f"Conversion from '{input_doc_path}' to '{output_docx_path}' successful.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to your original .doc file and the output path for the new .docx file
doc_file_path = 'assign_2jkjk.doc'
docx_file_path = 'document.docx'

# Convert .doc to .docx
convert_doc_to_docx(doc_file_path, docx_file_path)
