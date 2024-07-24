#!/usr/bin/env python3
""" Task 2's module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """ Process thst allows to add and remove
        items from the cach using LIFO
    """

    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add's an item to the cache
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                final_key, other_key = self.cache_data.popitem(True)
                print("DISCSRD:", final_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ get item in the cach
            with the key value
            """
        return self.cache_data.get(key, None)
