'''
Created on Mar 11, 2019
@author: jgomezm
'''
class StackDynamicArray:

    # Constructor
    def __init__(self, limit = 10):
        #self.stk = [None]*limit
        self.stk = []
        self.limit = limit

    def isEmpty(self):
        return len(self.stk) <= 0

    def push(self, item):
        if len(self.stk) >= self.limit:
            self.resize()
        self.stk.append(item)
        print('Stack after Push',self.stk)

    def pop(self):
        if len(self.stk) <= 0:
            print('Stack Underflow!')
            return 0
        else:
            return self.stk.pop()

    def peek(self):
        if len(self.stk) < 0:
            print('Stack Underflow!')
            return 0
        else:
            return self.stk[-1]

    def size(self):
        return len(self.stk)

    def resize(self):
        self.limit = 2 * self.limit
        #self.stk = list(self.stk)

if __name__ == "__main__":
        
    our_stack = StackDynamicArray(5)
    x = 13
    print(hex(id(x)))
    print(hex(id(our_stack)))
    print("limit -->", our_stack.limit)
    our_stack.push(1)
    print("limit -->", our_stack.limit)
    our_stack.push(21)
    print("limit -->", our_stack.limit)
    our_stack.push(14)
    our_stack.push(11)
    our_stack.push(31)
    our_stack.push(14)
    our_stack.push(15)
    our_stack.push(19)
    print("limit -->", our_stack.limit)
    our_stack.push(3)
    print("limit -->", our_stack.limit)
    our_stack.push(99)
    print("limit -->", our_stack.limit)
    our_stack.push(9)
    print("limit -->", our_stack.limit)
    print( our_stack.peek())
    print( our_stack.pop())
    print( our_stack.peek())
    print( our_stack.pop())