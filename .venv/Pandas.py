import json

with open('../archive/dataset/case-accessory.json', 'r') as f:
    json_data = f.read

data_dict = json_data.loads(json_data)
print(data_dict)
