import zipfile
import fctlist as fl

root_folder = "/Users/PycharmProjects/SearchThroughZipForNames/"

files_and_folders = fl.search_for_zip_file(root_folder)

for single_files_and_folders in files_and_folders:
    if not single_files_and_folders.__contains__("."):
        files = fl.search_for_zip_file(root_folder + single_files_and_folders + "/")
        for file in files:
            file_or_folder = root_folder + single_files_and_folders + "/" + file
            if (file_or_folder).__contains__(".py"):
                break
            archive = zipfile.ZipFile(file_or_folder, 'r')
            list = archive.filelist
            with open(str(file) + ".txt", "a") as file_name:
                for element in list:
                    file_name.write(element.filename + "\n")

