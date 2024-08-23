#!/usr/bin/python3
""" LRUCache class """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.iteration_count = {}  # Dictionary to track iteration count of each key

    def put(self, key, item):
        """ Assign the item to the dictionary """
        if key is not None and item is not None:
            if key in self.cache_data:
                # If the key exists, reset its counter
                self.iteration_count[key] = 0
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Find the key with the highest iteration count (least recently used)
                    lru_key = max(self.iteration_count, key=self.iteration_count.get)
                    del self.cache_data[lru_key]
                    del self.iteration_count[lru_key]
                    print("DISCARD: {}".format(lru_key))

                # Add the new key to the cache and reset its counter
                self.iteration_count[key] = 0

            # Insert/update the key and value in the cache
            self.cache_data[key] = item

            # Increment all other counters
            for k in self.iteration_count:
                if k != key:
                    self.iteration_count[k] += 1

    def get(self, key):
        """ Retrieve the item from the dictionary """
        if key is None or key not in self.cache_data:
            return None
        
        # Reset the counter of the accessed key to 0
        self.iteration_count[key] = 0

        # Increment all other counters
        for k in self.iteration_count:
            if k != key:
                self.iteration_count[k] += 1

        return self.cache_data.get(key)
