# WRITE YOUR FUNCTIONS HERE
# This is a comment 
# pet_shop_name = str("Camelot of Pets")
def get_pet_shop_name(pet_shop):
        return pet_shop["name"]


def get_total_cash(pet_shop):
    # sum = get_total_cash
    return pet_shop["admin"]["total_cash"]
        
# def add_or_remove_cash(pet_shop, amount):
#     return pet_shop["admin"]["total_cash"] + amount

def add_or_remove_cash(pet_shop, amount):
    total_amount= pet_shop["admin"]["total_cash"]
    new_amount = total_amount + amount
    pet_shop["admin"]["total_cash"] = new_amount 
    return (new_amount)

# def add_or_remove_cash(pet_shop, amount):
#     total_amount= pet_shop["admin"]["total_cash"]
#     new_amount = total_amount - amount
#     pet_shop["admin"]["total_cash"] = new_amount 
#     return (new_amount)

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, sold):
    pets_sold = pet_shop["admin"]["pets_sold"]
    increased_sales = pets_sold + sold
    pet_shop["admin"]["pets_sold"] = increased_sales
    return (increased_sales)

def get_stock_count(pet_shop):
    stock = len(pet_shop["pets"])
    return stock

def get_pets_by_breed(pet_shop, breed):
    matching = []
    for match in pet_shop["pets"]:
        if match["breed"] == breed:
            matching.append(breed)
    return matching

# def get_pets_by_breed(pet_shop, breed):
#     unmatching = None
#     for match in pet_shop["pets"]:
#         if match["breed"] == None:
#             # unmatching.pop(breed)
#             return unmatching

# def find_pet_by_name(pet_shop, name):
#     for pet_name in pet_shop["pets"]:
#         if pet_name["name"] == name:
#             return pet_name

def find_pet_by_name(pet_shop, name):
    pet_name = "Fred"
    for pet_name in pet_shop["pets"]:
        if pet_name["name"] == name:
            return pet_name
        else:
            return None

def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet_name == (pet["name"]):
            pet_shop["pets"].remove(pet)

# def add_pet_to_stock(pet_shop, pet):
#     new_pet = []
#     pet_shop.append(new_pet)
#     count = len(pet_shop["pets"])
#     return count
    
def get_customer_cash(customer):
    return customer["cash"]

# def remove_customer_cash(customer, amount):
#     amount = 100
#     total_amount = customer["cash"]
#     new_amount = total_amount - amount
#     new_cash = customer["cash"]
#     return (new_cash)

def get_customer_pet_count(customer):
    return customer["pets"]
     
# def increase_pets_sold(pet_shop, add):
#     add = 2
#     return pet_shop["admin"]["pets_sold"].add
#     # sold = get_pets_sold(self.cc_pet_shop)
#

def add_pet_to_customer(customer, new_pet):
    add_pet_to_customer = []
    animals = []
    animals.append(new_pet)
    get_customer_pet_count(customer) == len(customer["pets"])






# def remove_pet_by_name(pet_shop, pet_name):
#     for pet in pet_shop["pets"]:
#         if pet_name == (pet["name"]):
#             pet_shop["pets"].remove(pet)
