import rdflib, json
from sys import argv

# WOULD BE FASTER
    # to add fails to combined list at this point:
    # for each ONS IRI:
        # check if in combined list
            # if yes, no need to try and parse!
            # just add coll id to combined list data
            # if no, try and parse to see if it fails

for dump in argv[1:]:
    coll_id = dump.split('.')[0]
    coll_all_distinct = []
    # CAUTION two options for local path to RDF dumps
    # g = rdflib.Graph().parse(f"../../../Dropbox/od2colls/{dump}") # home computer
    g = rdflib.Graph().parse(f"../../data_scratch/od2colls/{dump}") # work computer
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
    with open(f"coll_fails/{coll_id}.json", 'w+') as jsonfile:
        json.dump({coll_id: coll_failures}, jsonfile)
