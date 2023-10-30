import kaggle


def download_csv(dataset_owner: str, dataset_name: str):
    try:
        kaggle.api.dataset_download_files(
            dataset=f"{dataset_owner}/{dataset_name}", path=".", unzip=False
        )
        return "Your dataset has {dataset_name} been downloaded successfully!"
    except Exception as e:
        return f"An error: {e}"


if __name__ == "__main__":
    download_csv(dataset_owner="joebeachcapital", dataset_name="fast-food")
