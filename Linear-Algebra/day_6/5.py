def final_price(price,discount=10):
    if price<0:
        return "price can't be negative"
    else:
        price= price -(price *(discount)/100)
        return price
    

print(final_price(100))

print(final_price(100,discount=20))

print(final_price(-50))