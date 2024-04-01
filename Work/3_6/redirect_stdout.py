# redirect_stdout.py

# (c) A Context Manager
# This context manager works by making
# a temporary patch to sys.stdout to cause
# all output to redirect to a different file.
# On exit, the patch is reverted.

import sys

class redirect_stdout:
    def __init__(self, out_file):
        # type(out_file) == <class '_io.TextIOWrapper'>
        self.out_file = out_file

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file

    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout


if __name__ == '__main__':
    import stock, reader, tableformat
    portfolio = reader.read_csv_as_instances('../Data/portfolio.csv', stock.Stock)
    formatter = tableformat.create_formatter('txt')
    with redirect_stdout(open('out.txt', 'w')) as file:
        tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
        file.close()
