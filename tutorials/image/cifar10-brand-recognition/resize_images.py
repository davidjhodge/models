# TARGET SIZE 32x32

from PIL import Image
import os
import glob

output_directory = '10k/cropped_images'
# Create new output directory or clear old one if needed
if os.path.exists(output_directory):
    shutil.rmtree(output_directory)
os.makedirs(output_directory)

filenames = glob.glob1('10k/images', "*.jpg")
for filename in filenames:
    path = '10k/images/' + filename

    img = Image.open(path)
    size = (32,32)
    img.thumbnail(size, Image.ANTIALIAS)

    final_img = Image.new('RGBA', size, (255, 255, 255, 0))  #with alpha
    final_img.paste(img, ((size[0] - img.size[0]) / 2, (size[1] - img.size[1]) / 2))

    newPath = output_directory + '/' + filename
    final_img.save(newPath)
