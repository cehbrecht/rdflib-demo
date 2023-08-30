from provdemo.db2 import GraphDB
from provdemo.provenance import Provenance

def cli():
    prov = Provenance()
    prov.build()
    rdf_data = prov.get_rdf_graph()

    # write to store
    graph_db = GraphDB()
    graph_db.add(rdf_data)

    # query store
    graph_db.query()

    # write 
    prov.write_rdf()


