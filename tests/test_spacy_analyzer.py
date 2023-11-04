import unittest
from spacy_analyzer.SpacyAnalyzer import SpacyAnalyzer

class TestSpacyAnalyzer(unittest.TestCase):
	
	annotated_doc = None

	def setUp(self):
		if TestSpacyAnalyzer.annotated_doc is None:
			self.text = "However, screening for TP53 germline mutation in patients with early onset breast cancer and unselected for familial history has shown TP53 mutations in 2% – 3% of the cases (Lalloo et al. 2006), whereas screening of 525 patients with any kind of cancer family history has identified 91 (17.3%) TP53 mutations (Gonzalez et al. 2009)."
			self.annotated_doc = SpacyAnalyzer.analyze(self.text)		

	def test_analyze(self):		
		self.assertGreater(len(self.annotated_doc.ents), 1)

	def test_find_co_occurance(self):
		self.assertEqual(len(SpacyAnalyzer.find_co_occurance(self.annotated_doc)),1)
