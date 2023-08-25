from provdemo.db import GraphDB
from provdemo.provenance import Provenance

prov = Provenance()
prov.build()
rdf_graph = prov.get_rdf_graph()

# write to store
graph_db = GraphDB()
graph_db.add(rdf_graph)

# query store
graph_db.query()


