import random
class RandomizedSet(object):
    '''
    Keep track of the index of the added elements, so when we remove them, we copy the last one into it.
    '''
    def __init__(self):
        self.nums = []
        self.pos = {}  # store indices
        
    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)   # store number in array(end)
            self.pos[val] = len(self.nums) - 1 # store index in hashtable
            return True
        return False
        

    def remove(self, val):
        if val in self.pos: # if entry in hashtable
            idx = self.pos[val] 
            last = self.nums[-1]
            
            # Copy el to be deleted into last element and pop
            self.nums[idx] = last
            self.pos[last] = idx
            
            self.nums.pop()
            self.pos.pop(val, 0) 
            return True
        return False
            
    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()