import json

x= '{ "name":"Neenu", "age":35, "city":"India", "occupation":"Software Engineer"}'

y = json.loads(x)   
print(y["name"])
print(y["age"])
print(y["city"])
print(y["occupation"])
