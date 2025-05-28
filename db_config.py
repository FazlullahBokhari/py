from sqlalchemy import create_engine, MetaData

DB_URL = 'mysql+pymysql://root:1234@localhost/pyDb'

engine = create_engine(DB_URL)
metadata = MetaData()
metadata.reflect(bind=engine)

for table in metadata.tables.keys():
    print(table)

