import pymongo
from pymongo import MongoClient
import pandas as pd
import certifi


class Mongo:
    def __init__(self, url):
        self.mongo_client = MongoClient(url, tlsCAFile=certifi.where())

    def set_database(self, database):
        self.database = database

    def get_database(self):
        try:
            return self.mongo_client.get_database(self.database)
        except:
            return self.mongo_client.get_database()

    def get_collection_name(self, collection_name):
        return self.get_database()[collection_name]

    def get_collection(self, collection_name, find_condition={}, sort_condition=[("_id", pymongo.ASCENDING)], limit_condition=0):
        return list(self.find(collection_name, find_condition).sort(sort_condition).limit(limit_condition))

    def get_collection_dataframe(self, collection_name, find_condition={}, sort_condition=[("_id", pymongo.ASCENDING)], limit_condition=0, selector=None):
        return pd.DataFrame(list(self.find(collection_name, find_condition, selector).sort(sort_condition).limit(limit_condition)))

    def insert_many(self, collection_name, records):
        return self.get_collection_name(collection_name).insert_many(records)

    def insert_dataframe(self, collection_name, df, drop=False):
        if (len(df) > 0):
            if (drop):
                self.get_collection_name(collection_name).delete_many({})
            return self.insert_many(collection_name, df.to_dict('records'))
        else:
            print("Empty DataFrame")

    def find_one(self, collection_name, find_condition={}):
        try:
            return list(self.get_collection_name(collection_name).find(find_condition).limit(1))[0]
        except IndexError:
            return None

    def find(self, collection_name, find_condition={}, selector=None):
        return self.get_collection_name(collection_name).find(find_condition, selector)

    def find_by_id(self, collection_name, id):
        return self.get_collection_name(collection_name).find({"_id": id})

    def insert_one(self, collection_name, record):
        return self.get_collection_name(collection_name).insert_one(record).inserted_id

    def find_one_and_update(self, collection_name, find_condition, update_record):
        return self.get_collection_name(collection_name).find_one_and_update(find_condition, update_record)

    def aggregate(self, collection_name, aggregate_statement):
        return self.get_collection_name(collection_name).aggregate(aggregate_statement)

    def aggregate_dataframe(self, collection_name, aggregate_statement):
        return pd.DataFrame(list(self.get_collection_name(collection_name).aggregate(aggregate_statement)))
