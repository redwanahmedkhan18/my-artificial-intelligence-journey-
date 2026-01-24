def celcius_to_fahrenheit(celcius):
    fahrenheit= 1.8* celcius +32

    return fahrenheit



def fahrenheit_to_cellcius(fahrenheit):
    celcius =(fahrenheit -32)/1.8

    return celcius

f=celcius_to_fahrenheit(-40)
print(f)

c=fahrenheit_to_cellcius(-40)

print(c)

