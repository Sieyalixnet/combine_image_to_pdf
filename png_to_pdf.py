import img2pdf
from PIL import Image
import PyPDF2

def combine_pdf(img_pathes,output_path):
    pdf_merger = PyPDF2.PdfMerger()
    for img_path in img_pathes:
        image = Image.open(img_path)
        pdf_bytes = img2pdf.convert(image.filename)
        file = open("./avif_temp_pdf.pdf", "wb")
        file.write(pdf_bytes)
        pdf_merger.append(PyPDF2.PdfReader("./avif_temp_pdf.pdf", strict=False))
    pdf_merger.write("./"+output_path+".pdf")
    pdf_merger.close()