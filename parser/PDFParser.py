from io import BytesIO
from PyPDF2 import PdfReader
import requests

class PDFParser():
	def __init__(self):
		pass

	@classmethod
	def get_reader(cls, pdf_bytes_content):
		return PdfReader(BytesIO(pdf_bytes_content))

	@classmethod
	def extract_text(cls, pdf_reader):
		
		text_content = ""
		for page in pdf_reader.pages:
			text_content += page.extract_text()

		return text_content