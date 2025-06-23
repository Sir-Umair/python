# class CustomStack:
#     def __init__(self, max_size):
#         self.stack, self.max_size = [], max_size

#     def push(self, item):
#         if len(self.stack) < self.max_size:
#             self.stack.append(item)
#             print(f"Pushed: {item}")
#         else:
#             print("Stack Overflow!")

#     def pop(self):
#         return self.stack.pop() if self.stack else print("Stack Underflow!")

#     def peek(self):
#         return self.stack[-1] if self.stack else print("Stack is empty.")

#     def display(self):
#         print("Stack:", self.stack if self.stack else "Empty")

# size = int(input("Enter stack size: "))
# stack = CustomStack(size)

# while True:
#     choice = input("\npush/p, pop/o, peek/k, display/d, exit/x: ").lower()
#     if choice in ("push", "p"): stack.push(input("Enter value: "))
#     elif choice in ("pop", "o"): print("Popped:", stack.pop())
#     elif choice in ("peek", "k"): print("Top:", stack.peek())
#     elif choice in ("display", "d"): stack.display()
#     elif choice in ("exit", "x"): break
#     else: print("Invalid choice!")




# FIFO example
class que:
    def __init__(self):
        self.queue=[]
    def enque(self,item):
        if len(self.queue)==0:
           self.queue.append(item) 
           print(f"Enqueued:{item}")
    def is_empty(self):
        return len(self.item)==0
    def deque(self):
        if self.is_empty:
            return None
        return self.item.pop(0)
    def peek (self):
        if self.is_empty:
            return None
        return self.item(0)
    
q=que()
q.enque(10)
q.enque(20)
q.enque(30)
print(q.peek())

class Que:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity  # maximum size of queue

    def enque(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
        else:
            self.queue.append(item)
            print(f"Enqueued: {item}")

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def deque(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

# Testing the queue
q = Que(3)  # capacity = 3
q.enque(10)
q.enque(20)
q.enque(30)
q.enque(40)  # Should print "Queue is full"

print("Front of the queue:", q.peek())
print("Dequeued:", q.deque())
print("Front after dequeue:", q.peek())
q.enque(40)  # Now there's space

class PQ:
    def __init__(self): self.q = []
    def enqueue(self, item, prio): self.q.append((prio, item)); self.q.sort()
    def dequeue(self): return self.q.pop(0)[1] if self.q else None
    def peek(self): return self.q[0][1] if self.q else None





















