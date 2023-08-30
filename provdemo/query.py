from provdemo.db import GraphDB


def query_all():
    graph_db = GraphDB()
   
    query_str = """
        SELECT ?subject ?predicate ?object
        WHERE {
        ?subject ?predicate ?object
        }
    """
    results = graph_db.query(query_str)

    # Print the query results
    print(f"\n\nquery: results={len(results)}")
    for row in results:
        # print(row)å
        pass