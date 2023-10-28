import os
import shutil

dataset_name = "joebeachcapital/fast-food"

destination_path = "."

unzip = True
kaggle_path = f"/home/{os.getlogin()}/.kaggle"
try:
    os.mkdir(kaggle_path)
    shutil.copyfile("kaggle.json", f"{kaggle_path}/kaggle.json")
except FileExistsError as e:
    pass
except Exception as e:
    print(e)

try:
    import kaggle
    kaggle.api.dataset_download_files(dataset=dataset_name, path=destination_path, unzip=unzip)
    print("Dataset downloaded successfully!")
except Exception as e:
    print(f"An error has been occured: {e}")