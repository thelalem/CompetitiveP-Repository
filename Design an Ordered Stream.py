class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.stream[idKey] = value
        result = []
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            result.append(self.stream[self.ptr])
            self.ptr += 1
        return result
