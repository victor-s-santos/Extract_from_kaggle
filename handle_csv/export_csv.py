import os


def download_csv(credentials: dict, dataset_owner: str, dataset_name: str):
    os.environ["KAGGLE_USERNAME"] = credentials["username"]
    os.environ["KAGGLE_KEY"] = credentials["key"]
    from kaggle.api.kaggle_api_extended import KaggleApi

    try:
        api = KaggleApi()
        api.authenticate()
    except Exception as e:
        raise Exception(f"An error: {e}")

    try:
        datasets = api.dataset_list(search=f"{dataset_owner}/{dataset_name}")

        for dataset in datasets:
            api.dataset_download_files(
                dataset=dataset.ref, path=".", force=False, unzip=True
            )

        print("The dataset has been downloaded successfully!")
    except Exception as e:
        raise Exception(f"An error: {e}")


if __name__ == "__main__":
    from decouple import config

    dict_credentials = {"username": config("KAGGLE_USER"), "key": config("KAGGLE_KEY")}
    full_dict = {
        "credentials": dict_credentials,
        "dataset_owner": "joebeachcapital",
        "dataset_name": "fast-food",
    }
    download_csv(**full_dict)
