#!/usr/bin/env python3
"""
FIFO caching Module
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO caching system
    """

    def __init__(self):
        """
        Initialize the cache with FIFO eviction policy.
        """
        super().__init__()

    def put(self, key, item):
        """
        add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = next(iter(self.cache_data))
            del self.cache_data[discarded_key]
            print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
