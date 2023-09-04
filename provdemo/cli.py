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
        ["http://example.org/input/HadCRUT.5.0.1.0.anomalies.ensemble_mean.nc"], 
        ["http://example.org/output/HadCRUT.5.0.1.0.anomalies.ensemble_mean_infilled.nc"],
        start_time,
        end_time
    )
    prov.add_statistics(
        ["http://example.org/output/HadCRUT.5.0.1.0.anomalies.ensemble_mean_infilled.nc"], 
        10, 
        20, 
        2
    )
    return prov

   


