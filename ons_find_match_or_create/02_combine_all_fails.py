import json, os, csv

with open("_combined_distinct_fails.json", "r") as existingjson:
    all_fails = json.load(existingjson)
    all_fails = all_fails["_combined_distinct_fails"]
# test
# print(f"len(all_fails) > {len(all_fails)}")

coll_data = os.listdir("coll_fails")
for coll in coll_data:
    with open(f"coll_fails/{coll}", "r") as coll_json:
        coll_fails = json.load(coll_json)
        coll_id = list(coll_fails.keys())[0]
        coll_fails = coll_fails[coll_id]

    # ... not 100% sure that this code is doing what I think it is doing
    for failed_iri in coll_fails:
        if not any(d['fail'] == failed_iri for d in all_fails):
            all_fails.append({
                'fail': failed_iri,
                'coll_s': [ coll_id ],
                'use': ''
            })
        elif any(d['fail'] == failed_iri for d in all_fails) and all_fails['fail' == value]['coll_s'] != coll_id:
            all_fails['fail' == failed_iri]['coll_s'].append(coll_id)
        else:
            pass

with open("_combined_distinct_fails.json", "w+") as newjsonfile:
    json.dump({"_combined_distinct_fails": all_fails}, newjsonfile)

with open("_combined_distinct_fails.csv", "w+") as newcsvfile:
    fieldnames = ['fail', 'coll_s', 'use']
    writer = csv.DictWriter(newcsvfile, fieldnames=fieldnames)
    writer.writeheader()
    for entry in all_fails:
        writer.writerow({
            'fail': entry['fail'], 
            'coll_s': ', '.join(entry['coll_s']), 
            'use': entry['use']
            })
