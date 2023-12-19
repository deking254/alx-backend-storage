#!/usr/bin/env python3
"""updating topics in a document"""


def update_topics(mongo_collection, name, topics):
    """update docs in a collection"""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
