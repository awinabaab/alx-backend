#!/usr/bin/env python3
"""FIFOCaching implementation"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class"""
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Adds a new key value-pair to the cache"""
        if key in self.cache_data:
            self.queue.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = self.queue.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

        if key and item:
            self.cache_data.update({key: item})
            self.queue.append(key)

    def get(self, key):
        """Returns the value in the cache linked to key"""
        return self.cache_data.get(key)
