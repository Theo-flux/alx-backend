#!/usr/bin/python3
""" basic cache module """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    class inherits from BaseCaching and is a caching system

    Args:
        BaseCaching (_type_): parent class
    """
    def __init__(self):
        """initialising parent init method"""
        super().__init__()

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is not None and item is not None:
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
