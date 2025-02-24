class StaticArray:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
        self.length = 0
        
    # Array validation
    def insert(self, index, value):
        if self.length >= self.size:
            raise Exception("Array is full")
        if index < 0 or index > self.length:
            raise Exception("Invalid Index")
        # Shifting elements to make space
        for i in range(self.length, index, -1):
            self.array[i] = self.array[i-1]
            
        self.array[index] = value
        self.length += 1
        
    def delete(self, index):
        if index < 0 or index >= self.length:
            raise Exception("Invalid index")
        # gap filling
        for i in range(index, self.length -1):
            self.array[i] = self.array[i+1]
        
        self.array[self.length - 1] = None
        self.length -= 1
        
    def get(self, index):
        if index < 0 or index >= self.length:
            raise Exception("Invalid Index")
        return self.array[index]
    
    def is_full(self):
        return self.length == self.size
    
    def is_empty(self):
        return self.length == 0
    
    
# Example usage and comparison
def array_type_comparison():
    # Static Array Example
    static_arr = StaticArray(5)
    static_arr.insert(0, 1)  # [1, None, None, None, None]
    static_arr.insert(1, 2)  # [1, 2, None, None, None]
    static_arr.insert(2, 3)  # [1, 2, 3, None, None]
    # static_arr.insert(3, 4)  # Works
    # static_arr.insert(4, 5)  # Works
    # static_arr.insert(5, 6)  # Raises Exception: Array is full
    