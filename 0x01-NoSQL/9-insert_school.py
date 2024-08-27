#!/usr/bin/env python3
'''Task 9. Insert a document in Python'''


def insert_school(mongo_collection, **kwargs):
    ''' Insert a document in python
        Return the new _id
    '''
    new_id = mongo_collection.insert_one(kwargs)
    return new_id.inserted_id
