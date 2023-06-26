import src.mongopy as mp
import os
from dotenv import load_dotenv
import pandas as pd
import pytest

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")

db = mp.Mongo(MONGODB_URL)


def test_database_connection():
    """Testing: Get Database Connection"""
    db.get_database()


def test_get_collection_dataframe():
    """Testing: Get Collection Dataframe"""
    users = db.get_collection_dataframe("users")
    assert users.iloc[0]["email"] == "sagarmotghare@proton.me"

    assert users.iloc[0]["email"] != "sagarmotghare@proton.me2"


def test_get_collection():
    """Testing: Get Collection"""
    users = db.get_collection("users")
    assert users[0]["email"] == "sagarmotghare@proton.me"

    assert users[0]["email"] != "sagarmotghare@proton.me2"


def test_insert_dataframe():
    """Testing: Insert Dataframe"""
    db.insert_dataframe(
        "test_dataframe",
        df=pd.DataFrame([{"key": "value1"}, {"key": "value2"}]),
    )


def test_find_one():
    """Testing: Find One"""
    if db.find_one(
        collection_name="test_dataframe", find_condition={"key": "value1"}
    ):
        pass
    else:
        pytest.fail("No record Found")
