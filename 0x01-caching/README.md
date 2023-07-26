# caching system and it's algorithm
A Cache is a storage layer that allows you to store subsets of data
majorly for quick access in the future.

Caching is the processing of creating a storage layer for a subset of
data for future references

Caching basically helps to improve the speed of retrieving data.
There are various caching alogrithm used.

# Caching algorithms
- FIFO
    First-in-First-out, The first data set to be cached will be the first to be removed once
    the storage layer has been fully utilised. This is done to create room for future data sets

- LIFO
    Last-in-First-out, The Last data set to be cached will be the first to be removed pnce the
    storage layer has been fully utilised. Similiar to a stack.

- LRU
    Least Recently Used, The least recently used data set is disregarded in order to create room
    for the most recently used item.

- MRU
    Most Recently Used, The most recently used item is replaced with the new item once the entire block
    has been occupied.

- LFU
    Least Frequently Used, similar to LRU. The least frequently item is replaced with the latest item.
    The frequency at which an item is visited takes predominance.

# Resources:
- (Caching Replace Policies/Algorithms)[https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29]
