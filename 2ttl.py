from rdflib import Graph
from rdflib.namespace import Namespace
from os import system
from sys import argv

# add namespaces
# preferred / common prefixes from ontology, at prefix.cc
# ! make creating namespaces, binding namespaces better
# ! does bind step below need to happen when initializing each graph, or only once total?
# ! many more namespaces still to-do, see JSON-LD for some additional prefix suggestions
LINKREL = Namespace("http://www.iana.org/assignments/relation/")
EBUCORE = Namespace("http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#")
EDM = Namespace("http://www.europeana.eu/schemas/edm/")
ORE = Namespace("http://www.openarchives.org/ore/terms/")
LDP = Namespace("http://www.w3.org/ns/ldp#")
ACL = Namespace("http://www.w3.org/ns/auth/acl#")
PCDM = Namespace("http://pcdm.org/models#")
MARCREL = Namespace("http://id.loc.gov/vocabulary/relators/")

# couldn't identify preferred prefix
ONS = Namespace("http://opaquenamespace.org/ns/")
FEDREP = Namespace("http://fedora.info/definitions/v4/repository#")
RESTAT = Namespace("http://fedora.info/definitions/1/0/access/ObjState#")
FEDORA = Namespace("info:fedora/fedora-system:def/model#")

target = input("enter target dir in data_scratch, if applicable\n>>> ")

# ! improve - what if user doesn't enter file name after script name?
for resource in argv[1:]:
    # bind namespaces to prefixes for readability
    g = Graph()
    g.bind("linkrel", "http://www.iana.org/assignments/relation/")
    g.bind("ebucore", "http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#")
    g.bind("edm", "http://www.europeana.eu/schemas/edm/")
    g.bind("ore", "http://www.openarchives.org/ore/terms/")
    g.bind("ldp", "http://www.w3.org/ns/ldp#")
    g.bind("acl", "http://www.w3.org/ns/auth/acl#")
    g.bind("pcdm", "http://pcdm.org/models#")
    g.bind("marcrel", "http://id.loc.gov/vocabulary/relators/")
    g.bind("ons", "http://opaquenamespace.org/ns/")
    g.bind("fedrep", "http://fedora.info/definitions/v4/repository#")
    g.bind("restat", "http://fedora.info/definitions/1/0/access/ObjState#")
    g.bind("fedora", "info:fedora/fedora-system:def/model#")

    g.parse(f"/mnt/c/Users/briesenb/Desktop/{resource}") # I believe this is an absolute path
    if target != '':
        g.serialize(f"/home/brieswsl/data_scratch/{target}/{resource.split('.')[0]}.ttl", format = "turtle") # I believe this is an absolute path
    else:
        g.serialize(f"/home/brieswsl/data_scratch/{resource.split('.')[0]}.ttl", format = "turtle")
    # and I believe that the absolute paths are working well for me here
    system(f"rm /mnt/c/Users/briesenb/Desktop/{resource}") # cleanup desktop

if target != '':
    print(f"Your turtle is in ~/data_scratch/{target}/")
else:
    print("your turtle is in ~/data_scratch")