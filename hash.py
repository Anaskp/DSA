class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None 

hash = HashTable()

hash['jan'] = 1
hash['feb'] = 2
hash['mar'] = 3
hash['apr'] = 4
hash['may'] = 5
hash['jun'] = 6
hash['jul'] = 7
hash['aug'] = 8
print( hash.arr )
del hash['jul']
print( hash.arr )
