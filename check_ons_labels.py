import rdflib

# get all ONS.org values
all_distinct_ons = []
g = rdflib.Graph().parse("../data_scratch/colls/building-or.ttl")
result = g.query(
    """
    SELECT DISTINCT ?ons_resource
    WHERE {
        ?s ?p ?ons_resource .
        FILTER CONTAINS (str(?ons_resource), "http://opaquenamespace.org/ns/")
        FILTER NOT EXISTS { ?s <info:fedora/fedora-system:def/model#hasModel> 'Generic' . }
    }
    """
)
counter = 0
for row in result:
    counter += 1
    # print(row.ons_resource)
    all_distinct_ons.append(str(row.ons_resource))
print(f"{counter} distinct ONS values found")

# iterate through these to see which fail when attempting to retrieve label
    # this is going to take forever... other way to access RDF besides g.parse("rdfurl.nt")?
failures = []
for iri in all_distinct_ons:
    try:
        g = rdflib.Graph().parse(f"{iri}.nt")
    except:
        failures.append(iri)
print(f"Cannot retrieve a label for {len(failures)} ONS resources")

# compile list of failures
with open("/mnt/c/Users/briesenb/Desktop/ons_failures.txt", "w+") as txtfile:
    for iri in failures:
        txtfile.write(f"{iri}\n")
print("See Desktop file 'ons_failures.txt' for IRIs where no label could be retrieved")