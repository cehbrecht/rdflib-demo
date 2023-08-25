from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Text


# Provide the path to the SQLite database in the local folder
database_path = "provenance_database.sqlite"

Base = declarative_base()

class RDFGraph(Base):
    __tablename__ = 'rdf_graph'
    
    id = Column(Integer, primary_key=True)
    graph_data = Column(Text)

class GraphDB(object):
    def __init__(self):
        # Create a SQLAlchemy engine
        self.engine = create_engine(f'sqlite:///{database_path}', echo=True)

        # Create the table(s) in the database
        Base.metadata.create_all(self.engine)

        # Create a session factory
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add(self, rdf_graph):
        # Create an instance of your data model
        rdf_graph_instance = RDFGraph(graph_data=rdf_graph)

        # Add the instance to the session
        self.session.add(rdf_graph_instance)

        # Commit the changes to the database
        self.session.commit()

        # Close the session when done
        self.session.close()