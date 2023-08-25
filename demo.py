from rdflib import Graph
from prov.model import ProvDocument
from rdflib.plugins.stores.sparqlstore import SPARQLUpdateStore

# Create a new PROV document
prov_doc = ProvDocument()

# Define namespaces
ex = prov_doc.namespace("ex", "http://example.org/")

# Create entities, activities, and agents
entity = prov_doc.entity(ex["Entity"])
activity = prov_doc.activity(ex["Activity"])
agent = prov_doc.agent(ex["Agent"])

# Associate the entity with the activity
prov_doc.wasGeneratedBy(entity, activity)

# Associate the activity with the agent
prov_doc.wasAssociatedWith(activity, agent)

# Serialize the PROV document to RDF format
rdf_graph = prov_doc.serialize(format="turtle")

# Provide the path to the SQLite database in the local folder
database_path = "provenance_database.sqlite"

# Construct the SQLite URI
sqlite_uri = "sqlite:///" + database_path

# Set up the SPARQL Update Store with SQLite backend
store = SPARQLUpdateStore(queryEndpoint=sqlite_uri)

# Create a new RDF graph using the store
g = Graph(store, identifier=ex["ProvenanceGraph"])

# Add the serialized RDF graph to the store
g.parse(data=rdf_graph, format="turtle")

# Commit the graph to the store
g.commit()
