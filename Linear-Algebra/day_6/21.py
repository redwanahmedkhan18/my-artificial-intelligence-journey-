def greet(**kwargs):
    name=kwargs.get("name")
    tone=kwargs.get("tone")
    if tone=="formal":
        return f"Good Day, {name}!"
    elif tone=="casual":
        return f"Hey, {name}!"
    

print(greet(name="Redwan", tone="formal"))