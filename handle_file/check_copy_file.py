import os
import shutil

def check_file_exists() -> bool:
    """Checks if the kaggle.json file exists in current directory.

    Returns:
        bool: True if file is in current directory or False if it isn't.
    """
    file = "kaggle.json"
    return os.path.isfile(file)

def copy_file() -> str:
    """Copy the kaggle.json file to necessary destination.

    Returns:
        str: The success or error message.
    """
    kaggle_path = f"/home/{os.getlogin()}/.kaggle"
    try:
        shutil.copyfile("kaggle.json", f"{kaggle_path}/kaggle.json")
        return (f"The file can be find in the following location: {kaggle_path}/kaggle.json")
    except Exception as e:
        return(e)


if __name__ == "__main__":
    if check_file_exists():
        copy_file()