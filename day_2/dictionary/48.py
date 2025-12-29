#Inventory management system
inventory={
    "item_1":{
        "name":"Laptop",
        "quantity":50,
        "price_per_unit":800,
        "supplier":"Tech Supplies Co."
    },
    "item_2":{
        "name":"Smartphone",
        "quantity":200,
        "price_per_unit":500,
        "supplier":"Mobile World Inc."
    },
    "item_3":{
        "name":"Tablet",
        "quantity":150,
        "price_per_unit":300,
        "supplier":"Gadget Hub Ltd."
    },
    "item_4":{
        "name":"Headphones",
        "quantity":300,
        "price_per_unit":100,
        "supplier":"Audio Essentials"
    }
}

#Read

print(inventory["item_1"]["name"])

#Create
inventory["item_5"]={
    "name":"Smartwatch",
    "quantity":120,
    "price_per_unit":200,
    "supplier":"Wearable Tech Co."
}

print(inventory)

#Update
inventory["item_4"]["price_per_unit"]=350

print(inventory)    

#Delete

if "supplier_id" in inventory["item_5"]:
    del inventory["item_5"]["supplier_id"]


print(inventory)

