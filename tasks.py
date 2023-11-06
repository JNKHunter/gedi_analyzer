from celery import Celery
from downloader.PDFDownloader import PDFDownloader
from parser.PDFParser import PDFParser
from spacy_analyzer.SpacyAnalyzer import SpacyAnalyzer
import main
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

message_broker = os.getenv('MESSAGE_BROKER')
db = os.getenv('DATABASE_URI')
app = Celery('tasks', broker=message_broker)

@app.task
def analyze(url, article_id):    
    pdf_content = PDFDownloader.download(url)
    reader = PDFParser.get_pypdf2_reader(pdf_content)
    text_content = PDFParser.extract_text(reader)
    doc = SpacyAnalyzer.analyze(text_content)    
    co_occurances = SpacyAnalyzer.find_co_occurance(doc)
    engine = create_engine(db)
    
    try:
        predications = []
        for co_occ in co_occurances:
            predications.append(main.Predication(
                gene = co_occ[0],
                disease = co_occ[1],
                pred_type = "co-occurance",
                article_id = article_id
            ))
        Session = sessionmaker(bind=engine)
        session = Session()
        session.bulk_save_objects(predications)
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()

    