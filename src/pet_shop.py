# WRITE YOUR FUNCTIONS HERE
# This is a comment 
# pet_shop_name = str("Camelot of Pets")

# 1
def get_pet_shop_name(pet_shop):
        return pet_shop["name"]

# 2
def get_total_cash(pet_shop):
    # sum = get_total_cash
    return pet_shop["admin"]["total_cash"]
        
# 3, 4
def add_or_remove_cash(pet_shop, amount):
    total_amount= pet_shop["admin"]["total_cash"]
    new_amount = total_amount + amount
    pet_shop["admin"]["total_cash"] = new_amount 
# 5
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# 6
def increase_pets_sold(pet_shop, sold):
    pets_sold = pet_shop["admin"]["pets_sold"]
    increased_sales = pets_sold + sold
    pet_shop["admin"]["pets_sold"] = increased_sales
    return (increased_sales)

# 7
def get_stock_count(pet_shop):
    stock = len(pet_shop["pets"])
    return stock
    # or
    
# def get_stock_count(pet_shop):
    # return len(pet_shop["pets"])

# 8, 9
def get_pets_by_breed(pet_shop, breed):
    found_pets = []
    for pet in pet_shop["pets"]:
        if pet ["breed"] == breed:
            found_pets.append(breed)
    return found_pets

# or

# def get_pets_by_breed(pet_shop, breed):
#     found_pets = []
#     pets = pet_shop["pets"]
#     for pet in pet_shop["pets"]:
#         if pet ["breed"] == breed:
#             found_pets.append(pet)
#     return found_pets

# 10, 11
def find_pet_by_name(pet_shop, name):
    for pet_name in pet_shop["pets"]:
        if pet_name["name"] == name:
            return pet_name
# def find_pet_by_name(pet_shop, name):
#     found_pet = None
#     for pet_name in pet_shop["pets"]:
#         if pet_name["name"] == name:
#             found_pet = pet_name
#     return pet_name

# 12 use the value which you find in previous function 11 - find_pet_by_name-
def remove_pet_by_name(pet_shop, name):
    pet_to_delete = find_pet_by_name (pet_shop, name)
    pet_shop["pets"].remove(pet_to_delete)

# or

# def remove_pet_by_name(pet_shop, pet_name):
#     for pet in pet_shop["pets"]:
#         if pet_name == (pet["name"]):
#             pet_shop["pets"].remove(pet)

# 13
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

# 14
def get_customer_cash(customer):
    return customer["cash"]

# 15
# or
# def remove_customer_cash(customer, amount):
    # customer["cash"] -= amount

def remove_customer_cash(customer, amount):
    total_amount = customer["cash"]
    new_amount = total_amount - amount
    # new_cash = customer["cash"]
    customer["cash"] = new_amount

# 16
def get_customer_pet_count(customer):
    return len(customer["pets"])

# def increase_pets_sold(pet_shop, add):
#     add = 2
#     return pet_shop["admin"]["pets_sold"].add
#     # sold = get_pets_sold(self.cc_pet_shop)
#

# 17
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
   

# OPTIONALS:

# 18, 19, 20
  
    def customer_can_afford_pet_(customer, pet):
        return customer ["cash"] >= pet["price"]

# or 
# def customer_can_afford_pet_(customer, pet):
#     if customer ["cash"] > pet ["price"]:
#         return True
#     elif customer ["cash"] == pet ["price"]:
#          return True
#     else:
#         return False

# 21, 22, 23

def sell_pet_to_customer__pet_found(pet_shop, pet , customer):
    if pet != None and customer_can_afford_pet(customer, pet):

        remove_pet_by_name(pet_shop, pet ["name"])
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        increase_pets_sold(pet_shop, 1)


# # or 
# def sell_pet_to_customer__pet_found(pet_shop, pet , customer):
#     if pet in pet_shop["pets"] and customer_can_afford_pet(customer, pet):
#         remove_pet_by_name(pet_shop, pet ["name"])
#         add_pet_to_customer(customer, pet)
#         remove_customer_cash(customer, pet["price"])
#         add_or_remove_cash(pet_shop, pet["price"])
#         increase_pets_sold(pet_shop, 1)

# # or 
# def sell_pet_to_customer__pet_found(pet_shop, pet , customer):
#     number_of_pets_sold = 1
#     if pet in pet_shop["pets"] and customer_can_afford_pet(customer, pet):
#         remove_pet_by_name(pet_shop, pet ["name"])
#         add_pet_to_customer(customer, pet)
#         remove_customer_cash(customer, pet["price"])
#         add_or_remove_cash(pet_shop, pet["price"])
#         increase_pets_sold(pet_shop, number_of_pets_sold)







# def remove_pet_by_name(pet_shop, pet_name):
#     for pet in pet_shop["pets"]:
#         if pet_name == (pet["name"]):
#             pet_shop["pets"].remove(pet)
