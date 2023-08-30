from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF

# Provide the path to the SQLite database in the local folder
db_url = "sqlite:///my_rdf_store.db"

class GraphDB(object):
    def __init__(self):
        # Create a graph with a specific backend store
        self.graph = Graph(
            store="SQLAlchemy", 
            identifier=URIRef("http://example.org/graph"))
        self.graph.open(db_url, create=True)

    def add(self, data):
        new_graph = Graph()
        new_graph.parse(data=data, format="turtle")

        # add rdf to existing graph
        for triple in new_graph:
            print(triple)
            self.graph.add(triple)
        # Commit changes to the store
        self.graph.store.commit()

    def query(self):
        # Define and execute a SPARQL query
        query = """
            SELECT ?s ?p ?o
            WHERE {
                ?s ?p ?o .
            }
        """

        results = self.graph.query(query)

        # Print the query results
        print(f"query: results={len(results)}")
        for row in results:
            print(row)
