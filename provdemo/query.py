from provdemo.db import GraphDB


def query_all():
    query_str = """
        SELECT ?subject ?predicate ?object
        WHERE {
        ?subject ?predicate ?object
        }
    """
    _query(query_str)

def query_input_data():
    print("\nquery: input data")
    query_str = """
        SELECT ?label
        WHERE {
            ?data rdf:type provone:Data ;
                rdfs:label ?label .
            FILTER (!strends(lcase(?label), "_infilled.nc"))
        }
    """
    _query(query_str)

def query_execution():
    print("\nquery: execution")
    query_str = """
        SELECT ?start ?end
        WHERE {
            ?exec rdf:type provone:Execution ;
                prov:startedAtTime ?start ;
                prov:endedAtTime ?end .
        }
    """
    _query(query_str)

def _query(query_str):
    graph_db = GraphDB()
    results = graph_db.query(query_str)

    # Print the query results
    print(f"query: results={len(results)}")
    for row in results:
        print(row)