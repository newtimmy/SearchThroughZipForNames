# import OS module
import os

def search_for_zip_file(path):

    # Get the list of all files and directories
    dir_list = os.listdir(path)
    #print("Files and directories in '", path, "' :")
    # prints all files
    #print(dir_list)
    return dir_list


