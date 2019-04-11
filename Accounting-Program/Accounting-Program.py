import os

# Add a product information to the list.
def AddProduct(products, name, price):
    p = []
    p.append(name)
    p.append(price)
    products.append(p)
    return products

# Read csv.
def Read_csv():
    with open('products.csv', 'r', encoding='utf-8') as csv:
        for line in csv:
            products.append(line.strip().split(','))

# Write all products information in products.csv.
def Write_csv(products):
    with open('products.csv', 'w', encoding='utf-8') as csv:
        if products[0] != ['Name', 'Price']:
            csv.write('Name,Price\n')
        for p in products:
            csv.write(p[0] + ',' + p[1] + '\n')

# Main program of accounting.
if __name__ == '__main__':
    if os.path.isfile('products.csv') == False:
        new = [['Name', 'Price\n']]
        Write_csv(new)
    products = []
    Read_csv()
    print(products)
    while True:
        name = input('Please input the name of product(q = quit):')
        if name == 'q':
            break
        else:
            price = input('Please input the price of product:')
            AddProduct(products, name, price)
        Write_csv(products)

