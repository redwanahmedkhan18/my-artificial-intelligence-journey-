#Convert dict to JSON

import json

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

with open('inventory_management_details.json','w') as json_file:
    json.dump(inventory,json_file,indent=4)

with open('inventory_management_details.json','r') as json_file:
    data=json.load(json_file)
    print(data)