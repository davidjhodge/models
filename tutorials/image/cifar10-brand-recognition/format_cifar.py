import json
from top_brand_keys import brand_key_lookup

# Import JSON data
with open('10k/top_brands_products.json') as inputData:
    jsonData = json.load(inputData)


formattedData = []
for product in jsonData:
    brand = product["brand"]
    label = int(brand_key_lookup[brand])
    image = str(product["image_path"])
    if label is not None and image is not None:
        newItem = {"label": label, "image": image}
        formattedData.append(newItem)

# Overwrite json file to include file path
with open('10k/dataset.json', 'w+') as outfile:
    json.dump(formattedData, outfile, indent=2)
