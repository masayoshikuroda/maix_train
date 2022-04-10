import sys
import os
import shutil
from PIL import Image

IMAGE_WIDTH  = 224
IMAGE_HEIGHT = 224
IMAGE_COUNT  = 40

src_path = sys.argv[1]
zip_path = sys.argv[2]
trim_label = True

print("src_path: ", src_path)
print("zip_path: ", zip_path)

os.mkdir(zip_path)

for f in os.listdir(src_path):
    f = os.path.join(src_path, f)
    if os.path.isfile(f):
        continue
    label = os.path.basename(f)
    #print("label: ", label)
    d = os.path.join(zip_path, "images", label)
    os.makedirs(d)

    count = 0
    for i in os.listdir(f):
        s = os.path.join(f, i)
        t = os.path.join(d, i)
        if os.path.isdir(i):
            continue
        count = count + 1
        img = Image.open(s)
        img = img.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
        img.save(t)
        #print("    ", "save: ", t)
    #print("   ", "count: ", count)
    if count <= IMAGE_COUNT:
        print("WARN: ", f"Image file count must over {IMAGE_COUNT}. count={count}, lavel={label}")
        if trim_label:
            print("Trim insuffcient image cout label. label={label}")
            shutil.rmtree(d)

shutil.make_archive(zip_path, "zip", zip_path)
shutil.rmtree(zip_path)
print("Created: ", zip_path + ".zip")
