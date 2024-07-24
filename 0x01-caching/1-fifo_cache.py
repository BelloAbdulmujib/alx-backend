#!/usr/bin/env python3
""" Task 1's module
"""

from base_caching import BaseCaching
from collections import OrderedDict

class FIFOCache(BaseCaching):
    """ Process thst allows to add and remove
        items from the cach using FIFO
    """

    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add's an item to the dic
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            initial_key, other_key = self.cache_data.popitem(False)
            print("DISCARD:", initial_key)

    def get(self, key):
        """ Get's an item linked to 
            the key from the dictionary
        """
        return self.cache_data.get(key, None)
