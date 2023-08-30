from provdemo.provenance import Provenance
from provdemo import query

def cli():
    prov = build()

    # store in db and file
    prov.store_rdf()
    prov.write_rdf()

    # query
    # query.query_all()
    query.query_input_data()
    query.query_execution()

def build():
    prov = Provenance(".")
    prov.start(workflow=True)
    prov.add_operator(
        "crai", 
        {
            "dataset_name": "HadCRUT5",
            "variable_name": "tas_mean",
        }, 
        ["HadCRUT.5.0.1.0.anomalies.ensemble_mean.nc"], 
        ["HadCRUT.5.0.1.0.anomalies.ensemble_mean_infilled.nc"]
    )
    import time
    time.sleep(2)
    prov.stop()
    return prov

   


