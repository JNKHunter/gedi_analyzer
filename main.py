# from downloader.PDFDownloader import PDFDownloader
# from parser.PDFParser import PDFParser
# from spacy_analyzer.SpacyAnalyzer import SpacyAnalyzer

#uri = 'https://pubmed-boulder.s3.us-east-2.amazonaws.com/cshperspect-PFT-a001008.pdf'
#pdf_content = PDFDownloader.download(uri)
#reader = PDFParser.get_pypdf2_reader(pdf_content)
#text_content = PDFParser.extract_text(reader)
#doc = SpacyAnalyzer.analyze(text_content)
#print(len(doc.ents))
#SpacyAnalyzer.find_co_occurance(doc)

from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
import tasks
import json
import os

parser = reqparse.RequestParser()
parser.add_argument('title', location='form')
parser.add_argument('uri', location='form')

def setup_database(app):    
    db_uri = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db = SQLAlchemy(app)
    return db

app = Flask("annotate")
api = Api(app)
db = setup_database(app)

class ArticleProcessor(Resource):

	def post(self):
		args = parser.parse_args()		

		new_article = Article(
			title=args['title'],
			uri=args['uri'])

		db.session.add(new_article)
		db.session.commit()

		tasks.analyze.delay(args['uri'], new_article.id)

		return new_article.id, 201		

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    uri = db.Column(db.String(255))    

class Predication(db.Model):
    __tablename__ = 'predications'

    id = db.Column(db.Integer, primary_key=True)
    gene = db.Column(db.String(100))
    disease =  db.Column(db.String(100))
    pred_type = db.Column(db.String(100))
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), nullable=False)

api.add_resource(ArticleProcessor, '/article')

if __name__ == '__main__':
	app.run()