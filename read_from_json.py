import json

with open('amazfit.json', 'r') as json_file:
    all = json.load(json_file)

items_list = all['data']['productsFilter']['record']['products']
for i in range(len(items_list)):
    print(items_list[i]['id'])
    print(items_list[i]['name'])
    print(items_list[i]['price']['current'])
    for property in items_list[i]['propertiesShort']:
        print(property['name'], property['value'])
    print()
