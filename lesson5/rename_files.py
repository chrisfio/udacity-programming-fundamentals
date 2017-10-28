import os
def rename_files():
    #get file names from a folder
    file_list = os.listdir("/home/fio/Desktop/udacity/lesson5/prank")
    print(file_list)

    save_path = os.getcwd()
    os.chdir("/home/fio/Desktop/udacity/lesson5/prank")

    #for each file, rename filename
    for each in file_list:
        os.rename(each, each.translate(None,"0123456789"))

    print(file_list)
    os.chdir(save_path)
    
rename_files()
