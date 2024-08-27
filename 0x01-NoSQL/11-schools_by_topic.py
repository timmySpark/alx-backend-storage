#!/usr/bin/env python3
'''Task 11. Where can I learn Python?'''


def schools_by_topic(mongo_collection, topic):
    ''' Returns the list of school having a specific topic
        mongo_collection will be the pymongo collection object
        topic (string) will be topic searched
    '''
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
