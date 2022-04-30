import os

image_files = []
# PATH_to_images_folder = ""
for filename in os.listdir("PATH_to_images_folder"):
    if filename.endswith(".jpg" or ".png"):
        #/train/images
        image_files.append("PATH_to_image" + filename)
os.chdir("PATH_to_images_folder")
os.chdir("..")
with open("test.txt or train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")