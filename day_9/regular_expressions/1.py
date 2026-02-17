import re

txt='''Hello, my name is Redwan Ahmed.
I live in Dhaka, Bangladesh.
My phone number is +880-1712-345678.
My backup number is 01718-998877.
My email is redwan.ai@gmail.com.
My secondary email is redwan_2024@outlook.com.'''

pattern=r'(?:\+880-\d{4}-\d{6}|\d{5}-\d{6})'
x=re.findall(pattern,txt)

print(x)

email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

emails = re.findall(email_pattern, txt)
print(emails)

country_pattern= r'\b(Afghanistan|Albania|Algeria|Argentina|Australia|Austria|Bangladesh|Belgium|Brazil|Canada|China|Denmark|Egypt|Finland|France|Germany|Greece|India|Indonesia|Iran|Iraq|Ireland|Italy|Japan|Malaysia|Mexico|Nepal|Netherlands|New Zealand|Norway|Pakistan|Poland|Portugal|Qatar|Russia|Saudi Arabia|Singapore|South Africa|South Korea|Spain|Sri Lanka|Sweden|Switzerland|Thailand|Turkey|UAE|United Arab Emirates|UK|United Kingdom|USA|United States|Vietnam|Zimbabwe)\b'



countries= re.findall(country_pattern, txt)

print(countries)

city_pattern = r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b'
cities=re.findall(city_pattern,txt)
print(cities)


