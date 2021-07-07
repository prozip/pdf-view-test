x = {
    "name":"John",
    "age": ['12','13']
}
list = x['age']
list.append('15')
x['age'] = list
print(x)