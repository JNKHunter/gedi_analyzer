import io
import PyPDF2

# Open the PDF file
with open('helloworld.pdf', 'rb') as pdf_file:
    # Create a BytesIO object
    pdf_bytesio = io.BytesIO(pdf_file.read())

# Now you can use pdf_bytesio as if it were a file-like object
# For example, you can pass it to PyPDF2 for further processing
pdf_reader = PyPDF2.PdfFileReader(pdf_bytesio)

# Example: Print the number of pages in the PDF
print(f"Number of pages in the PDF: {pdf_reader.numPages}")

# Close the BytesIO object (optional, but a good practice)
pdf_bytesio.close()