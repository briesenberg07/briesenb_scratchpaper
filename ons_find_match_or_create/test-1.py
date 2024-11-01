good_structure = {
        "http://failed_iri_01": {
            "collection": "blimps",
            "use_instead": "http://good_iri_01"
        },
        "http://failed_iri_02": {
            "collection": "ships",
            "use_instead": "http://good_iri_02"
        }
    }

# dictionary.get('key') = dictionary['key']
# .get throws and error
# just using the dictionary key and missing doesn't
