from rdflib import Graph

# ! to do: Get OD ID for properties - this is what staff will see on spreadsheet
descriptive_props = [
    "http://purl.org/dc/terms/title",
    "http://opaquenamespace.org/ns/vra_measurements",
    "http://id.loc.gov/vocabulary/relators/rps"
]

nosatsu = Graph().parse("../data_scratch/colls/nosatsu.jsonld")

with open("/mnt/c/Users/briesenb/Desktop/nosatsu_report.md", "w+") as mkdown:
    mkdown.write("# Nosatsu metadata overview\n")
    mkdown.write("## Descriptive properties\n")

    for property in descriptive_props:
        toc_entry = f"- {property.split('/')[-1]}: [for items](#{property.split('/')[-1]}---for-items) / [for complex objects](#{property.split('/')[-1]}---for-complex-objects)\n"
        mkdown.write(toc_entry)

    # I think double-curlies would work as well
    item_q = """
    SELECT ?value 
    WHERE {
        ?item <property_here> ?value .
        FILTER NOT EXISTS { ?item <info:fedora/fedora-system:def/model#hasModel> 'Generic'  . }
    }
    """
    # ! results are only for the first property in descriptive_props
    # ! whhhhyyyyyy
    mkdown.write("## Values by property - items\n")
    for property in descriptive_props:
        mkdown.write(f"### {property.split('/')[-1]} - for items\n")
        item_q = item_q.replace("property_here", property)
        result = nosatsu.query(item_q)
        for row in result:
            mkdown.write(f"- {row.value}\n")
        mkdown.write("\n")
        mkdown.write("***back to [top](#nosatsu-metadata-overview)***\n")
