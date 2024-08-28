#!/usr/bin/env python3
'''Task 12: Log stats
'''
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''Prints stats about Nginx request logs.'''
    print('{} logs'.format(nginx_collection.count_documents({})))

    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        count = nginx_collection.count_documents({'method': method})
        print(f'\tmethod {method}: {count}')

    status_check_count = nginx_collection.count_documents(
        {'method': 'GET', 'path': '/status'}
    )
    print('{} status check'.format(status_check_count))


def run():
    '''Provides some stats about Nginx logs stored in MongoDB.'''
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print_nginx_request_logs(nginx_collection)


if __name__ == '__main__':
    run()
