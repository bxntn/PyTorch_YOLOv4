import os
def change_name(folder,name,class_number):
    for file_name in os.listdir(folder):
        # Construct old file name
        source = folder + file_name
        # trim file
        tmp_name = file_name[:-4].split('.')
        new_file_name = "".join(tmp_name)
        
        #yolov4 can't find label if label's name has 'jpg' in the name
        tmp_name = new_file_name.split('jpg')
        new_file_name = "".join(tmp_name)
        destination = folder + new_file_name[0] + class_number + new_file_name[2:] + name
        
        # Renaming the file
        os.rename(source, destination)
        
def main(root_folder):
    #initialize the class number
    class_number = 0
    # iterate all files from a directory
    for train_type in os.listdir(root_folder):
        type_folder_PATH = root_folder + os.sep + train_type 
        for train_class in os.listdir(type_folder_PATH):
            class_folder_PATH = type_folder_PATH + os.sep + train_class
            for sub_folder in os.listdir(class_folder_PATH):
                if not (sub_folder.endswith('.zip') or sub_folder.endswith('.yaml')):
                    folder = class_folder_PATH + os.sep + sub_folder
                    images_folder = folder + os.sep + 'images' + os.sep 
                    labels_folder = folder + os.sep + 'labels' + os.sep
                    change_name(images_folder,'.jpg',str(class_number))
                    change_name(labels_folder,'.txt',str(class_number))
                    
                    #This section changes the class number in .txt file of each class /labels folder
                    for filename in os.listdir(labels_folder):
                        with open(os.path.join(labels_folder, filename), 'r') as f:
                            lines = f.readlines() 
                            # print(lines)
                        new_line = []
                        for line in lines:
                            new_line.append(line.replace(line[0],str(class_number),1))
                        with open(os.path.join(labels_folder, filename), 'w') as f:
                            f.write(''.join(new_line))
            print(train_class,":",class_number,"Finish")
            class_number+=1
        
    # verify the result
    # res = os.listdir(folder)
    # print(res)
        
#PATH to data_folder
#Only change here
root_folder = r'E:\robocup_data\data'

if __name__ == '__main__':
    main(root_folder)
