#!/usr/bin/env python3
"""collections in pymongo"""


def list_all(mongo_collection):
    """returs a list of documents in the mongo_collection"""
    return list(mongo_collection.find())
