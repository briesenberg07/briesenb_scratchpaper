
# get all ONS.org values
# Enter RDF dumps with file extension following `python3 1_getfails.py`
# Must be in data_scratch/colls/

import rdflib
import json
from sys import argv

# to-dos
    # !! speed this up !! see below
        # sort by vocab and only parse each vocab once for that group???
        # report on time taken?

combined_failures = []
colls_given = []
for dump in argv[1:]:
    colls_given.append(dump)

for dump in argv[1:]:
    all_distinct_ons = []
    # CAUTION local path to RDF dumps here
    g = rdflib.Graph().parse(f"../../data_scratch/colls/{dump}")
    result = g.query(
        """
        SELECT DISTINCT ?ons_resource
        WHERE {
            ?s ?p ?ons_resource .
            FILTER CONTAINS (str(?ons_resource), "http://opaquenamespace.org/ns/")
            }
        """)
    counter = 0
    for row in result:
        counter += 1
        # print(row.ons_resource)
        all_distinct_ons.append(str(row.ons_resource))
    print(f"{counter} distinct ONS values found in {dump}")
    # this is the part that I'd think needs to be sped up
    # by for example, parsing each ONS vocab only once for terms from that vocab
    failures = []
    for iri in all_distinct_ons:
        try:
            g = rdflib.Graph().parse(f"{iri}.nt")
        except:
            failures.append(iri)
    print(f"Cannot retrieve a label for {len(failures)} ONS resources in {dump}")
    coll_alias = dump.split('.')[0]
    with open(f"ref_results/{coll_alias}_failures.json", 'w+') as jsonfile:
        json.dump({f"{coll_alias}_failures": failures}, jsonfile)

print("creating combined failed IRI list")
for dump in colls_given:
    coll = dump.split('.')[0]
    with open(f"ref_results/{coll}_failures.json", "r") as jsonfile:
        faildict = json.load(jsonfile)
        faillist = faildict[f"{coll}_failures"]
        print(f"{len(faillist)} failed ONS IRIs in collection {coll}\n")
    for item in faillist:
        if item not in combined_failures:
            combined_failures.append(item)
        else:
            pass
print(f"TOTAL {len(combined_failures)} FAILURES")
# aaaaaa forgot to write this to a fiiiillllleeeee
