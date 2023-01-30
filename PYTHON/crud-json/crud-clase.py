import json

class CRUD:
    def __init__(self, filename):
        self.filename = filename

    def create(self, data):
        try:
            with open(self.filename, 'r') as f:
                records = json.load(f)
        except:
            records = []

        records.append(data)

        with open(self.filename, 'w') as f:
            json.dump(records, f)

    def read(self):
        try:
            with open(self.filename, 'r') as f:
                records = json.load(f)
            return records
        except:
            return []

    def update(self, id, data):
        with open(self.filename, 'r') as f:
            records = json.load(f)

        for record in records:
            if record['id'] == id:
                record.update(data)
                break

        with open(self.filename, 'w') as f:
            json.dump(records, f)

    def delete(self, id):
        with open(self.filename, 'r') as f:
            records = json.load(f)

        records = [record for record in records if record['id'] != id]

        with open(self.filename, 'w') as f:
            json.dump(records, f)