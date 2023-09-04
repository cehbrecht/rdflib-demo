from provdemo.provenance import Provenance
from provdemo import query
from provdemo import report
from datetime import datetime

def cli():
    prov = build()

    # store in db and file
    prov.store_rdf()
    prov.write_rdf()

    # query
    df = query.query_with_pandas()
    report.write_html(df)

def build():
    start_time = datetime.now().isoformat(timespec="seconds")
    end_time = start_time

    prov = Provenance(".")
    prov.add_operator(
        "crai", 
        {
            "dataset_name": "HadCRUT5",
            "variable_name": "tas_mean",
        }, 
        ["HadCRUT.5.0.1.0.anomalies.ensemble_mean.nc"], 
        ["HadCRUT.5.0.1.0.anomalies.ensemble_mean_infilled.nc"],
        start_time,
        end_time
    )
    return prov

   


