from PIL import Image
import glob
import numpy as np

LAST_TRAINING_INDEX = 1532

training_binary = []
eval_binary = []

filenames = glob.glob1('10k/images', "*.jpg")
for index,filename in enumerate(filenames):
    path = '10k/images/' + filename

    img = Image.open(path)
    img = (np.array(img))

    label = [1]
    r = img[:,:,0].flatten()
    g = img[:,:,1].flatten()
    b = img[:,:,2].flatten()

    formatted_binary = list(label) + list(r) + list(g) + list(b)

    if index > LAST_TRAINING_INDEX:
        eval_binary.append(formatted_binary)
    else:
        training_binary.append(formatted_binary)

# Output training binary
out = np.array(training_binary, np.uint8)
out.tofile("data/training_batch.bin")

# Output evaluation binary
out = np.array(training_binary, np.uint8)
out.tofile("data/test_batch.bin")
