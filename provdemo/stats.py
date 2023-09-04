from prov.identifier import Namespace
from prov.model import ProvDocument
from datetime import datetime

# Create a new provenance document
doc = ProvDocument()

# Define namespaces
ex = Namespace("example_namespace", uri="http://example.org/stats")
doc.add_namespace(ex)

# Define attributes using namespaces
attr_data = ex["data"]
attr_value = ex["value"]
attr_statistic = ex["statistic"]

# Compute statistics
data_values = [10, 20, 30, 40, 50]
mean_val = sum(data_values) / len(data_values)
min_val = min(data_values)
max_val = max(data_values)

# Create entities for input data and statistics
input_data = doc.entity(ex["input_data"], {attr_data: str(data_values)})
mean_value = doc.entity(ex["mean_value"], {attr_value: mean_val, attr_statistic: "mean"})
min_value = doc.entity(ex["min_value"], {attr_value: min_val, attr_statistic: "min"})
max_value = doc.entity(ex["max_value"], {attr_value: max_val, attr_statistic: "max"})

# Define an agent
user = doc.agent(ex["user:example_user"], {ex["name"]: "John Doe"})

# Define activities
data_preparation = doc.activity(ex["data_preparation"], datetime.now())
compute_statistics = doc.activity(ex["compute_statistics"], datetime.now())

# Specify relationships
doc.wasAttributedTo(mean_value, user)
doc.wasAttributedTo(min_value, user)
doc.wasAttributedTo(max_value, user)

doc.wasGeneratedBy(mean_value, compute_statistics)
doc.wasGeneratedBy(min_value, compute_statistics)
doc.wasGeneratedBy(max_value, compute_statistics)

doc.wasAssociatedWith(data_preparation, user)
doc.wasAssociatedWith(compute_statistics, user)

doc.used(compute_statistics, input_data)



# Print the provenance document
print(doc.get_provn())
