# tableformat.py

# (c) Table Output
def print_table(records, fields):
    # header
    headers = ' '.join(['%10s'] * len(fields))
    print(headers % (*fields, ))
    print(' '.join(['-' * 10] * len(fields)))
    # print(' '.join('%10s' % name for name in fields))
    # print(('-' * 10 + ' ') * len(fields))

    # table rows
    for record in records:
        print(' '.join('%10s' % getattr(record, name) for name in fields))


if __name__ == '__main__':
    import stock
    portfolio = stock.read_portfolio('../Data/portfolio.csv')
    print_table(portfolio, ['name','shares'])
