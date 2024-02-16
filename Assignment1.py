import time
import sys

class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product: {self.id} {self.name} {self.price} {self.category}"

    def __repr__(self):
        return f"Product({self.id}, {self.name}, {self.price}, {self.category})"

def BubbleSortByPrice(products):#sort by price
    n = len(products)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1): 
            if products[j].price > products[j+1].price:
                products[j], products[j+1] = products[j+1], products[j]
                swapped = True
        if not swapped:
            break
def FindProduct(products, to_find):
    for product in products:
        if isinstance(to_find, float) and product.price == to_find:
            return product
        elif isinstance(to_find, int) or isinstance(to_find, str):
            if str(product.id) == str(to_find) or product.name == to_find or product.category == to_find:
                return product
    return None
def UpdateProduct(products, _productIdToUpdate, _newName, _newPrice, _newCategory):
    for product in products:
        if product.id == _productIdToUpdate:
            product.name = _newName
            product.price = _newPrice
            product.category = _newCategory
            print(f"Successfully updated product: {product}")
            return product
    return None

def DeleteProduct(products, _productIdToDelete):
    for product in products:
        if product.id == _productIdToDelete:
            print(f"Successfully deleted product: {product}")
            products.remove(product)
            return product
    return None

def AddProduct(products, _productId, _productName, _productPrice, _productCategory):
    if(FindProduct(products, _productId)!=None):
        print(f"Product with id {_productId} already exists.")
        return None
    newProduct = Product(_productId, _productName, _productPrice, _productCategory)
    products.append(newProduct)
    print(f"Successfully added product: {newProduct}")
    return newProduct

def ComplexityAnalisys(products):
    start = time.time()
    BubbleSortByPrice(products)
    end = time.time()
    space_complexity = sys.getsizeof(products) + sys.getsizeof(start) + sys.getsizeof(end) + 64
    print(f"Time taken: {end - start:.6f} seconds, Space used: {space_complexity} bytes")
    return None


file_path = 'product_data.txt'

products = []

try:
    with open(file_path, 'r') as file:
        data = file.read()

        for line in data.split('\n'):
            attributes = line.split(',')
            attributes = [attr.strip() for attr in attributes]
            
            if(len(attributes) == 4):
                tempProduct = Product(attributes[0], attributes[1], float(attributes[2]), attributes[3])
                products.append(tempProduct)     
except FileNotFoundError:
    print(f"File '{file_path}' not found.")

productsAverageCase = products.copy()
print("Average Case:")
ComplexityAnalisys(productsAverageCase)
for product in productsAverageCase:
    print(product)
productsBestCase = productsAverageCase.copy()
print("Best Case:")
ComplexityAnalisys(productsBestCase)
productsWorstCase = productsBestCase[::-1]
print("Worse Case:")
ComplexityAnalisys(productsWorstCase)

print(FindProduct(products, 211.57))

AddProduct(products, "44574234", "temp", 14.234, "_productCategory")
for product in products:
    print(product)
print("---------------------")

UpdateProduct(products, "44574234", "changedItem", 5000, "new category")
for product in products:
    print(product)
print("---------------------")
DeleteProduct(products, "44574234")
for product in products:
    print(product)
print("---------------------")