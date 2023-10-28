import os

def check_directory_exists() -> bool:
    """Check if the kaggle directory exists in /home/ 

    Returns:
        bool: True if the directory exists and false if the directory doesn't exist.
    """
    path = f"/home/{os.getlogin()}/.kaggle/"
    return os.path.exists(path)

def create_kaggle_directory() -> str:
    """Create a directory called .kaggle

    Returns:
        str: The success or error message.
    """
    kaggle_path = f"/home/{os.getlogin()}/.kaggle"
    try:
        os.mkdir(kaggle_path)
        return(f"The {kaggle_path} directory has been created successfully!")
    except Exception as e:
        return(f"An error has been occured: {e}.")

if __name__ == "__main__":
    if not check_directory_exists():
        create_kaggle_directory()