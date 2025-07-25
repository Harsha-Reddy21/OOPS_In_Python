class Product:
    _total_products=0
    _actual_products=[]
    def __init__(self,product_id,name,price,category,stock):
        self.product_id=product_id
        self.name=name
        self.price=price
        self.category=category
        self.stock=stock
        Product._total_products+=1
        Product._actual_products.append(self)
    def get_product_info(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Category: {self.category}, Stock: {self.stock}"
    @classmethod
    def get_total_products(cls):
        return cls._total_products
    def update_stock(self,quantity):
        self.stock+=quantity
    @classmethod
    def get_popular_category(cls):
        if not cls._actual_products:
            return "No products available"
        return max(cls._actual_products,key=lambda x:x.stock).category
    


laptop=Product("P001"," Gaming Laptop",1299.99, "Electronics", 10)
book=Product("P002","Python Programming",39.99, "Books", 25)
shirt=Product("P003","CottonT-shirt",19.99, "Clothing", 50)


print(f"Product info:{laptop.get_product_info()}")
print(f"Total Products in system: {Product.get_total_products()}")


class Customer:
    def __init__(self,customer_id,name,email,discount_rate=10):
        self.customer_id=customer_id
        self.name=name
        self.email=email
        self.discount_rate=discount_rate
        self.purchase_history = []  
    
    def get_discount_rate(self):
        return self.discount_rate
    
    def get_total_revenue(self):
        """Calculate total revenue from all purchases made by this customer"""
        return sum(order['total'] for order in self.purchase_history)
    
    def add_purchase(self, order_total):
        """Add a purchase to customer's history"""
        self.purchase_history.append({
            'total': order_total,
            'timestamp': datetime.now()  
        })
    
class ShoppingCart:     
    def __init__(self,customer):
        self.customer=customer
        self.items=[]

    def add_item(self,product,quantity):
  
        for i, (existing_product, existing_quantity) in enumerate(self.items):
            if existing_product.product_id == product.product_id:
                self.items[i] = (existing_product, existing_quantity + quantity)
                return

        self.items.append((product,quantity))
    
    def remove_item(self, product_id):
        """Remove an item from the cart by product ID"""
        self.items = [(product, quantity) for product, quantity in self.items 
                     if product.product_id != product_id]
    
    def clear_cart(self):
        """Remove all items from the cart"""
        self.items = []
    
    def get_cart_items(self):
        """Get a list of all items in the cart with their details"""
        return [(item[0].name, item[1]) for item in self.items]
    
    def get_total_items(self):
        return sum(item[1] for item in self.items)
    
    def get_subtotal(self):
        return sum(item[0].price*item[1] for item in self.items)
    
    def calculate_total(self):
        subtotal=self.get_subtotal()
        discount=subtotal*(self.customer.discount_rate/100)
        return subtotal-discount
    
    def place_order(self):
     
        if not self.items:
            return "Cart is empty. Cannot place order."
        
       
        for product, quantity in self.items:
            if product.stock < quantity:
                return f"Insufficient stock for {product.name}. Available: {product.stock}, Requested: {quantity}"
        

        total = self.calculate_total()
        for item in self.items:
            item[0].update_stock(-item[1])
        
       
        self.customer.add_purchase(total)
        

        order_items = self.get_cart_items().copy()
        self.clear_cart()
        
        return f"Order placed successfully. Items ordered: {order_items}"

   
customer=Customer("C001","John Doe","john.doe@example.com",20)
cart=ShoppingCart(customer) 

print(f"Customer: {customer.name}")
print(f"Customer discount: {customer.get_discount_rate()}%")


cart.add_item(laptop,2)
cart.add_item(book,2)
cart.add_item(shirt,3)


print(f"Cart total items: {cart.get_total_items()}")
print(f"Cart subtotal: ${cart.get_subtotal():.2f}")


final_total=cart.calculate_total()
print(f"Final total (with {customer.get_discount_rate()}% discount): ${final_total:.2f}")



print(f"Laptop stock before order: {laptop.stock}")
order_result=cart.place_order()
print(f"Order result: {order_result}")
print(f"Laptop stock after order: {laptop.stock}")


popular_category=Product.get_popular_category()
print(f"Popular category: {popular_category}")


# Fixed: Now calling get_total_revenue() on customer instance, not class
total_revenue=customer.get_total_revenue()
print(f"Total revenue from {customer.name}: ${total_revenue:.2f}")

# Create a new cart for demonstration of remove and clear methods
new_cart = ShoppingCart(customer)
new_cart.add_item(laptop, 1)
new_cart.add_item(book, 1)
print(f"New cart items: {new_cart.get_cart_items()}")

new_cart.remove_item("P002")
print(f"Cart items after removing P002: {new_cart.get_cart_items()}")

new_cart.clear_cart()
print(f"Cart items after clearing: {new_cart.get_cart_items()}")






