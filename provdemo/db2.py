from rdflib import Graph, URIRef
from rdflib_sqlalchemy import registerplugins
from sqlalchemy import create_engine

# Provide the path to the SQLite database in the local folder
db_url = "sqlite:///my_rdf_store.db"

class GraphDB(object):
    def __init__(self):
        # Create a graph with a specific backend store
        self.graph = Graph(
            store="SQLAlchemy", 
            identifier=URIRef("http://example.org/graph1"))
        self.graph.open(db_url, create=True)

    def add(self, rdf_graph):
        new_graph = Graph()
        new_graph.parse(data=rdf_graph, format="turtle")
        # add rdf to existing graph
        for triple in new_graph:
            print(triple)
            self.graph.add(triple)
        # Commit changes to the store
        self.graph.store.commit()

    def query(self):
        # You can now run SPARQL queries on the stored data
        query = """
            SELECT ?s ?p ?o
            WHERE {
                ?s ?p ?o .
            }
        """
        # for row in self.graph.query(query):
        #    print(row)