#!/usr/bin/python3
""" FIFOCache class """


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Assign the item to the dictionary """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print("DISCARD: {}".format(oldest_key))

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Retrieve the item from the dictionary """
        if key is None:
            return None
        return self.cache_data.get(key)
