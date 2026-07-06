from pathlib import Path

def create_folder():
    try:
        name = input("please tell your folder name : -")
        p = Path(name)
        p.mkdir()
        print("folder created successflly")
    except Exception as err:
        print("sorry an error occured as {err}")  

def read_file_folder():
    p = Path("")
    items = list(p.rglob('*')) 
    for i, v in enumerate(items):
        print(f"{i + 1}: {v}") 

def update_folder():
    try:

        read_file_folder()
        old_name = input("please tell which folder you want to update : -")
        p = Path(old_name)
        if p.exists() and p.is_dir():
            new_name = input("please tell your new folder name : -")
            new_p = Path(new_name)
            p.rename(new_p)
            print("your folder name is updated successfully")

        else:
            print("sorry no such folder exist") 

    except Exception as err:
        
        print("An error occured as {err}")

def delete_folder():
    try:
        read_file_folder()
        name = input("please tell which folder you want to delete : -")
        p = Path(name)
        if p.exist() and p.is_dir():
            p.rmdir()
            print("folder deleted successfully")

        else:
            print("no such folder exist")

    except Exception as err: 
        print("Ther was an error as {err}")       



while True:
    print("options : - ")

    print("1. Create a folder")
    print("2. Read files and folders")
    print("3. Update the folder")
    print("4. Delete the folder")
    print("0. Exit the program")


    choice = int(input("please choose your option"))


    if choice == 1:
        create_folder()

    if choice == 2:
        read_file_folder()

    if choice == 3:
        update_folder()

    if choice == 4:
        delete_folder()
    