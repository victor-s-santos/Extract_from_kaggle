import os
from handle_path.check_create_directory import (
    check_directory_exists,
    create_kaggle_directory,
)
from handle_file.check_copy_file import check_file_exists, copy_file

dataset_name = "joebeachcapital/fast-food"

destination_path = "."

unzip = True

if __name__ == "__main__":
    if not check_directory_exists():
        create_kaggle_directory()

        if check_file_exists():
            copy_file()
