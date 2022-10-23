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

# def add_or_remove_cash(pet_shop, amount):
#     total_amount= pet_shop["admin"]["total_cash"]
#     new_amount = total_amount + amount
#     pet_shop["admin"]["total_cash"] = new_amount 
#     return (new_amount)

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

# def stock_count(pet_shop):
#     stock = len("pets")
#     return stock

def get_pets_by_breed(pet_shop, breed):
    matching = []
    for match in pet_shop["pets"]:
        if match["breed"] == breed:
            matching.append(breed)
    return matching


def find_pet_by_name(pet_shop, name):
    for pet_name in pet_shop["pets"]:
        if pet_name["name"] == name:
            return pet_name

# def increase_pets_sold(pet_shop, add):
#     add = 2
#     return pet_shop["admin"]["pets_sold"].add
#     # sold = get_pets_sold(self.cc_pet_shop)
#  

# def find_pet_by_name(pet_shop, name):
#     for pet_name in pet_shop["pets"]:
#         if pet_name["name"] == name:
#             return pet_name
