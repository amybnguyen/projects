import os
import shutil


# location of folder containing pictures
new_directory = "RAF-images"
pic_folder = "C:/Users/Amy Nguyen/Downloads/test-pics"
RAF_FOLDER = os.path.join(pic_folder, new_directory)

# list of files within the path
images = os.listdir(pic_folder)

for image in images:
    extension = os.path.splitext(image)[1]
    if extension == ".RAF":
        if not os.path.isdir(RAF_FOLDER):
            os.mkdir(RAF_FOLDER)
        curr_img_directory = os.path.join(pic_folder, image)
        new_img_directory = os.path.join(RAF_FOLDER, image)
        shutil.move(curr_img_directory, new_img_directory)

print(images)
