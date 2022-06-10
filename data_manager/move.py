import os
import shutil

def move (folder,name,sub_folder,outdir):
    for file_name in os.listdir(folder):
        # Construct old file name
        source = folder + file_name
        # new location 
        if name == '.jpg':
            path = 'images'
        else : path = 'labels'
        #PATH_To_Outdir is where all the file go to
        destination = outdir + os.sep + sub_folder + os.sep + path + os.sep + file_name

        # move the file
        shutil.move(source, destination)
        
def main(root_folder,sub_folders,outdir):
    # iterate all files from a directory
    for train_type in os.listdir(root_folder):
        type_folder_PATH = root_folder + os.sep + train_type 
        for train_class in os.listdir(type_folder_PATH):
            class_folder_PATH = type_folder_PATH + os.sep + train_class
            for sub_folder in sub_folders:
                    folder = class_folder_PATH + os.sep + sub_folder
                    images_folder = folder + os.sep + 'images' + os.sep 
                    labels_folder = folder + os.sep + 'labels' + os.sep
                    move(images_folder,'.jpg',sub_folder,outdir)
                    move(labels_folder,'.txt',sub_folder,outdir)
            print(train_class,"has been moved")

#PATH to data_folder that want to move
#Only change here
ROOTDIR = r'E:\robocup_data\data'
sub_folders = ['test','train','valid']
OUTDIR = r'E:\robocup_data\train_data_aug_70_20_10'
      
if __name__ == '__main__':
    main(ROOTDIR,sub_folders,OUTDIR)