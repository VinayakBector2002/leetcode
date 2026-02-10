'''
Input: List[List[int]]
    There is a stream of n (idKey -> int , value -> String) pairs 
    arriving in an arbitrary order, where idKey is an integer between 1 and n and 
    value is a string. No two pairs have the same id.

Design a stream that returns the values in increasing order of their IDs by returning a chunk (list) of values after each insertion. The concatenation of all the chunks should result in a list of the sorted values.

Implement the OrderedStream class:
    1. OrderedStream(int n) Constructs the stream to take n values.
    2. String[] insert(int idKey, String value) 
        Inserts the pair (idKey, value) into the stream, 
        then returns the largest possible chunk of currently 
        inserted values that appear next in the order.

'''

class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.arr = [''] * n
        self.start = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey - 1] = value
        prevStart = self.start
        while self.start < self.n and (self.arr[self.start]) != "":
            self.start += 1
        
        return self.arr[prevStart:self.start]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)