#!/usr/bin/python3
""" LRUCache class """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []
        self.how_many_it_used = {}

    def put(self, key, item):
        """ Assign the item to the dictionary """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)  # Remove the old key
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least recently used key and discard it
                least_used_key = self.order.pop(0)
                del self.cache_data[least_used_key]
                print("DISCARD: {}".format(least_used_key))

            # Add the new key to the cache
            self.cache_data[key] = item
            self.order.append(key)  # Append to end as most recently used
            self.how_many_it_used[key] = self.how_many_it_used.get(key, 0) + 1

    def get(self, key):
        """ Retrieve the item from the dictionary """
        if key is None or key not in self.cache_data:
            return None
        
        # Move the key to the end to mark it as recently used
        self.order.remove(key)
        self.order.append(key)
        self.how_many_it_used[key] += 1

        return self.cache_data.get(key)
