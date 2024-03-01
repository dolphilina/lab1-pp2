import json

file_path = 'json1\\data.json'

with open(file_path) as json_file:
    data = json.load(json_file)

print("Interface status")
print("="*80)
print("DN", " " * 38, "Description", " " * 3, "Speed", " " * 8, "MTU")
print("-" * 41, "-" * 13, " ", "-" * 6, " " * 6, "-" * 6)

for imdata in data["imdata"]:
    for l1PhysIf in imdata:    
        for attributes in imdata[l1PhysIf]:
            print(imdata[l1PhysIf][attributes]["dn"],"\t", "\t", imdata[l1PhysIf][attributes]["speed"], "\t", imdata[l1PhysIf][attributes]["mtu"])