class DynamicArray:
    def __int__(self):
        self.size = 1
        self.array = [None] * self.size
        self.length = 0
        
    def resize(self, new_size):
        new_array = [None] * new_size
        # COpy element to a new array
        for i in range(self.length):
            new_array[i] = self.array[i]
            self.array = new_array
            self.size = new_size
            
    def append(self, value):
        if self.length == self.size:
            # Doubling the array when full
            self.resize(self.size * 2)
            
        self.array[self.length] = value
        self.lenght += 1
        
    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise Exception("Invalid Index")
        if self.length == self.size:
            self.resize(self.size * 2)
            
        # Shifting elements to make space
        for i in range(self.length, index, -1):
            self.array[i] = self.array[i-1]
            
        self.array[index] = value
        self.length += 1
        
    def delete(self, index):
        if index < 0 or index >= self.length:
            raise Exception("Invalid index")
        for i in range(index, self.length - 1):
            self.array[self.length -1] = None
            self.length -= 1
        
        # Shrink array if too sparse
        if self.length < self.size // 4:
            self.resize(self.size // 2)
            
    def get(self, index):
        if index < 0 or index >= self.length:
            raise Exception("Invalid index")
        
        return self.array[index]
    
    # Example usage and comparison
    def array_type_comparison():
        dynamic_arr = DynamicArray()
        # Initial size is 1
        dynamic_arr.append(1)  # [1]
        # Resize to 2
        dynamic_arr.append(2)  # [1, 2]
        # Resize to 4
        dynamic_arr.append(3)  # [1, 2, 3, None]
        dynamic_arr.append(4)  # [1, 2, 3, 4]
        # Resize to 8
        dynamic_arr.append(5)  # [1, 2, 3, 4, 5, None, None, None]