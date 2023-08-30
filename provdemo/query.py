from provdemo.db import GraphDB


def query_all():
    query_str = """
        SELECT ?subject ?predicate ?object
        WHERE {
        ?subject ?predicate ?object
        }
    """
    _query(query_str)

def _query(query_str):
    graph_db = GraphDB()
    results = graph_db.query(query_str)

    # Print the query results
    print(f"\n\nquery: results={len(results)}")
    for row in results:
        # print(row)
        pass