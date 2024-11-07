import os, json

jsonfile = "combined.json"

if not os.path.exists(jsonfile):
    print(f"{jsonfile} does not exist")
    exit(0)

with open(jsonfile, 'r') as all_fails:
    combined = json.load(all_fails)
# test
# print(len(combined))

# for iri in combined
    # if it is from the people vocab, try and parse from creator using slug
        # if parseable, add this IRI as "use" in combined JSON
    # if from creator, try and parse from people using slug
        # if parseable, add this IRI as "use" in combined JSON