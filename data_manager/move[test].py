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
        destination = r'E:\robocup_data\asd' + os.sep + sub_folder + os.sep + path + os.sep + file_name

        # move the file
        shutil.move(source, destination)

#PATH to data_folder that want to move
root_folder = r'E:\robocup_data\asd'
# sub_folders = ['test','train','valid']
sub_folder = 'train'

folder = root_folder + os.sep + 'valid'
images_folder = folder + os.sep + 'images' + os.sep 
labels_folder = folder + os.sep + 'labels' + os.sep
move(images_folder,'.jpg',sub_folder)
move(labels_folder,'.txt',sub_folder)