#!/usr/bin/env python3
"""returning a document"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    documents = []
    for document in mongo_collection.find():
        if (document.get('topics') != None):
            for topc in document.get('topics'):
                if (topc == topic):
                    documents.append(document)
    return documents
