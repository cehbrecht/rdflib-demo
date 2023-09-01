from provdemo.provenance import Provenance
from provdemo import query
from provdemo import report

def cli():
    prov = build()

    # store in db and file
    prov.store_rdf()
    prov.write_rdf()

    # query
    # query.query_all()
    # query.query_input_data()
    # query.query_output_data()
    # query.query_execution_time()
    # query.query_execution_jobs()
    df = query.query_with_pandas()
    report.write_html(df)

def build():
    prov = Provenance(".")
    prov.start()
    prov.add_operator(
        "crai", 
        {
            "dataset_name": "HadCRUT5",
            "variable_name": "tas_mean",
        }, 
        ["HadCRUT.5.0.1.0.anomalies.ensemble_mean.nc"], 
        ["HadCRUT.5.0.1.0.anomalies.ensemble_mean_infilled.nc"]
    )
    return prov

   


