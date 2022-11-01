from abc import ABC, abstractmethod
from ast import Pass

class Product:
    product_size = 0
    product_color = ""
    product_expiry_date = 0
    
 
class ProductAbstract(ABC):

    @abstractmethod
    def create_product(self, product:Product):
        pass

    @abstractmethod
    def edit_product(self):
        pass

    @abstractmethod
    def get_product_by_id(self):
        pass

    @abstractmethod 
    def get_all_products(self):
        pass

    @abstractmethod
    def upload_product_image(self):
        pass

    @abstractmethod 
    def delete_product(self):

        from productabstract import productabstract

class productmanager(ProductAbstract): 
       
    def create_product(self, product:Product):
        print("creating product")
        print(f"product size is {product.product_size}")

    def edit_product(self):
        print("make changes to product")     

    def get_product_by_id(self):
         print ("insert product ID") 

    def get_all_products(self):
        print ("show all my products")   

    def upload_product_image(self, image):
        print("upload product image")

    def delete_product(self):
        print ("delete this product")

product = Product()
product.product_size = 6

bottle = productmanager()
bottle.create_product(product=product)






