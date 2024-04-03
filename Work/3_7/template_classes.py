# Classes as a Template

# A class might implement a general-
#   purpose algorithm, but delegate certain 
#   steps to a subclass
# Will illustrate with a simple example

import csv

class CSVParser:
    def parse(self, filename):
        records = []
        with open(filename) as f: 
             rows = csv.reader(f)
             self.headers = next(rows)
             for row in rows:
                # custom implementation
                record = self.make_record(row)
                records.append(record)
        return records

    # Step that must be impletented
    # Note: Class is useless by itself
    def make_record(self, row):
        raise RuntimeError('Must Implement')

class DictCSVParser(CSVParser):
    def make_record(self, row):
        return dict(zip(self.headers, row))


if __name__ == '__main__':
    parser = DictCSVParser()
    portfolio = parser.parse('../Data/portfolio.csv')

# Using the template (use inheritance)
# Critical idea: User defines a small class that 
# supplies the one missing piece, but most of 
# the real functionality is in the base class