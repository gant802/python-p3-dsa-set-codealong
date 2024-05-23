import ipdb
class MySet:
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
            
    def __str__(self):
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'

    def __repr__(self):
        return f"MySet({list(self.dictionary.keys())})"

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True # Add a value as a key on the Dictionary
        return self                   # Return updated set
    
    def delete(self, value):
        self.dictionary.pop(value, None) #The optional second argument None is the return value if the value does not exist in the Dictionary
        return self

    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary.clear()
        return self.dictionary
    
set = MySet([1,2,3,4])

# ipdb.set_trace()