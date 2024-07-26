from rdflib import Graph
from datetime import datetime

# this creates a huge markdown document of questionable usefulness...


# ! to do: Get OD ID for properties - this is what staff will see on spreadsheet
descriptive_props = [
    "http://purl.org/dc/terms/title",
    "http://purl.org/dc/terms/alternative",
    "http://purl.org/dc/terms/description",
    "http://opaquenamespace.org/ns/vra_measurements"
    # ... 
]

nosatsu = Graph().parse("../data_scratch/colls/nosatsu.jsonld")

with open("/mnt/c/Users/briesenb/Desktop/nosatsu_report.md", "w+") as mkdown:
    mkdown.write("# Nosatsu metadata overview\n")
    mkdown.write(f"**Last updated {datetime.today().strftime('%Y-%m-%d')}**\n")
    mkdown.write("## Descriptive properties which expect a text value\n")
    mkdown.write("*Is this a complete list??*\n")

    for property in descriptive_props:
        toc_entry = f"- {property.split('/')[-1]}: [for items](#{property.split('/')[-1]}---for-items) / [for complex objects](#{property.split('/')[-1]}---for-complex-objects)\n"
        mkdown.write(toc_entry)

    # still to do -- *also* output values for complex objects, as indicated at doc top
    mkdown.write("## Values by property - items\n")
    for property in descriptive_props:
        mkdown.write(f"### {property.split('/')[-1]} - for items\n")
        item_q = f"""
        SELECT DISTINCT ?value 
        WHERE {{
            ?item <{property}> ?value .
            FILTER NOT EXISTS {{ ?item <info:fedora/fedora-system:def/model#hasModel> 'Generic'  . }}
        }}
        """
        result = nosatsu.query(item_q)
        for row in result:
            mkdown.write(f"- {row.value}\n")
        mkdown.write("\n")
        mkdown.write("***back to [top](#nosatsu-metadata-overview)***\n")
    
    mkdown.write("## Values by property - for complex objects\n")
    for property in descriptive_props:
        mkdown.write(f"### {property.split('/')[-1]} - for complex objects\n")
        item_q = f"""
        SELECT DISTINCT ?value 
        WHERE {{
            ?item <{property}> ?value .
            FILTER EXISTS {{ ?item <info:fedora/fedora-system:def/model#hasModel> 'Generic'  . }}
        }}
        """
        result = nosatsu.query(item_q)
        for row in result:
            mkdown.write(f"- {row.value}\n")
        mkdown.write("\n")
        mkdown.write("***back to [top](#nosatsu-metadata-overview)***\n")
