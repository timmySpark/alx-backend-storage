#!/usr/bin/env python3
'''Using Redis with Python'''
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Any


def replay(method: Callable) -> None:
    '''
    Displays the history of calls of a particular function.
    '''
    if not method or not hasattr(method, '__self__'):
        return
    redis_store = method.__self__._redis
    if not isinstance(redis_store, redis.Redis):
        return
    method_name = method.__qualname__
    print(f'{method_name} was called '
          f'{int(redis_store.get(method_name))} times:')
    in_key = f'{method_name}:inputs'
    out_key = f'{method_name}:outputs'
    inputs = redis_store.lrange(in_key, 0, -1)
    outputs = redis_store.lrange(out_key, 0, -1)
    for input, output in zip(inputs, outputs):
        print(f'{method_name}(*{input.decode("utf-8")}) '
              f'-> {output.decode("utf-8")}')


def count_calls(method: Callable) -> Callable:
    '''Records number of times a method was called'''
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        '''Wrapper function'''
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    '''Records call history'''
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> str:
        '''Wrapper function'''
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        result = method(self, *args, *kwargs)
        self._redis.rpush(f"{method.__qualname__}:outputs", result)
        return result
    return wrapper


class Cache:
    '''Implement cache using redis'''
    def __init__(self) -> None:
        '''Init method'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Generates a random key (e.g. using uuid),
        stores the input data in Redis using the random key
        and return the key.
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        '''Retrieves data from Redis'''
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        '''Retrieves string from redis'''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        '''Retrieves int value from redis database'''
        return self.get(key, lambda x: int(x))
