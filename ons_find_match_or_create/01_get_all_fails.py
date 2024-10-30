import rdflib, json
from sys import argv

for dump in argv[1:]:
    coll_id = dump.split('.')[0]
    coll_all_distinct = []
    # CAUTION two options for local path to RDF dumps
    g = rdflib.Graph().parse(f"../../../Dropbox/od2colls/{dump}") # home computer
    # g = rdflib.Graph().parse(f"../../data_scratch/colls/{dump}") # work computer
    result = g.query(
        """SELECT DISTINCT ?ons_resource
        WHERE { ?s ?p ?ons_resource .
        FILTER CONTAINS (str(?ons_resource), "http://opaquenamespace.org/ns/") }""")
    for row in result:
        coll_all_distinct.append(str(row.ons_resource))
    
    coll_failures = []
    for iri in coll_all_distinct:
        try:
            g = rdflib.Graph().parse(f"{iri}.nt")
        except:
            coll_failures.append(iri)
    with open(f"coll_fails/{coll_id}_fails.json", 'w+') as jsonfile:
        json.dump({coll_id: coll_failures}, jsonfile)
