import json, os, csv

if os.path.exists("combined.json"):
    with open("combined.json", "r") as existingjson:
        combined = json.load(existingjson)
else:
    combined = {}

# test
# print(f"len(combined): {len(combined)}")

coll_data = os.listdir("coll_fails")
for coll in coll_data:
    coll_id = coll.split('.')[0]
    with open(f"coll_fails/{coll}", "r") as coll_json:
        coll_fails = json.load(coll_json)
        coll_fails = coll_fails[coll_id]
    # test
    # print(f"{len(coll_fails)} failed IRIs in {coll_id}")
    for iri in coll_fails:
        if combined.get(iri) == None:
            combined.update({ iri: {
                "coll": [coll_id],
                "use": None
            }})
        elif combined.get(iri) != None and coll_id not in combined[iri]['coll']:
            combined[iri]['coll'].append(coll_id)
        elif combined.get(iri) != None and coll_id in combined[iri]['coll']:
            pass
        else:
            print("ERROR IN COLL_FAILS FOR LOOP")

# test
# print(f"len(combined): {len(combined)}")

with open("combined.json", "w+") as newjsonfile:
    json.dump(combined, newjsonfile)

with open("combined.csv", "w+") as newcsvfile:
    fieldnames = ['fail', 'coll', 'use']
    writer = csv.DictWriter(newcsvfile, fieldnames=fieldnames)
    writer.writeheader()
    with open("combined.json", "r") as jsonfile:
        combined = json.load(jsonfile)
    for iri in combined: # this syntax ...
        writer.writerow({
            'fail': iri, # ...was a little tricky ...
            'use': combined[iri]['use'], # ...I guess I'm still learning...
            'coll': ', '.join(combined[iri]['coll']) # ...data structures...
            })
