# PDA evidence: Week 1

def add_pet_to_customer(customer,new_pet):
    customer["pets"].append(new_pet)


new_pet = {
    "name": "Bors the Younger",
    "pet_type": "cat",
    "breed": "Cornish Rex",
    "price": 100
}

customer = {
    "name": "Alice",
    "pets": [],
    "cash": 1000
}

print(f"Before the function runs:  {customer}")
add_pet_to_customer(customer, new_pet)
print(f"After the function runs {customer}")