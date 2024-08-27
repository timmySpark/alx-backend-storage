#!/usr/bin/env python3
'''Task 8: Lists all documents in collection'''


def list_all(mongo_collection):
    ''' List all document in a collection
        Return an empty list if there is no document in the collection
    '''
    return [doc for doc in mongo_collection.find()]
