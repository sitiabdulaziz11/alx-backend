#!/usr/bin/python3
"""MRU Caching Module"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ more recently used caching system
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """put an item in the cache
        """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                and key not in self.order:
            del_key = self.order.pop()
            del self.cache_data[del_key]
            print("DISCARD: {}".format(del_key))
        if key in self.order:
            self.order.remove(key)
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
