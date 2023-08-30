from rdflib import Graph, URIRef

# Provide the path to the SQLite database in the local folder
DB_URL = "sqlite:///provenance.db"

class GraphDB(object):
    def __init__(self):
        # Create a graph with a specific backend store
        self.graph = Graph(
            store="SQLAlchemy", 
            identifier=URIRef("http://example.org/graph"))
        self.graph.open(DB_URL, create=True)

    def add(self, data):
        new_graph = Graph()
        new_graph.parse(data=data, format="turtle")

        # add rdf to existing graph
        for triple in new_graph:
            self.graph.add(triple)
        # Commit changes to the store
        self.graph.commit()

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
        print(f"\n\nquery: results={len(results)}")
        for row in results:
            # print(row)
            pass
