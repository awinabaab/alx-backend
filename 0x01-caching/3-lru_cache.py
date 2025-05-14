#!/usr/bin/env python3

"""LRUCaching implementation"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Adds a new key value-pair to the cache"""
        if key and item:
            if key in self.cache_data:
                self.order.remove(key)
                self.order.append(key)
                self.cache_data.update({key: item})
            else:
                self.cache_data.update({key: item})
                self.order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru = self.order.pop(0)
                del self.cache_data[lru]
                print(f"DISCARD: {lru}")

    def get(self, key):
        """Returns the value in the cache linked to key"""
        if key in self.order:
            self.order.remove(key)
            self.order.append(key)
        return self.cache_data.get(key)
