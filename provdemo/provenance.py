from prov.model import ProvDocument
from prov.identifier import Namespace


ex = Namespace("ex", uri="http://example.org/")

class Provenance(object):
    def __init__(self):
        self.doc = ProvDocument()
        self.doc.add_namespace(ex)

    def build(self):
        entity = self.doc.entity(ex["Entity"])
        activity = self.doc.activity(ex["Activity"])
        agent = self.doc.agent(ex["Agent"])

        # Associate the entity with the activity
        self.doc.wasGeneratedBy(entity, activity)

        # Associate the activity with the agent
        self.doc.wasAssociatedWith(activity, agent)

    def get_provn(self):
        return self.doc.get_provn()
    
    def get_rdf_graph(self):
        # Serialize the PROV document to RDF format
        rdf_graph = self.doc.serialize(format="rdf", rdf_format="turtle")
        return rdf_graph