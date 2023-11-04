import spacy
import re

class SpacyAnalyzer():
	def __init__(self):
		pass

	@classmethod
	def analyze(cls, text_content):
		nlp = spacy.load("en_ner_bionlp13cg_md")
		return nlp(text_content)

	@classmethod
	def find_co_occurance(cls, nlp_doc):		
		co_occurance_dict = {}
		for ent in nlp_doc.ents:			
			if ent.label_ == "GENE_OR_GENE_PRODUCT": 				
 			  	if ent.sent not in co_occurance_dict:
 			  		co_occurance_dict[ent.sent] = []
 			  		co_occurance_dict[ent.sent].append(ent.text)
		

		for ent in nlp_doc.ents:
			if ent.label_ == "CANCER":				
				if re.match("[a-z]+ cancer", ent.text):
					if ent.sent in co_occurance_dict:
						co_occurance_dict[ent.sent].append(ent.text)

		co_keys = list(co_occurance_dict.keys())
		for key in co_keys:
			if len(co_occurance_dict[key]) != 2:
				del co_occurance_dict[key]

		co_occurances = []
		for key in co_occurance_dict:
			co_occurances.append(co_occurance_dict[key])

		return co_occurances

 		
