total_cost = 0.0
with open('../Data/portfolio.dat') as fh:
    for line in fh:
        items = line.split()
        n_shares = int(items[1])
        price = float(items[2])
        total_cost += n_shares * price
    
print(total_cost)
