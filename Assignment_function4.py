def filter(**kwargs):
    non_empty_fields = {}
    for key, value in kwargs.items():
        if value: 
            non_empty_fields[key] = value
    return non_empty_fields


result = filter(name="Neenu", age=36, city="", occupation="Engineer", hobby="")
print(result) 