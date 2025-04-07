class Stack:
    def __init__(self):
        self.st = []

    def push(self, item):
        self.st.append(item)
        print(f"ITEM IS PUSHED: {item}")

    def is_empty(self):
        return len(self.st) == 0

    def pop(self):
        if self.is_empty():
            print("IT IS EMPTY")
        else:
            removed = self.st.pop()
            print(f"{removed}: ____ item is popped")

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Cannot peek.")
        else:
            print(f"Top item is: {self.st[-1]}")

    def display(self):
        if self.is_empty():
            print("THIS IS EMPTY")
        else:
            print("Stack items (from top to bottom):")
            for k in reversed(self.st):
                print(f"{k}")

# Testing the stack class
j = Stack()
j.push(6)
j.push(5)
j.pop()
j.display()
j.peek()
j.peek()
j.display()

                

