'''
Created on April 02, 2021
@author: jgomezm
@Update : 12/04/2024
version: 1.1  
'''
class StackSimpleArray:

    def __init__(self, limit = 10): 
        self.stk = [None for x in range(limit)]
        self.front = -1
        self.limit = limit

    def isEmpty(self):
        return len(self.stk) <= 0

    def size(self):
        return len(self.stk)

    def push(self, item):
        #if len(self.stk) >= self.limit:
        if self.front + 1 >= self.limit:
            print('Stack Overflow!')
        else:
            #self.stk.append(item)
            self.front = self.front + 1
            self.stk[self.front] = item
            print('Stack after Push', self.stk)

    def pop(self):
       #if len(self.stk) <= 0:
        if self.front <= -1:
            print('Stack Underflow!')
            return -1
        else:
            #value = self.stk.pop()
            value = self.stk[self.front]
            self.stk[self.front] = None
            self.front = self.front - 1
            print('Stack after Pop', self.stk)
            return value

    def peek(self):
        if len(self.stk) < 0:
            print('Stack Underflow!')
            return -1
        else:
            return self.stk[-1]


if __name__ == "__main__":

    # Execution
    our_stack = StackSimpleArray(5)
    our_stack.push(1)
    our_stack.push(21)
    our_stack.push(14)
    our_stack.push(31)
    our_stack.push(19)
    our_stack.push(3)
    our_stack.push(99)
    our_stack.push(9)

    # [1,21,14,31,19,3,99,9]
    x = our_stack.pop() # 9
    print(x)
    # [1,21,14,31,19,3,99]

    print( our_stack.size())
    #print( our_stack.peek())
    print( our_stack.pop())
    #print( our_stack.peek())
    print( our_stack.pop()) 
    print( our_stack.pop()) 
    print( our_stack.pop()) 
    print( our_stack.pop()) 

    our_stack.push(19)


