class LRUCache:

    def __init__(self, capacity: int):
        self.cache: dict[str, int] = {}
        self.capacity: int = capacity
        self.q: list[str] = []

    def reorder(self, key: str):
        self.q.append(self.q.pop(self.q.index(key)))

    def get(self, key: int) -> int:
        value = self.cache.get(str(key), -1)
        if value != -1:
            # Reorder q if key is found in cache
            self.reorder(str(key))
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.get(str(key)) == -1:
            if len(self.cache) == self.capacity:
                # Remove LRU key from q and cache
                LRU_key = self.q.pop(0)
                self.cache.pop(LRU_key)
            
            # Update MRU key and 
            self.q.append(str(key))

        # Update value in cache OR Add pair to cache
        self.cache[str(key)] = value
        
            
