from handle_csv.export_csv import download_csv
from decouple import config

if __name__ == "__main__":
    dict_credentials = {"username": config("KAGGLE_USER"), "key": config("KAGGLE_KEY")}
    full_dict = {
        "credentials": dict_credentials,
        "dataset_owner": "joebeachcapital",
        "dataset_name": "fast-food",
    }
    download_csv(**full_dict)
