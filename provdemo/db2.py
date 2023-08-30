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

        # Add some data to the graph
        self.graph.add((URIRef("http://example.org/subject1"), RDF.type, URIRef("http://example.org/Person")))
        self.graph.add((URIRef("http://example.org/subject1"), URIRef("http://example.org/name"), Literal("Alice")))

        # Commit the changes to the database
        self.graph.commit()

    def add(self, data):
        return
        new_graph = Graph()
        new_graph.parse(data=data, format="turtle")
        # dummy
        new_graph = Graph()

        # Add some data to the graph
        new_graph.add((URIRef("http://example.org/subject1"), RDF.type, URIRef("http://example.org/Person")))
        new_graph.add((URIRef("http://example.org/subject1"), URIRef("http://example.org/name"), Literal("Alice")))


        # add rdf to existing graph
        for triple in new_graph:
            print(triple)
            self.graph.add(triple)
        # Commit changes to the store
        self.graph.store.commit()

    def query(self):
        # Define and execute a SPARQL query
        query = """
            SELECT ?subject ?name
            WHERE {
                ?subject a <http://example.org/Person> .
                ?subject <http://example.org/name> ?name .
            }
        """

        results = self.graph.query(query)

        # Print the query results
        for row in results:
            subject, name = row
            print(f"Subject: {subject}, Name: {name}")
