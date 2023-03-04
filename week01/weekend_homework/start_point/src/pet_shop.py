import pdb
# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(petshop):
    return petshop["name"]

def get_total_cash(petshop):
    return petshop["admin"]["total_cash"]

def add_or_remove_cash(petshop,cash):
    petshop["admin"]["total_cash"] += cash

def get_pets_sold(petshop):
    return petshop["admin"]["pets_sold"]

def increase_pets_sold(petshop,sold_qty):
    petshop["admin"]["pets_sold"] += sold_qty

def get_stock_count(petshop):
    return len(petshop["pets"])

def get_pets_by_breed(petshop,breed):
    list_of_pets = []
    for pet in petshop["pets"]:
        if pet["breed"] == breed:
            list_of_pets.append(pet)
    return list_of_pets

def find_pet_by_name(petshop,name):
    for pet in petshop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(petshop,name):
    # current_index = 0
    # for pet in petshop["pets"]:
    #     if pet["name"] == name:
    #         petshop["pets"].pop(current_index)
    #     current_index += 1
    petshop["pets"].remove(find_pet_by_name(petshop,name))


def add_pet_to_stock(petshop,new_pet):
    petshop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer,amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer,new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    cost_of_pet = new_pet["price"]
    customer_cash = get_customer_cash(customer)
    return customer_cash >= cost_of_pet

def sell_pet_to_customer(petshop,pet,customer):
    pet_not_exists = (pet == None)
    if pet_not_exists:
        pass
    elif customer_can_afford_pet(customer,pet):
        remove_pet_by_name(petshop,pet["name"])
        add_pet_to_customer(customer,pet)
        add_or_remove_cash(petshop,pet["price"])
        remove_customer_cash(customer,pet["price"])
        increase_pets_sold(petshop,1)
       