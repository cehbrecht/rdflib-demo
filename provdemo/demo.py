from prov.model import ProvDocument
from prov.identifier import Namespace

from provdemo.db import GraphDB


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

# write to store
graph_db = GraphDB()
graph_db.add(rdf_graph)


