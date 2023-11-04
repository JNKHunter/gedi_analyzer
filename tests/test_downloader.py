import unittest
import requests
from downloader.PDFDownloader import PDFDownloader
from unittest.mock import patch, MagicMock
from io import BytesIO

class TestPDFDownloader(unittest.TestCase):
	
	@patch('downloader.PDFDownloader.requests')
	def test_download(self, mock_requests):
		
		pdf_content = b"%PDF-1.5 ... (sample content) ..."
		
		mock_response = MagicMock() 
		mock_response.status_code = 200
		mock_response.content = pdf_content
		mock_requests.get.return_value = mock_response

		url = "https://example.com/sample.pdf"		
		self.assertEqual(PDFDownloader.download(url), pdf_content)