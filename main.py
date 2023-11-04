from downloader.PDFDownloader import PDFDownloader
from parser.PDFParser import PDFParser
from spacy_analyzer.SpacyAnalyzer import SpacyAnalyzer

uri = 'https://pubmed-boulder.s3.us-east-2.amazonaws.com/cshperspect-PFT-a001008.pdf'
pdf_content = PDFDownloader.download(uri)
reader = PDFParser.get_pypdf2_reader(pdf_content)
text_content = PDFParser.extract_text(reader)
doc = SpacyAnalyzer.analyze(text_content)
SpacyAnalyzer.find_co_occurance(doc)