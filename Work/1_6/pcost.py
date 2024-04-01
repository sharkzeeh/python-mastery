# pcost.py

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename) as fh:
        for line in fh:
            items = line.split()
            try:
                n_shares = int(items[1])
                price = float(items[2])
            except ValueError as e:
                print("Couldn't parse:", line, end='')
                print('Reason:', e)
            total_cost += n_shares * price
    return total_cost


if __name__ == '__main__':
    print(portfolio_cost('../Data/portfolio3.dat'))
    print(portfolio_cost('../Data/portfolio2.dat'))

