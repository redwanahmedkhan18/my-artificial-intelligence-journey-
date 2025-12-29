#Implement cache using dictionary

class Cache:
    def __init__(self):
        self.cache_dict = {}

    def set(self, key, value):
        self.cache_dict[key] = value

    def get(self, key):
        return self.cache_dict.get(key, None)

    def delete(self, key):
        if key in self.cache_dict:
            del self.cache_dict[key]

    def clear(self):
        self.cache_dict.clear()

# Example usage
cache = Cache()
cache.set("a", 1)
cache.set("b", 2)
print(cache.get("a"))  # Output: 1
print(cache.get("b"))  # Output: 2
cache.delete("a")
print(cache.get("a"))  # Output: None

