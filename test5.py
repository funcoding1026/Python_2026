
def create_shopping_list(store_name, *args):
    # store_name is a normal argument, *args grabs everything else
    print(f"--- Shopping List for {store_name} ---")
    for item in args:
        print(f"- {item}")

# Example usage:
create_shopping_list("Walmart", "Milk", "Eggs", "Bread","Bread")

def clean_user_list(*args):
    valid_users=[]
    for names in args:
       cleaned= names.strip().title()
       if cleaned:
           valid_users.append(cleaned)


# 1. Define the blueprint (Class)
class ShoppingCart:
    def __init__(self):
        # Every new cart starts with an empty list inside it
        self.items = []
        
    # 2. This is your User-Defined Method!
    def add_item(self, item_name):
        self.items.append(item_name)
        print(f"Added {item_name} to your custom cart!")

# --- How to use it ---

# Create a brand new cart object
my_cart = ShoppingCart()

# Call your user-defined method using the dot (.) syntax
my_cart.add_item("Laptop")  # Output: Added Laptop to your custom cart!
my_cart.add_item("Mouse")   # Output: Added Mouse to your custom cart!

# Check what's inside
print(my_cart.items)        # Output: ['Laptop', 'Mouse']'''

class ShoppingCart:
    def __init__(self, owner_name):
        self.owner = owner_name  # Stores the owner name on 'self'
        self.items = []          # Stores an empty list on 'self'
        
    def add_item(self, item_name):
        # 'self' makes sure the item goes into the correct cart!
        self.items.append(item_name)
        print(f"Added {item_name} to {self.owner}'s cart.")

# --- Creating two completely separate objects ---
alice_cart = ShoppingCart("Alice")
bob_cart   = ShoppingCart("Bob")

alice_cart.add_item("Laptop")    # ShoppingCart.add_item(alice_cart, "Laptop")
bob_cart.add_item("Laptop2")

print(alice_cart.items) # Output: ['Laptop']
print(bob_cart.items)   # Output: [] (Bob's cart was not touched!)








        