import json
import os
import glob

# Import JSON data
with open('10k/products.json') as inputData:
    jsonData = json.load(inputData)

print("Starting Product Count: " + str(len(jsonData)))

topBrands = ["Bugatchi", "Peter Millar", "John Varvatos", "Ermenegildo Zegna", "Rag & Bone", "Robert Graham", "Burberry", "Club Monaco", "Givenchy", "Theory"]
matchingItems = []
for product in jsonData:
    if product.get("brand", None) is not None:
        brandName = product["brand"]
        # If this brand is not one of the top brands
        if brandName in topBrands:
            matchingItems.append(product)
        else:
            # Delete image
            imageUrl = product.get("image_path", None)
            if imageUrl is not None:
                filePath = '10k/' + str(imageUrl)
                if os.path.isfile(filePath):
                    os.remove(str(filePath))

print("Final Product Count: " + str(len(matchingItems)))

# Overwrite json file to include file path
with open('10k/top_brands_products.json', 'w+') as outfile:
    json.dump(matchingItems, outfile, indent=2)
