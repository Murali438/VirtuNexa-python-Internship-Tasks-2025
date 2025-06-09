from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import os

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

def split_pdf(input_path, output_dir):
    reader = PdfReader(input_path)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        output_file = os.path.join(output_dir, f'page_{i+1}.pdf')
        with open(output_file, 'wb') as f:
            writer.write(f)
