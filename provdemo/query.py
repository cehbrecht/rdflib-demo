from provdemo.db import GraphDB
import pandas as pd


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
        SELECT ?specificEntity
        WHERE {
        ?specificEntity rdf:type prov:Entity .
        
        ?entity rdf:type prov:Entity ;
                prov:qualifiedDerivation [ prov:entity ?specificEntity ] .
        }
    """
    _query(query_str)

def query_output_data():
    print("\nquery: output data")
    query_str = """
        SELECT ?entity
        WHERE {
        ?specificEntity rdf:type prov:Entity .
        
        ?entity rdf:type prov:Entity ;
                prov:qualifiedDerivation [ prov:entity ?specificEntity ] .
        }
    """
    _query(query_str)

def query_execution_time():
    print("\nquery: execution time")
    query_str = """
        SELECT ?start ?end
        WHERE {
            ?exec rdf:type provone:Execution ;
                prov:startedAtTime ?start ;
                prov:endedAtTime ?end .
        }
    """
    _query(query_str)

def query_execution_jobs():
    print("\nquery: execution jobs")
    query_str = """
        SELECT ?name ?dataset ?variable
        WHERE {
            ?exec rdf:type provone:Execution ;
                rdfs:label ?name ;
                clint:dataset_name ?dataset ;
                clint:variable_name ?variable .
        }
    """
    _query(query_str)

def query_with_pandas():
    query_str = """
        SELECT ?process ?dataset ?variable ?startTime ?endTime
        WHERE {
            ?exec rdf:type provone:Execution ;
                rdfs:label ?process ;
                clint:dataset_name ?dataset ;
                clint:variable_name ?variable ;
                prov:startedAtTime ?startTime ;
                prov:endedAtTime ?endTime .
        }
    """
    graph_db = GraphDB()
    results = graph_db.query(query_str)

    data = []
    for row in results:
        process = row.process.split("/")[-1]
        dataset = row.dataset.value
        variable = row.variable.value
        start_time = row.startTime.value
        end_time = row.endTime.value
        data.append({
            "Process": process, 
            "Dataset": dataset,
            "Variable": variable, 
            "Start Time": start_time, 
            "End Time": end_time}
        )

    df = pd.DataFrame(data)
    return df

def _query(query_str):
    graph_db = GraphDB()
    results = graph_db.query(query_str)

    # Print the query results
    print(f"query: results={len(results)}")
    for row in results:
        print(row)