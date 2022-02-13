"""
Design and implement a data structure for LRU (Least Recently Used) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting the new item.
The LRU Cache will be initialized with an integer corresponding to its capacity. Capacity indicates the maximum number of unique keys it can hold at a time.

Definition of “least recently used” : An access to an item is defined as a get or a set operation of the item. “Least recently used” item is the one with the oldest access time.
"""
class ListNode:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None       
        
class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.mapper = {}
        self.head = None
        self.pointers = {}
        self.last_node = None
        
    # @return an integer
    def get(self, key):
        
        #retrieving the value of the key
        if self.mapper.get(key):
            
            #changing the LRU cache(DLL)
            node = self.pointers[key]
            if self.head!=node:
                if node.next == None:
                    self.last_node = node.prev.val
                else:
                    node.next.prev = node.prev
                node.prev.next = node.next
                node.prev = None
                node.next = self.head
                self.head.prev = node
                self.head = node
                
            return self.mapper[key]
        return -1
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.mapper.get(key):
            self.mapper[key] = value
            self.get(key)
            return
        
    
    if self.capacity==len(self.mapper):
        node = self.pointers[self.last_node]
        if self.head == node:
            self.head = None
            temp = None
        else:
            temp = node.prev.val
            node.prev.next = None
            node.prev = None
        del self.mapper[self.last_node]
        del self.pointers[self.last_node]
        self.last_node = temp
        
    
    new_node = ListNode(key)
    new_node.next = self.head
    if self.head ==None:
        self.last_node = new_node.val
    else:
        self.head.prev = new_node
    self.head = new_node
    
    self.mapper[key] = value
    self.pointers[key] = new_node
    return