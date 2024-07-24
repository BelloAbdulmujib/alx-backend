#!/usr/bin/env python3
""" Task 0's module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Caching system's class
    """

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def put(self, key, item):
        """ Assingn a value to the key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieves an item linked to the key
        """

        # if key is None or key not in self.cache_data:
        return self.cache_data.get(key, None)
