from sqlalchemy import db

engine = db.create_engine("mysql://root:14072002@localhost/pjalmox")

conn = engine.connect()