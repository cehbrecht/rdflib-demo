from provdemo.provenance import Provenance
from provdemo import query
from provdemo import report
from datetime import datetime

def cli():
    print("build prov")
    prov = build()

    # store in db and file
    print("store prov")
    prov.store_rdf()
    prov.write_rdf()

    # query
    print("query prov")
    df = query.query()
    print(df)

    # report
    print("report prov")
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
            "min": 10,
            "max": 20,
            "stddev": 2,
        }, 
        ["http://example.org/input/HadCRUT.5.0.1.0.anomalies.ensemble_mean.nc"], 
        ["http://example.org/output/HadCRUT.5.0.1.0.anomalies.ensemble_mean_infilled.nc"],
        start_time,
        end_time,
    )
    return prov

   


