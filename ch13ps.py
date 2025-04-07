class Stack:
    def __init__(self):
        self.stack = []

    # Push item to the top of the stack
    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed to stack.")

    # Pop item from the top of the stack
    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
        else:
            removed = self.stack.pop()
            print(f"{removed} popped from stack.")

    # Peek at the top element
    def peek(self):
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
        else:
            print(f"Top element is: {self.stack[-1]}")

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display all elements
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack (top to bottom):")
            for item in reversed(self.stack):
                print(item)

# ----------------------------------------
# Using the Stack
s = Stack()

# Push elements
s.push(5)
s.push(10)
s.push(15)

# Display stack
s.display()

# Peek at top
s.peek()

# Pop one item
s.pop()

# Display again
s.display()

# Pop all to empty
s.pop()
s.pop()

# Try popping from empty stack
s.pop()

# Final peek
s.peek()
