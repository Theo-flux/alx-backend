#!/usr/bin/python3
"""fifo caching moduke"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Caching class

    Args:
        BaseCaching (_type_): _description_
    """
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

            if data_size == max_size:
                last_key = list(self.cache_data.keys())[-1]
                self.cache_data.pop(last_key)
                print(f"DISCARD: {last_key}")

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
        return self.cache_data.get(key)
