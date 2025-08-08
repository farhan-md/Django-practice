# Management of store products

products = []

def price_is_valid(func):
    def wrapper(name,price):
        if price <= 0:
            raise ValueError("Price cannot be less than 0")
        else:
            return func(name,price)
    return wrapper

@price_is_valid
def add_product(name,price):
    return products.append((name,price))

def list_product():
    # returning all of products as a list
    list(map(lambda x : print(f"name: {x[0]} , price: {x[1]}"),products))

def filter_by_price(min_price):

    return list(filter(lambda x: x[1] >= min_price,products))

def sort_products_by_price():
    # define price as a key
    res =  sorted(products,key = lambda x : x[1])
    # navigating and printing sorted list elements
    list(map(lambda x: print(f"name: {x[0]} , price: {x[1]}"),res))

add_product("water",15)
add_product("fruit",12)
add_product("laptop",200)

list_product()
sort_products_by_price()

print(filter_by_price(15))