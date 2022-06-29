import os
from PIL import Image

data = []
labels = []
cur_path = os.getcwd()
print(cur_path)

cur_path = cur_path+'\Train'
print(cur_path)

classes = 43
for i in range(classes):
    path = os.path.join(cur_path,str(i))
    print(os.listdir(path))
    images = os.listdir(path)
    for a in images:
        try:
            image = Image.open(path + '\\' + a)
            image = image.resize((30, 30))
            image = np.array(image)
            # sim = Image.fromarray(image)
            data.append(image)
            labels.append(i)
        except:
            print("Error loading image")