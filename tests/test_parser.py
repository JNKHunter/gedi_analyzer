import unittest
import requests
from parser.PDFParser import PDFParser
from io import BytesIO

class TestPDFDownloader(unittest.TestCase):
	
	def test_reader(self):

		pdf_bytes = b'%PDF-1.7\n\n1 0 obj  % entry point\n<<\n  /Type /Catalog\n  /Pages 2 0 R\n>>\nendobj\n\n2 0 obj\n<<\n  /Type /Pages\n  /MediaBox [ 0 0 200 200 ]\n  /Count 1\n  /Kids [ 3 0 R ]\n>>\nendobj\n\n3 0 obj\n<<\n  /Type /Page\n  /Parent 2 0 R\n  /Resources <<\n    /Font <<\n      /F1 4 0 R \n    >>\n  >>\n  /Contents 5 0 R\n>>\nendobj\n\n4 0 obj\n<<\n  /Type /Font\n  /Subtype /Type1\n  /BaseFont /Times-Roman\n>>\nendobj\n\n5 0 obj  % page content\n<<\n  /Length 44\n>>\nstream\nBT\n70 50 TD\n/F1 12 Tf\n(Hello, world!) Tj\nET\nendstream\nendobj\n\nxref\n0 6\n0000000000 65535 f \n0000000010 00000 n \n0000000079 00000 n \n0000000173 00000 n \n0000000301 00000 n \n0000000380 00000 n \ntrailer\n<<\n  /Size 6\n  /Root 1 0 R\n>>\nstartxref\n492\n%%EOF'

		pdf_content = bytearray(pdf_bytes)		
		reader = PDFParser.get_reader(pdf_content)
		
		self.assertEqual(len(reader.pages), 1)

	def test_extract_text(self):
		pdf_bytes = b'%PDF-1.7\n\n1 0 obj  % entry point\n<<\n  /Type /Catalog\n  /Pages 2 0 R\n>>\nendobj\n\n2 0 obj\n<<\n  /Type /Pages\n  /MediaBox [ 0 0 200 200 ]\n  /Count 1\n  /Kids [ 3 0 R ]\n>>\nendobj\n\n3 0 obj\n<<\n  /Type /Page\n  /Parent 2 0 R\n  /Resources <<\n    /Font <<\n      /F1 4 0 R \n    >>\n  >>\n  /Contents 5 0 R\n>>\nendobj\n\n4 0 obj\n<<\n  /Type /Font\n  /Subtype /Type1\n  /BaseFont /Times-Roman\n>>\nendobj\n\n5 0 obj  % page content\n<<\n  /Length 44\n>>\nstream\nBT\n70 50 TD\n/F1 12 Tf\n(Hello, world!) Tj\nET\nendstream\nendobj\n\nxref\n0 6\n0000000000 65535 f \n0000000010 00000 n \n0000000079 00000 n \n0000000173 00000 n \n0000000301 00000 n \n0000000380 00000 n \ntrailer\n<<\n  /Size 6\n  /Root 1 0 R\n>>\nstartxref\n492\n%%EOF'

		pdf_content = bytearray(pdf_bytes)		
		reader = PDFParser.get_reader(pdf_content)

		self.assertEqual(PDFParser.extract_text(reader), "Hello, world!")
