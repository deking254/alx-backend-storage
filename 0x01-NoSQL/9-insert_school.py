#!/usr/bin/env python3
"""inserting documents"""

def insert_school(mongo_collection, **kwargs):
    """returns a id of the inserted document"""
    return mongo_collection.insert_one(kwargs).inserted_id
