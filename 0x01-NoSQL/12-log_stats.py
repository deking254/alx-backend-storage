#!/usr/bin/env python3
"""analysing a ninx log file"""
from pymongo import MongoClient
client = MongoClient('mongodb://127.0.0.1:27017')
collections = client.logs.get_collection('nginx')
print('{} logs\nMethods:\n    method GET: {}\n    method POST: {}\n\t\
method PUT: {}\n    method PATCH: {}\n    method DELETE: {}\n\
{} status check'.format(collections.count_documents({}),
                        collections.count_documents({'method': 'GET'}),
                        collections.count_documents({'method': 'POST'}),
                        collections.count_documents({'method': 'PUT'}),
                        collections.count_documents({'method': 'PATCH'}),
                        collections.count_documents({'method': 'DELETE'}),
                        collections.count_documents({'method': 'GET',
                                                    'path': '/status'})))
