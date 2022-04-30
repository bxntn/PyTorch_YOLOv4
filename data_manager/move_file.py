import os
import shutil

def move (folder,name,sub_folder):
    for file_name in os.listdir(folder):
        # Construct old file name
        source = folder + file_name
        # new location 
        if name == '.jpg':
            path = 'images'
        else : path = 'labels'
        #PATH_To_Outdir is where all the file go to
        destination = r'PATH_To_Outdir' + os.sep + sub_folder + os.sep + path + os.sep + file_name

        # move the file
        shutil.move(source, destination)

#PATH to data_folder that want to move
root_folder = r'PATH_TO_DATA'
sub_folders = ['test','train','valid']
# iterate all files from a directory
for train_type in os.listdir(root_folder):
    type_folder_PATH = root_folder + os.sep + train_type 
    for train_class in os.listdir(type_folder_PATH):
        class_folder_PATH = type_folder_PATH + os.sep + train_class
        for sub_folder in sub_folders:
                folder = class_folder_PATH + os.sep + sub_folder
                images_folder = folder + os.sep + 'images' + os.sep 
                labels_folder = folder + os.sep + 'labels' + os.sep
                move(images_folder,'.jpg',sub_folder)
                move(labels_folder,'.txt',sub_folder)