from provdemo.db import GraphDB
from provdemo.provenance import Provenance

def cli():
    # collect provenvance
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

    # write to store
    graph_db = GraphDB()
    graph_db.add(prov.get_rdf())

    # query store
    graph_db.query()

    # write 
    prov.write_rdf()


