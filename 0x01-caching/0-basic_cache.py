#!/usr/bin/python3
""" BaseCache class """


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BaseCache class """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()

    def put(self, key, item):
        """ Assign the item to the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve the item from the dictionary """
        if key is None:
            return None
        return self.cache_data.get(key)
