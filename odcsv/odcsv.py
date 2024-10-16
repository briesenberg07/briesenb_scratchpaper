import csv
from colls import colls

class OdCsv:
    def __init__(self, filepath, coll):
        self = self
        self.filepath = filepath
        self.coll = coll
    
    # trash this test method later?
    def print_file_id(self):
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(f"<< file: {row['file']} >> << identifier: {row['identifier']} >>")

    def fix_filenames(self):
        with open(self.filepath, newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            headers = reader.fieldnames
            with open(f"new_{self.filepath.split('/')[1]}", "w+") as outfile:
                writer = csv.DictWriter(outfile, fieldnames=headers)
                writer.writeheader()
                for row in reader:
                    newrow = {}
                    for header in headers:
                        if header == 'file':
                            newrow.update({header: row[header]})
                            # replace ^^^ with fixing filename, use colls data > collno
                        elif header == 'identifier':
                            newrow.update({header: row[header]})
                            # replace ^^^ with fixing identifier, use colls data > collno
                        else:
                            newrow.update({header: row[header]})
                    writer.writerow(newrow)


""" TO-DOS, IDEAS

to dos
    eliminate spaces from values in columns taking IRIs
    replace old file with new
    ...

ideas 
    validate column headers
        this could involve adding list of headers to colls data
    check encoding or otherwise avoid blorked-up item titles
    for rows with no filename, delete values
    summarize changes when replacing old file with new?
    ...

"""