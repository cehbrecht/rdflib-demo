from rdflib import Graph, Literal, Namespace, RDF, URIRef
from rdflib_sqlalchemy import registerplugins
from rdflib_sqlalchemy.store import SQLAlchemy
from PIL import Image
import base64
from sqlalchemy import create_engine
import io

# Create an RDF graph
graph = Graph()

# Define namespaces
ex = Namespace("http://example.org/")
prov = Namespace("http://www.w3.org/ns/prov#")

# Load an image
image_path = "path_to_your_image.jpg"
with open(image_path, "rb") as image_file:
    image_data = image_file.read()
    encoded_image = base64.b64encode(image_data).decode("utf-8")

# Add image information to the graph
image_resource = ex.ImageResource
graph.add((image_resource, RDF.type, ex.Image))
graph.add((image_resource, ex.hasImageData, Literal(encoded_image)))

# Create a SQLAlchemy-backed store and bind it to the graph
engine = create_engine("sqlite:///image_data.db")
store = SQLAlchemy(identifier=ex, engine=engine)
registerplugins(store, False)
graph.open(store, create=True)

# ... (previous code)

# Query and retrieve the image data
query = f"""
    SELECT ?imageData
    WHERE {{
        ?image rdf:type ex:Image ;
               ex:hasImageData ?imageData .
    }}
"""
results = graph.query(query, initNs={"rdf": RDF, "ex": ex})

# Prepare a list to store image data for the HTML report
image_data_list = []

# Retrieve and store image data for each image
for row in results:
    encoded_image = row.imageData.value
    image_data_list.append(encoded_image)

# Convert the image data to HTML <img> tags
html_images = []
for encoded_image in image_data_list:
    img_tag = f'<img src="data:image/jpeg;base64,{encoded_image}" alt="Image" style="max-width: 300px;">'
    html_images.append(img_tag)

# Convert the DataFrame to an HTML table
html_table = df.to_html(index=False)

# Define the HTML template
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Provenance Report</title>
    <style>
        /* ... (previous styles) */
    </style>
</head>
<body>
    <h1>Provenance Report</h1>
    {html_table}
    <h2>Images</h2>
    {''.join(html_images)}
</body>
</html>
"""

# Write the HTML template to a file
with open("provenance_report_with_images.html", "w") as file:
    file.write(html_template)
