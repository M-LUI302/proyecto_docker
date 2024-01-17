from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import declarative_base


engine = create_engine('sqlite:///Asistencia.db')
db_session = scoped_session(sessionmaker(engine))

Database = declarative_base()