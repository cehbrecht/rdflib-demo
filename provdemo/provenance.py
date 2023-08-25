from prov.model import ProvDocument
from prov.identifier import Namespace
from datetime import datetime


EX = Namespace("ex", uri="http://example.org/")

class Provenance(object):
    def __init__(self):
        self.doc = ProvDocument()
        self.doc.add_namespace(EX)

    def build(self):
        # Create an activity for the processing step
        process_activity = self.doc.activity(EX["process_step"], startTime=datetime.now())

        # Create entities for input and output
        input_entity = self.doc.entity(EX["input_data"], other_attributes={EX["value"]: 5})
        output_entity = self.doc.entity(EX["output_data"], other_attributes={EX["value"]: 25})

        # Associate input entity with the process activity
        self.doc.wasGeneratedBy(output_entity, process_activity)

        # Associate output entity with the process activity
        self.doc.used(process_activity, input_entity)

    def get_provn(self):
        return self.doc.get_provn()
    
    def get_rdf_graph(self):
        # Serialize the PROV document to RDF format
        rdf_graph = self.doc.serialize(format="rdf", rdf_format="turtle")
        return rdf_graph
    
    def write_rdf(self):
        # Save the provenance information to a file
        with open("provenance_example.prov.ttl", "w") as f:
            f.write(self.get_rdf_graph())