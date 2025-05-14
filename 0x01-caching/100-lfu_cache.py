#!/usr/bin/env python3

"""LFUCaching implementation"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class"""
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.access_log = {}

    def put(self, key, item):
        """Adds a new key value-pair to the cache"""
        if key and item:
            if key in self.cache_data:
                if key in self.access_log:
                    self.access_log[key] += 1
                else:
                    self.access_log[key] = 1
            else:
                self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lfu_key = min(self.access_log, key=self.access_log.get)
                del self.cache_data[lfu_key]
                del self.access_log[lfu_key]
                print(f"DISCARD: {lfu_key}")
            self.access_log[key] = 1

    def get(self, key):
        """Returns the value in the cache linked to key"""
        if key in self.cache_data:
            if key in self.access_log:
                self.access_log[key] += 1
            else:
                self.access_log[key] = 1
        return self.cache_data.get(key)
