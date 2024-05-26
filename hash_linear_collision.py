class HashTable:  
    def __init__(self):
        self.MAX = 12
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h][0] != key:
            hx = (h + 1) % self.MAX
            for i in range(self.MAX):
                if self.arr[hx][0] == key:
                    return self.arr[hx]
                hx = (hx + 1) % self.MAX
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if not self.arr[h]:
            self.arr[h] = [key,val]    
        else:
            hx = (h + 1) % self.MAX
            for i in range(self.MAX):
                if not self.arr[hx]:
                    self.arr[hx] = [key,val]
                    break
                hx = (hx + 1) % self.MAX
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h][0] != key:
            hx = (h + 1) % self.MAX
            for i in range(self.MAX):
                if self.arr[hx][0] == key:
                    self.arr[h] = []
                    break
                hx = (hx + 1) % self.MAX
        self.arr[h] = [] 


hash = HashTable()
hash['jan'] = 1
hash['feb'] = 2
hash['mar'] = 3
hash['apr'] = 4
hash['may'] = 5
hash['jun'] = 6
hash['jul'] = 7
hash['aug'] = 8
hash['sep'] = 9
hash['oct'] = 10
hash['nov'] = 11
hash['dec'] = 12
print(hash.arr)
del hash['mar']