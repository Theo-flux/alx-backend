#!/usr/bin/python3
"""
lru caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRU Caching class

    Args:
        BaseCaching (_type_): _description_
    """
    ranked_cache_data = []

    def __init__(self):
        """Intializing"""
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the
        item value for the key key

        Args:
            key (_type_): the key for the item
            item (_type_): the data to cache
        """
        if key is not None and item is not None:
            data_size = len(self.cache_data)
            max_size = super().MAX_ITEMS

            if data_size == max_size and key not in self.cache_data.keys():
                disposedEl = self.ranked_cache_data.pop()
                self.ranked_cache_data.insert(0, key)
                self.cache_data.pop(disposedEl)
                print(f"DISPOSED: {disposedEl}")
            else:
                if key not in self.ranked_cache_data:
                    self.ranked_cache_data.insert(0, key)

            self.ranked_cache_data.remove(key)
            self.ranked_cache_data.insert(0, key)
            self.cache_data[key] = item

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        if key is None or self.cache_data.get(key) is None:
            return None

        self.ranked_cache_data.remove(key)
        self.ranked_cache_data.insert(0, key)
        return self.cache_data.get(key)
