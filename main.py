from pathlib import Path

def createfile():
    try:
        name = input("Tell your file name: ")
        path = Path(name)
        if not path.exists():
            with open(path,"w") as f:
                data = input("What do you want to write: ")
                f.write(data)
            print("File created successfully!")
        else:
            print("Error! File name already exists.")
    except Exception as err:
        print(f"An error occured as: {err}")


def readfile():
    try:
        name = input("Tell your file name: ")
        path = Path(name)
        if path.exists():
            with open(path,"r") as f:
                content = f.read()
                print("Your File content is:\n",content)
        else: 
            print("File Doesn't Exists!")
    except Exception as err:
        print(f"An error occured as: {err}")


def updatefile():
    try:
        name = input("Tell your file name: ")
        path = Path(name)

        if path.exists():
        
            print("Update file Operations:")
            print("1) Renaming The File. ")
            print("2) Appending The Content. ")
            print("3) Overwriting The File. ")

            choice = int(input("\nEnter your option: "))

            if choice == 1:
                newname = input("Tell your new file name:")
                newpath = Path(newname)

                if not newpath.exists():
                    path.rename(newpath)
                    print("Rename Successfully!")
                else:
                    print("Error! File already exists.")
                
            elif choice == 2:
                with open(path, "a") as f:
                    data = input("What do you want to append: ")
                    f.write("\n" + data)
                print("Successfully Appended!")

            elif choice == 3:
                with open(path, "w") as f:
                    data = input("What do you want to overwrite: ")
                    f.write(data)
                print("Overwrite Successfully!")

            else:
                print("Invalid option!")
        else:
            print("Error! File doesn't exists.")
        
    except Exception as err:
        print(f"An error occured as: {err}")


def deletefile():
    try:
        name = input("Tell your file name: ")
        path = Path(name)
        if path.exists():
            path.unlink()
            print("File deleted successfully!")
        else: 
            print("File doesn't exists!")
    except Exception as err:
        print(f"An error occured as: {err}")

while True:
    print("1) Press 1 for Creating a file. ")
    print("2) Press 2 for Reading a file. ")
    print("3) Press 3 for Updating a file. ")
    print("4) Press 4 for Deleting the file. ")
    print("5) Exit")

    try:
        a = int(input("\nTell your response: "))
        if a == 1:
            createfile()
        elif a == 2:
            readfile()
        elif a == 3:
            updatefile()
        elif a == 4:
            deletefile()
        elif a == 5:
            print("Exiting program...")
            break
        else:
            print("Invalid response!")
    except Exception as err:
        print(f"An error Occured as: {err}")