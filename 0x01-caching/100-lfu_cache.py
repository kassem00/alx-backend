#!/usr/bin/python3
""" LFUCache class """

from base_caching import BaseCaching
from collections import defaultdict

class LFUCache(BaseCaching):
    """ LFUCache class """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.iteration_count = {}       # Track how recently each key is accessed
        self.frequency_count = defaultdict(int)  # Track frequency of each key's use

    def put(self, key, item):
        """ Assign the item to the dictionary """
        if key is None or item is None:
            return

        # Check if the key is already in cache to update frequency and iteration counts
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency_count[key] += 1
        else:
            # Cache is at max capacity, discard an item based on LFU and then LRU
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Identify the key(s) with the lowest frequency
                min_freq = min(self.frequency_count.values())
                least_freq_keys = [k for k, v in self.frequency_count.items() if v == min_freq]
                
                # Choose the least recently used key among those with the lowest frequency
                if len(least_freq_keys) > 1:
                    lru_key = min(least_freq_keys, key=lambda k: self.iteration_count[k])
                else:
                    lru_key = least_freq_keys[0]

                del self.cache_data[lru_key]
                del self.frequency_count[lru_key]
                del self.iteration_count[lru_key]
                print("DISCARD: {}".format(lru_key))

            # Add the new key with initial frequency and iteration counts
            self.cache_data[key] = item
            self.frequency_count[key] = 1
            self.iteration_count[key] = 0

        # Update all keys' iteration count
        for k in self.iteration_count:
            if k != key:
                self.iteration_count[k] += 1

    def get(self, key):
        """ Retrieve the item from the dictionary """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and iteration count on access
        self.frequency_count[key] += 1
        self.iteration_count[key] = 0
        for k in self.iteration_count:
            if k != key:
                self.iteration_count[k] += 1

        return self.cache_data[key]
