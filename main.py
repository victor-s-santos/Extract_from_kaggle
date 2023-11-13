from handle_csv.export_csv import download_csv
from decouple import config
from csv import DictReader
from mongo_connection.main import Mongo
import os


if __name__ == "__main__":
    kaggle_credentials = {
        "username": config("KAGGLE_USER"),
        "key": config("KAGGLE_KEY"),
    }
    mongo_credentials = {
        "user": config("MONGO_USERNAME"),
        "password": config("MONGO_PASSWORD"),
        "host": config("MONGO_HOST"),
        "port": config("MONGO_PORT"),
        "db_name": config("MONGO_DBNAME"),
    }
    full_dict = {
        "credentials": kaggle_credentials,
        "dataset_owner": "joebeachcapital",
        "dataset_name": "fast-food",
    }
    mongo_obj = Mongo(credentials=mongo_credentials)
    mongo_obj.connect_to_mongo()
    my_db = mongo_obj.get_connection()

    download_csv(**full_dict)
    csv_files_list = []
    for file in os.listdir():
        if file.endswith(".csv"):
            csv_files_list.append(file)

    for csv_file in csv_files_list:
        my_collection = my_db[csv_file]
        with open(csv_file, "r") as file:
            dict_objs = DictReader(file)
            for dicio in dict_objs:
                my_collection.insert_one(dict(dicio))
