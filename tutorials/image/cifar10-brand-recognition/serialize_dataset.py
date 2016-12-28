import json
import os
import glob

# Import JSON data
with open('10k/top_brands_products.json') as inputData:
    jsonData = json.load(inputData)

deleteCount = 0

def deleteImage(imageUrl):
    if imageUrl is not None:
        filePath = '10k/' + str(imageUrl)
        if os.path.isfile(filePath):
            print("IMAGE DELETED")
            deleteCount += 1
            os.remove(str(filePath))

# Clear products and images without brands
for product in jsonData:
    # If product does not have a brand, remove that product
    if product.get("brand", None) is None:
        # Delete image
        imageUrl = product.get("image_path", None)
        deleteImage(imageUrl)
        # Remove product from json
        jsonData.remove(product)

# Clear images without references
imageFilenames = glob.glob1('10k/images', "*.jpg")
for filename in imageFilenames:
    fileFound = False
    for product in jsonData:
        imagePath = product["image_path"]
        if imagePath is not None:
            if filename in imagePath:
                fileFound = True
                break
    if fileFound == False:
        imagePath = 'images/' + filename
        deleteImage(imagePath)
        deleteCount += 1

print(deleteCount)
# Overwrite json file to include file path
# with open('10k/clean_products.json', 'w+') as outfile:
#     json.dump(jsonData, outfile, indent=2)
