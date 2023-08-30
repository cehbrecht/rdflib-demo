from provdemo.db import GraphDB

def query_all():
    graph_db = GraphDB()
   
    # Define and execute a SPARQL query
    query = """
        SELECT ?s ?p ?o
        WHERE {
            ?s ?p ?o .
        }
    """

    results = graph_db.query(query)

    # Print the query results
    print(f"\n\nquery: results={len(results)}")
    for row in results:
        # print(row)å
        pass