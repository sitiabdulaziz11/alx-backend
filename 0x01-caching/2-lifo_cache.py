#!/usr/bin/python3
"""
LIFO Caching Module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching system"""

    def __init__(self):
        """ Initiliaze"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """put an item in the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                and key not in self.stack:
            del_key = self.stack.pop()
            del self.cache_data[del_key]
            print("DISCARD: {}".format(del_key))
        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """get an item by key"""

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key, None]
