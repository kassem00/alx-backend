#!/usr/bin/python3
""" MRUCache class """


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.iteration_count = {}

    def put(self, key, item):
        """ Assign the item to the dictionary """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.iteration_count[key] = 0
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    m = self.iteration_count.get
                    lru_key = min(self.iteration_count, key=m)
                    del self.cache_data[lru_key]
                    del self.iteration_count[lru_key]
                    print("DISCARD: {}".format(lru_key))

                self.iteration_count[key] = 0

            self.cache_data[key] = item

            for k in self.iteration_count:
                if k != key:
                    self.iteration_count[k] += 1

    def get(self, key):
        """ Retrieve the item from the dictionary """
        if key is None or key not in self.cache_data:
            return None
        self.iteration_count[key] = 0
        for k in self.iteration_count:
            if k != key:
                self.iteration_count[k] += 1

        return self.cache_data.get(key)
