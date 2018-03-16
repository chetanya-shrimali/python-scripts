import os


def rename_files():
    files_list = os.listdir(r'C:\Users\Chetanya\PycharmProjects\FullStackWebDevelopment\prank\prank')
    # r shows to take the string as it is
    print(files_list)
    saved_path = os.getcwd()
    print(saved_path)

    os.chdir(r'C:\Users\Chetanya\PycharmProjects\FullStackWebDevelopment\prank\prank')

    for file_name in files_list:
        # 1 translate one set of characters to other set
        # 2 takes the list characters to be removed
        os.rename(file_name, file_name.lstrip("0123456789"))
        print(file_name)

    os.chdir(saved_path)
    print(files_list)


rename_files()
