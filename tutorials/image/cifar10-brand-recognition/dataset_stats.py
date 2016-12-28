# Prints out statistics about the contents of this dataset
# Item Count
# Image Count
# Unique Brand Count

import json
import os
import glob
from operator import itemgetter

# Import JSON data
with open('10k/top_brands_products.json') as inputData:
    jsonData = json.load(inputData)

# Number of products
productCount = 0
# Number of images
imageCount = len(glob.glob1('10k/images', "*.jpg"))
# Keep track of the number of unique brands
uniqueBrands = []

def newBrand(name) :
    return {"brand": brand, "count": 0}

def incrementBrandCount(brandDict):
    count = brandDict["count"]
    brandDict["count"] = count + 1

for product in jsonData:
    productCount += 1
    # Increment unique brands if needed
    brand = product.get("brand", None)
    if isinstance(brand, basestring) and brand is not None:
        alreadyExists = False
        for brandDict in uniqueBrands:
            if brandDict["brand"] == brand:
                alreadyExists = True
                break
        # Add to the dictionary or increment brand count
        if alreadyExists is False:
            uniqueBrands.append(newBrand(brand))
        else:
            incrementBrandCount(brandDict)

# Output helpers
def topBrands(number):
    brands = sorted(uniqueBrands, key=itemgetter('count'), reverse=True)
    return brands[:number]

def printTopBrands(number):
    brands = topBrands(number)
    print("\n" + "TOP BRANDS:")
    for brand in brands:
        logBrand(brand)

def logBrand(brand):
    brandName = brand["brand"]
    brandCount = brand["count"]
    print (str(brandName) + ': ' + str(brandCount))

def rawBrandList(minRank):
    rawBrands = []
    for brand in topBrands(minRank):
        rawBrands.append(brand["brand"])
    return rawBrands

# Output statistics
print('Product Count: ' + str(productCount))
print('Image Count: ' + str(imageCount))
print('Unique Brands Count: ' + str(len(uniqueBrands)))
printTopBrands(10)
# print(json.dumps(rawBrandList(10)))
