from prov.model import ProvDocument
from prov.identifier import Namespace
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Text

Base = declarative_base()

class RDFGraph(Base):
    __tablename__ = 'rdf_graph'
    
    id = Column(Integer, primary_key=True)
    graph_data = Column(Text)

# Create a new PROV document
prov_doc = ProvDocument()

# Define namespaces
ex = Namespace("example", uri="urn:example:")
prov_doc.add_namespace(ex)

# Create entities, activities, and agents
entity = prov_doc.entity(ex["Entity"])
activity = prov_doc.activity(ex["Activity"])
agent = prov_doc.agent(ex["Agent"])

# Associate the entity with the activity
prov_doc.wasGeneratedBy(entity, activity)

# Associate the activity with the agent
prov_doc.wasAssociatedWith(activity, agent)

# Serialize the PROV document to RDF format
rdf_graph = prov_doc.serialize(format="rdf", rdf_format="turtle")

# Provide the path to the SQLite database in the local folder
database_path = "provenance_database.sqlite"

# Create a SQLAlchemy engine
engine = create_engine(f'sqlite:///{database_path}', echo=True)

# Create the table(s) in the database
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

# Create an instance of your data model
rdf_graph_instance = RDFGraph(graph_data=rdf_graph)

# Add the instance to the session
session.add(rdf_graph_instance)

# Commit the changes to the database
session.commit()

# Close the session when done
session.close()
