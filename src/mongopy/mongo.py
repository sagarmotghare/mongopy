import certifi
import pandas as pd
import pymongo
from pymongo import MongoClient


class Mongo:
    '''Create Mongo Object'''
    database = None

    def __init__(self, url):
        '''Initalise Object'''
        self.mongo_client = MongoClient(url, tlsCAFile=certifi.where())

    def set_database(self, database):
        '''Set Database'''
        self.database = database

    def get_database(self):
        '''Get Database'''
        if self.database:
            return self.mongo_client.get_database(self.database)
        return self.mongo_client.get_database()

    def get_collection_name(self, collection_name):
        '''Get Collection name'''
        return self.get_database()[collection_name]

    def get_collection(
        self,
        collection_name,
        find_condition={},
        sort_condition=[("_id", pymongo.ASCENDING)],
        limit_condition=0,
    ):
        '''Get Collection in List'''
        return list(
            self.find(collection_name, find_condition)
            .sort(sort_condition)
            .limit(limit_condition)
        )

    def get_collection_dataframe(
        self,
        collection_name,
        find_condition={},
        sort_condition=[("_id", pymongo.ASCENDING)],
        limit_condition=0,
        selector=None,
    ):
        '''Get Collection Dataframe'''
        return pd.DataFrame(
            list(
                self.find(collection_name, find_condition, selector)
                .sort(sort_condition)
                .limit(limit_condition)
            )
        )

    def insert_many(self, collection_name, records):
        '''Insert Many records'''
        return self.get_collection_name(collection_name).insert_many(records)

    def insert_dataframe(self, collection_name, data_frame, drop=False):
        '''Insert DataFrame'''
        if len(data_frame) > 0:
            if drop:
                self.get_collection_name(collection_name).delete_many({})
            return self.insert_many(collection_name, data_frame.to_dict("records"))
        return []

    def find_one(self, collection_name, find_condition={}):
        '''Find One Record'''
        data = list(
            self.get_collection_name(collection_name)
            .find(find_condition)
                .limit(1)
        )

        if len(data) > 0:
            return data[0]
        return None

    def find(self, collection_name, find_condition={}, selector=None):
        '''Find Records'''
        return self.get_collection_name(collection_name).find(
            find_condition, selector
        )

    def find_by_id(self, collection_name, _id):
        '''Find By ID'''
        return self.get_collection_name(collection_name).find({"_id": _id})

    def insert_one(self, collection_name, record):
        '''Insert One Record'''
        return (
            self.get_collection_name(collection_name)
            .insert_one(record)
            .inserted_id
        )

    def find_one_and_update(
        self, collection_name, find_condition, update_record
    ):
        '''Find One And Update Record'''
        return self.get_collection_name(collection_name).find_one_and_update(
            find_condition, update_record
        )

    def aggregate(self, collection_name, aggregate_statement):
        '''Get Aggregated data'''
        return self.get_collection_name(collection_name).aggregate(
            aggregate_statement
        )

    def aggregate_dataframe(self, collection_name, aggregate_statement):
        '''Get Aggregated data in dataframe'''
        return pd.DataFrame(
            list(
                self.get_collection_name(collection_name).aggregate(
                    aggregate_statement
                )
            )
        )
