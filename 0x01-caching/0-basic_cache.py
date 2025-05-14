#!/usr/bin/env python3
"""Basic Caching implementation"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache class"""
    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """Adds a new key value-pair to the cache"""
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key):
        """Returns the value in the cache linked to key"""
        return self.cache_data.get(key)
