#!/usr/bin/env python3
"""Basic dictionary Caching task"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Create a class BasicCache that inherits
    from BaseCaching and is a caching system"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return None
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key"""
        if key is None:
            return None
        return self.cache_data.get(key, None)
