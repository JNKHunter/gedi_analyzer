import requests
from celery import Celery

class PDFDownloader():
	def __init__(self):
		pass

	@classmethod
	def download(cls, url):
		try:
			response = requests.get(url)
			response.raise_for_status()

			if response.status_code == 200:				
				return response.content
			else:
				return None
		except requests.exceptions.RequestException as e:
			raise e