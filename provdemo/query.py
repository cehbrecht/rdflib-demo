from provdemo.db import GraphDB
import pandas as pd


def query_all():
    query_str = """
        SELECT ?subject ?predicate ?object
        WHERE {
        ?subject ?predicate ?object
        }
    """

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
