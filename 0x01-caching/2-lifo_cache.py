#!/usr/bin/env python3
"""LIFOCaching implementation"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class"""
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Adds a new key value-pair to the cache"""
        if key in self.cache_data:
            self.stack.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        if key and item:
            self.cache_data.update({key: item})
            self.stack.append(key)

    def get(self, key):
        """Returns the value in the cache linked to key"""
        return self.cache_data.get(key)
